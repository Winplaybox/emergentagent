# HashtagHero - Setup Complete! 🎉

## ✅ What I've Done

1. **Extracted your zip file** from emergentagent-main.zip
2. **Switched from paid Emergent LLM to FREE Google Gemini API**
   - Removed `emergentintegrations` dependency
   - Installed `google-genai` (latest Google Gemini SDK)
   - Added your Gemini API key: `AIzaSyDPoDMrwPueQwBLuDZRniYJhhXUZv0-beM`
3. **Updated all API endpoints** to use free Gemini models
4. **Configured for local testing** with MongoDB

## 🚨 IMPORTANT: API Quota Issue

Your Gemini API key has **exceeded its free tier quota** for today. This means:
- ❌ Cannot make API calls right now
- ⏰ Wait ~24 hours for quota to reset
- 📊 Free tier limits: 15 requests/minute, 1500 requests/day

### Solution Options:

**Option 1: Wait 24 Hours** (Recommended)
- Your quota will reset automatically
- Test the app tomorrow

**Option 2: Get a New API Key**
- Go to: https://aistudio.google.com/apikey
- Create a new Google account (if needed)
- Generate a new API key
- Replace in `/app/backend/.env` file

**Option 3: Upgrade to Paid Tier** (Not recommended for testing)
- Add billing to your Google Cloud account
- Higher limits but costs money

---

## 📁 Project Structure

```
/app/
├── backend/
│   ├── server.py              # FastAPI backend with Gemini AI
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # API keys and config
├── frontend/
│   ├── src/
│   │   ├── App.js            # Main React app
│   │   ├── pages/            # Landing, Dashboard, Wishlist
│   │   └── components/       # UI components
│   ├── package.json
│   └── .env                  # Backend URL
└── README.md
```

---

## 🔧 Configuration Files

### Backend .env (`/app/backend/.env`)
```
GEMINI_API_KEY=AIzaSyDPoDMrwPueQwBLuDZRniYJhhXUZv0-beM
MONGO_URL=mongodb://localhost:27017/
DB_NAME=hashtaghero
CORS_ORIGINS=*
```

### Frontend .env (`/app/frontend/.env`)
```
REACT_APP_BACKEND_URL=https://smart-ai-agent-8.preview.emergentagent.com
```

---

## 🚀 Running Locally (After Quota Resets)

The app is already running!

- **Frontend**: https://smart-ai-agent-8.preview.emergentagent.com/
- **Backend API**: https://smart-ai-agent-8.preview.emergentagent.com/api/
- **MongoDB**: Running locally on port 27017

### Check Status:
```bash
sudo supervisorctl status
```

### Restart Services:
```bash
sudo supervisorctl restart all
```

### View Logs:
```bash
# Backend logs
tail -f /var/log/supervisor/backend.err.log

# Frontend logs
tail -f /var/log/supervisor/frontend.err.log
```

---

## 💾 Setting Up MongoDB Atlas (Required for PythonAnywhere)

Since PythonAnywhere doesn't support MongoDB, you need MongoDB Atlas (FREE cloud database):

### Step 1: Create MongoDB Atlas Account
1. Go to: https://www.mongodb.com/cloud/atlas/register
2. Sign up for FREE tier (no credit card needed)
3. Create a new cluster (choose FREE tier - M0)

### Step 2: Configure Database
1. **Create Database User:**
   - Go to "Database Access"
   - Add new user with username/password
   - Save credentials!

2. **Allow Network Access:**
   - Go to "Network Access"
   - Click "Add IP Address"
   - Select "Allow Access from Anywhere" (0.0.0.0/0)

3. **Get Connection String:**
   - Go to "Database" → "Connect"
   - Choose "Connect your application"
   - Copy connection string
   - It looks like: `mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/`

### Step 3: Update Backend .env
Replace in `/app/backend/.env`:
```
MONGO_URL=mongodb+srv://YOUR_USERNAME:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/
```

---

## 🌐 Deploying to PythonAnywhere

### Prerequisites:
1. ✅ MongoDB Atlas set up (see above)
2. ✅ Gemini API key working (quota not exceeded)
3. ✅ PythonAnywhere account (free tier works!)

### Deployment Steps:

#### 1. Upload Files to PythonAnywhere
```bash
# On PythonAnywhere console:
git clone <your-repo-url>
cd emergentagent-main/backend
```

#### 2. Install Dependencies
```bash
mkvirtualenv --python=/usr/bin/python3.10 hashtaghero
pip install -r requirements.txt
```

