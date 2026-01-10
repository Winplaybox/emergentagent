from fastapi import FastAPI, APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
import uuid
from datetime import datetime, timezone
import base64
from io import BytesIO
from PIL import Image
from google import genai
from google.genai import types

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017/')
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ.get('DB_NAME', 'hashtaghero')]

# Configure Gemini API
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# Create the main app
app = FastAPI()
api_router = APIRouter(prefix="/api")

# Models
class StatusCheck(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class StatusCheckCreate(BaseModel):
    client_name: str

class GenerateCaptionRequest(BaseModel):
    content_description: str
    platform: str
    tone: Optional[str] = "engaging"

class GenerateBioRequest(BaseModel):
    details: str
    platform: str

class GenerateCommentRequest(BaseModel):
    context: str

class GenerateRemixRequest(BaseModel):
    post_content: str

class RoastProfileRequest(BaseModel):
    profile_details: str

class GeneratedResponse(BaseModel):
    result: str
    character_count: int
    platform_limit: Optional[int] = None

class RemixResponse(BaseModel):
    instagram: str
    tiktok: str
    youtube: str

# Helper function to create Gemini model
def create_gemini_model(system_instruction: str):
    return system_instruction  # Return system instruction for use in prompts

# Helper function to convert image to PIL Image
async def process_uploaded_image(file: UploadFile) -> Image.Image:
    contents = await file.read()
    image = Image.open(BytesIO(contents))
    
    # Convert to RGB if needed
    if image.mode in ('RGBA', 'LA', 'P'):
        image = image.convert('RGB')
    
    # Resize if too large (max 2048px)
    max_size = 2048
    if max(image.size) > max_size:
        ratio = max_size / max(image.size)
        new_size = tuple(int(dim * ratio) for dim in image.size)
        image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    return image

# Routes
@api_router.get("/")
async def root():
    return {"message": "HashtagHero API is running!"}

@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_dict = input.model_dump()
    status_obj = StatusCheck(**status_dict)
    doc = status_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    _ = await db.status_checks.insert_one(doc)
    return status_obj

@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    status_checks = await db.status_checks.find({}, {"_id": 0}).to_list(1000)
    for check in status_checks:
        if isinstance(check['timestamp'], str):
            check['timestamp'] = datetime.fromisoformat(check['timestamp'])
    return status_checks

@api_router.post("/generate-hashtags-from-image")
async def generate_hashtags_from_image(file: UploadFile = File(...)):
    try:
        # Process image
        image = await process_uploaded_image(file)
        
        # Create Gemini model with vision
        model = create_gemini_model(
            "You are a viral social media expert specializing in Instagram, TikTok, and YouTube Shorts. "
            "Analyze images and generate trending, SEO-optimized hashtags that maximize reach and engagement."
        )
        
        prompt = (
            "Analyze this image and generate 30 trending, viral hashtags optimized for Instagram, TikTok, and YouTube Shorts. "
            "Mix popular hashtags (100k-1M posts) with niche-specific tags. Format: #hashtag1 #hashtag2 (no commas, just spaces). "
            "Focus on the main subject, mood, colors, and aesthetic. Make them SEO-optimized and trendy."
        )
        
        # Generate response
        response = model.generate_content([prompt, image])
        hashtags = response.text.strip()
        char_count = len(hashtags)
        
        return {
            "result": hashtags,
            "character_count": char_count,
            "platform_limit": 2200,
            "hashtag_count": len([tag for tag in hashtags.split() if tag.startswith('#')])
        }
    
    except Exception as e:
        logging.error(f"Error generating hashtags from image: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to generate hashtags: {str(e)}"}
        )

@api_router.post("/generate-caption", response_model=GeneratedResponse)
async def generate_caption(request: GenerateCaptionRequest):
    try:
        platform_limits = {
            "instagram": 2200,
            "tiktok": 2200,
            "youtube": 5000
        }
        
        limit = platform_limits.get(request.platform.lower(), 2200)
        
        model = create_gemini_model(
            f"You are a viral content creator for {request.platform}. Create engaging, authentic captions that drive engagement. "
            f"Keep captions under {limit} characters. Use {request.tone} tone."
        )
        
        prompt = (
            f"Create a compelling {request.platform} caption for: {request.content_description}. "
            f"Make it {request.tone}, add emojis naturally, include 3-5 relevant hashtags at the end. "
            f"Keep under {limit} characters total."
        )
        
        response = model.generate_content(prompt)
        caption = response.text.strip()
        
        return GeneratedResponse(
            result=caption,
            character_count=len(caption),
            platform_limit=limit
        )
    
    except Exception as e:
        logging.error(f"Error generating caption: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to generate caption: {str(e)}"}
        )