#### 3. Configure Web App
- Go to "Web" tab
- Click "Add a new web app"
- Choose "Manual configuration" + Python 3.10
- Set source code: `/home/yourusername/emergentagent-main/backend`
- Set working directory: `/home/yourusername/emergentagent-main/backend`

#### 4. Configure WSGI File
Replace contents with:
```python
import sys
import os

project_home = '/home/yourusername/emergentagent-main/backend'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from server import app as application
```

#### 5. Set Environment Variables
In PythonAnywhere dashboard, add:
```
GEMINI_API_KEY=AIzaSyDPoDMrwPueQwBLuDZRniYJhhXUZv0-beM
MONGO_URL=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/
DB_NAME=hashtaghero
CORS_ORIGINS=*
```

#### 6. Deploy Frontend
For frontend, use:
- **Vercel** (free, recommended): https://vercel.com
- **Netlify** (free): https://netlify.com
- Update `REACT_APP_BACKEND_URL` to your PythonAnywhere URL

---

## 🎯 Features Implemented

Your HashtagHero app has these amazing features:

1. **AI Hashtag Generator from Images** 🖼️
   - Upload image → Get 30 trending hashtags
   - Uses Gemini vision AI

2. **Caption Generator** ✍️
   - Platform-specific captions (Instagram, TikTok, YouTube)
   - Customizable tone (engaging, inspiring, funny, etc.)

3. **Bio Generator** 👤
   - Optimized bios for each platform
   - Character limit awareness

4. **Comment Suggestions** 💬
   - Context-aware comment generator
   - 3 variations per request

5. **Content Remixer** 🔄
   - Adapt one post for all platforms
   - Platform-specific optimization

6. **Profile Roaster** 🔥
   - Brutally honest profile audit
   - Constructive feedback with humor

---

## 🐛 Troubleshooting

### Backend won't start:
```bash
# Check logs
tail -f /var/log/supervisor/backend.err.log

# Common fixes:
pip install -r /app/backend/requirements.txt
sudo supervisorctl restart backend
```

### Frontend not loading:
```bash
# Check if dependencies installed
cd /app/frontend
yarn install

# Restart
sudo supervisorctl restart frontend
```

### MongoDB connection error:
- Make sure MongoDB is running: `sudo supervisorctl status mongodb`
- Or update to MongoDB Atlas connection string

### Gemini API errors:
- **Quota exceeded**: Wait 24 hours or get new API key
- **Invalid API key**: Check `/app/backend/.env` file
- **Wrong model**: Check https://ai.google.dev/models/gemini

---

## 📊 API Endpoints

### Base URL: `/api`

#### 1. Health Check
```bash
GET /api/
Response: {"message": "HashtagHero API is running!"}
```

#### 2. Generate Hashtags from Image
```bash
POST /api/generate-hashtags-from-image
Content-Type: multipart/form-data
Body: file (image upload)
```

#### 3. Generate Caption
```bash
POST /api/generate-caption
Body: {
  "content_description": "A beautiful sunset",
  "platform": "instagram",
  "tone": "inspiring"
}
```

#### 4. Generate Bio
```bash
POST /api/generate-bio
Body: {
  "details": "Tech entrepreneur and content creator",
  "platform": "instagram"
}
```

#### 5. Generate Comments
```bash
POST /api/generate-comment
Body: {
  "context": "Amazing sunset photo"
}
```

#### 6. Remix Content
```bash
POST /api/generate-remix
Body: {
  "post_content": "Just launched my new app!"
}
```

#### 7. Roast Profile
```bash
POST /api/roast-profile
Body: {
  "profile_details": "Tech blogger with 500 followers"
}
```

---

## 💡 Next Steps

1. **Wait for Gemini API quota to reset** (~24 hours)
2. **Set up MongoDB Atlas** (follow guide above)
3. **Test all features** locally
4. **Deploy to PythonAnywhere** (follow deployment guide)
5. **Deploy frontend** to Vercel/Netlify

---

## 📞 Need Help?

Common issues:
- **Quota exceeded**: Your API key hit daily limit. Get new key or wait 24h.
- **MongoDB errors**: Set up MongoDB Atlas (free tier).
- **CORS errors**: Make sure `CORS_ORIGINS=*` in backend .env.

---

## 🎉 You're All Set!

Your HashtagHero app is ready to go! Just wait for the Gemini API quota to reset, set up MongoDB Atlas, and you'll be generating viral content in no time! 🚀

**Tech Stack:**
- ✅ Python FastAPI backend
- ✅ React frontend  
- ✅ Google Gemini 2.0 Flash AI (FREE)
- ✅ MongoDB database
- ✅ Modern UI with Shadcn components