@api_router.post("/generate-bio", response_model=GeneratedResponse)
async def generate_bio(request: GenerateBioRequest):
    try:
        platform_limits = {
            "instagram": 150,
            "tiktok": 80,
            "youtube": 1000
        }
        
        limit = platform_limits.get(request.platform.lower(), 150)
        
        model = create_gemini_model(
            f"You are a social media strategist specializing in profile optimization for {request.platform}. "
            f"Create bios that are memorable, clear, and optimized for discoverability. "
            f"CRITICAL: You MUST keep the bio under {limit} characters. This is a hard limit that cannot be exceeded."
        )
        
        prompt = (
            f"Create an optimized {request.platform} bio based on: {request.details}. "
            f"IMPORTANT: The bio MUST be under {limit} characters (current limit for {request.platform}). "
            f"Make it catchy, clear, and memorable. Use emojis strategically. "
            f"Include a call-to-action if appropriate. "
            f"Count characters carefully and ensure you stay under {limit} characters total."
        )
        
        response = model.generate_content(prompt)
        bio = response.text.strip()
        
        return GeneratedResponse(
            result=bio,
            character_count=len(bio),
            platform_limit=limit
        )
    
    except Exception as e:
        logging.error(f"Error generating bio: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to generate bio: {str(e)}"}
        )

@api_router.post("/generate-comment", response_model=GeneratedResponse)
async def generate_comment(request: GenerateCommentRequest):
    try:
        model = create_gemini_model(
            "You are an engagement expert. Generate authentic, thoughtful comments that spark conversations. "
            "Avoid generic responses. Be genuine, specific, and add value."
        )
        
        prompt = (
            f"Generate 3 different engaging comment suggestions for this context: {request.context}. "
            f"Make them authentic, specific, and conversational. Separate each with '---'. "
            f"Keep each comment under 150 characters."
        )
        
        response = model.generate_content(prompt)
        comments = response.text.strip()
        
        return GeneratedResponse(
            result=comments,
            character_count=len(comments),
            platform_limit=None
        )
    
    except Exception as e:
        logging.error(f"Error generating comment: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to generate comment: {str(e)}"}
        )

@api_router.post("/generate-remix", response_model=RemixResponse)
async def generate_remix(request: GenerateRemixRequest):
    try:
        model = create_gemini_model(
            "You are a cross-platform content strategist. Adapt content for Instagram, TikTok, and YouTube Shorts "
            "by optimizing for each platform's unique audience, format, and algorithm."
        )
        
        prompt = (
            f"Adapt this content for Instagram, TikTok, and YouTube Shorts: '{request.post_content}'. "
            f"For each platform, create an optimized version considering: "
            f"Instagram (aesthetic, community, 2200 char limit), "
            f"TikTok (trendy, authentic, 2200 char limit), "
            f"YouTube (searchable, engaging, 5000 char limit). "
            f"Format your response EXACTLY as: "
            f"INSTAGRAM: [content]\n\nTIKTOK: [content]\n\nYOUTUBE: [content]"
        )
        
        response = model.generate_content(prompt)
        text = response.text
        
        # Parse response
        parts = text.split('\n\n')
        instagram_content = ""
        tiktok_content = ""
        youtube_content = ""
        
        for part in parts:
            if part.startswith('INSTAGRAM:'):
                instagram_content = part.replace('INSTAGRAM:', '').strip()
            elif part.startswith('TIKTOK:'):
                tiktok_content = part.replace('TIKTOK:', '').strip()
            elif part.startswith('YOUTUBE:'):
                youtube_content = part.replace('YOUTUBE:', '').strip()
        
        return RemixResponse(
            instagram=instagram_content or "Unable to generate Instagram version",
            tiktok=tiktok_content or "Unable to generate TikTok version",
            youtube=youtube_content or "Unable to generate YouTube version"
        )
    
    except Exception as e:
        logging.error(f"Error generating remix: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to generate remix: {str(e)}"}
        )

@api_router.post("/roast-profile", response_model=GeneratedResponse)
async def roast_profile(request: RoastProfileRequest):
    try:
        model = create_gemini_model(
            "You are a brutally honest social media consultant. Provide constructive criticism with humor. "
            "Be direct but helpful. Point out what's not working and give actionable advice to improve."
        )
        
        prompt = (
            f"Roast/audit this social media profile: {request.profile_details}. "
            f"Be honest and funny but constructive. Point out: "
            f"1) What's not working (bio, content strategy, engagement tactics) "
            f"2) Specific improvements they should make "
            f"3) What they're doing right (if anything). "
            f"Keep it under 500 words, make it entertaining but valuable."
        )
        
        response = model.generate_content(prompt)
        roast = response.text.strip()
        
        return GeneratedResponse(
            result=roast,
            character_count=len(roast),
            platform_limit=None
        )
    
    except Exception as e:
        logging.error(f"Error generating roast: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to generate roast: {str(e)}"}
        )

# Include router
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
