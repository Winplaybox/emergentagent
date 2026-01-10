import requests
import sys
import base64
import json
from datetime import datetime
from PIL import Image
from io import BytesIO
import numpy as np

class HashtagHeroAPITester:
    def __init__(self, base_url="https://hashtaghero.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def log_result(self, test_name, success, details=""):
        """Log test results"""
        self.tests_run += 1
        if success:
            self.tests_passed += 1
            print(f"✅ {test_name} - PASSED")
        else:
            self.failed_tests.append(f"{test_name}: {details}")
            print(f"❌ {test_name} - FAILED: {details}")

    def create_test_image(self):
        """Create a test image with actual visual features"""
        # Create a 200x200 image with varied content
        img = Image.new('RGB', (200, 200), color='white')
        pixels = img.load()
        
        # Add some visual features - gradient and shapes
        for i in range(200):
            for j in range(200):
                # Create a gradient with some geometric patterns
                r = int(255 * (i / 200))
                g = int(255 * (j / 200))
                b = int(128 + 127 * np.sin(i * j / 1000))
                pixels[i, j] = (r, g, b)
        
        # Convert to base64
        buffered = BytesIO()
        img.save(buffered, format="JPEG", quality=85)
        img_base64 = base64.b64encode(buffered.getvalue()).decode()
        
        return img_base64

    def test_api_root(self):
        """Test API root endpoint"""
        try:
            response = requests.get(f"{self.base_url}/api/")
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            if success:
                data = response.json()
                details += f", Message: {data.get('message', 'No message')}"
            self.log_result("API Root", success, details)
            return success
        except Exception as e:
            self.log_result("API Root", False, str(e))
            return False

    def test_status_endpoints(self):
        """Test status check endpoints"""
        try:
            # Test POST status
            test_data = {"client_name": f"test_client_{datetime.now().strftime('%H%M%S')}"}
            response = requests.post(f"{self.base_url}/api/status", json=test_data)
            success = response.status_code == 200
            
            if success:
                data = response.json()
                required_fields = ['id', 'client_name', 'timestamp']
                missing_fields = [field for field in required_fields if field not in data]
                if missing_fields:
                    success = False
                    details = f"Missing fields: {missing_fields}"
                else:
                    details = f"Created status with ID: {data['id']}"
            else:
                details = f"Status: {response.status_code}"
            
            self.log_result("POST Status", success, details)
            
            # Test GET status
            response = requests.get(f"{self.base_url}/api/status")
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            if success:
                data = response.json()
                details += f", Found {len(data)} status checks"
            
            self.log_result("GET Status", success, details)
            return success
            
        except Exception as e:
            self.log_result("Status Endpoints", False, str(e))
            return False

    def test_generate_hashtags_from_image(self):
        """Test image-to-hashtag generation"""
        try:
            img_base64 = self.create_test_image()
            
            # Convert base64 to file-like object for multipart upload
            img_data = base64.b64decode(img_base64)
            files = {'file': ('test_image.jpg', BytesIO(img_data), 'image/jpeg')}
            
            response = requests.post(f"{self.base_url}/api/generate-hashtags-from-image", files=files)
            success = response.status_code == 200
            
            if success:
                data = response.json()
                required_fields = ['result', 'character_count', 'platform_limit', 'hashtag_count']
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    success = False
                    details = f"Missing fields: {missing_fields}"
                else:
                    hashtag_count = data.get('hashtag_count', 0)
                    char_count = data.get('character_count', 0)
                    result = data.get('result', '')
                    
                    # Validate hashtags format
                    hashtags_valid = '#' in result and hashtag_count > 0
                    if not hashtags_valid:
                        success = False
                        details = f"Invalid hashtags format or count: {hashtag_count}"
                    else:
                        details = f"Generated {hashtag_count} hashtags, {char_count} chars"
            else:
                details = f"Status: {response.status_code}, Response: {response.text[:200]}"
            
            self.log_result("Generate Hashtags from Image", success, details)
            return success
            
        except Exception as e:
            self.log_result("Generate Hashtags from Image", False, str(e))
            return False

    def test_generate_caption(self):
        """Test caption generation"""
        try:
            test_data = {
                "content_description": "Morning coffee at a cozy cafe, latte art",
                "platform": "instagram",
                "tone": "engaging"
            }
            
            response = requests.post(f"{self.base_url}/api/generate-caption", json=test_data)
            success = response.status_code == 200
            
            if success:
                data = response.json()
                required_fields = ['result', 'character_count', 'platform_limit']
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    success = False
                    details = f"Missing fields: {missing_fields}"
                else:
                    char_count = data.get('character_count', 0)
                    platform_limit = data.get('platform_limit', 0)
                    result = data.get('result', '')
                    
                    # Validate character limit
                    if char_count > platform_limit:
                        success = False
                        details = f"Caption exceeds limit: {char_count}/{platform_limit}"
                    else:
                        details = f"Generated caption: {char_count}/{platform_limit} chars"
            else:
                details = f"Status: {response.status_code}, Response: {response.text[:200]}"
            
            self.log_result("Generate Caption", success, details)
            return success
            
        except Exception as e:
            self.log_result("Generate Caption", False, str(e))
            return False

    def test_generate_bio(self):
        """Test bio generation"""
        try:
            test_data = {
                "details": "Travel blogger, foodie, photographer. Based in NYC",
                "platform": "instagram"
            }
            
            response = requests.post(f"{self.base_url}/api/generate-bio", json=test_data)
            success = response.status_code == 200
            
            if success:
                data = response.json()
                required_fields = ['result', 'character_count', 'platform_limit']
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    success = False
                    details = f"Missing fields: {missing_fields}"
                else:
                    char_count = data.get('character_count', 0)
                    platform_limit = data.get('platform_limit', 150)  # Instagram limit
                    
                    if char_count > platform_limit:
                        success = False
                        details = f"Bio exceeds limit: {char_count}/{platform_limit}"
                    else:
                        details = f"Generated bio: {char_count}/{platform_limit} chars"
            else:
                details = f"Status: {response.status_code}, Response: {response.text[:200]}"
            
            self.log_result("Generate Bio", success, details)
            return success
            
        except Exception as e:
            self.log_result("Generate Bio", False, str(e))
            return False

    def test_generate_comment(self):
        """Test comment generation"""
        try:
            test_data = {
                "context": "A fitness influencer sharing their morning routine"
            }
            
            response = requests.post(f"{self.base_url}/api/generate-comment", json=test_data)
            success = response.status_code == 200
            
            if success:
                data = response.json()
                required_fields = ['result', 'character_count']
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    success = False
                    details = f"Missing fields: {missing_fields}"
                else:
                    result = data.get('result', '')
                    char_count = data.get('character_count', 0)
                    
                    # Check if comments are separated by ---
                    comment_count = result.count('---') + 1 if result else 0
                    if comment_count < 3:
                        success = False
                        details = f"Expected 3 comments, got {comment_count}"
                    else:
                        details = f"Generated {comment_count} comments, {char_count} chars"
            else:
                details = f"Status: {response.status_code}, Response: {response.text[:200]}"
            
            self.log_result("Generate Comment", success, details)
            return success
            
        except Exception as e:
            self.log_result("Generate Comment", False, str(e))
            return False

    def test_generate_remix(self):
        """Test remix generation"""
        try:
            test_data = {
                "post_content": "Just launched my new product! So excited to share this with you all"
            }
            
            response = requests.post(f"{self.base_url}/api/generate-remix", json=test_data)
            success = response.status_code == 200
            
            if success:
                data = response.json()
                required_fields = ['instagram', 'tiktok', 'youtube']
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    success = False
                    details = f"Missing fields: {missing_fields}"
                else:
                    platforms = ['instagram', 'tiktok', 'youtube']
                    platform_results = []
                    for platform in platforms:
                        content = data.get(platform, '')
                        if content and content != f"Unable to generate {platform.title()} version":
                            platform_results.append(f"{platform}: {len(content)} chars")
                        else:
                            success = False
                            platform_results.append(f"{platform}: FAILED")
                    
                    details = ", ".join(platform_results)
            else:
                details = f"Status: {response.status_code}, Response: {response.text[:200]}"
            
            self.log_result("Generate Remix", success, details)
            return success
            
        except Exception as e:
            self.log_result("Generate Remix", False, str(e))
            return False

    def test_roast_profile(self):
        """Test profile roast generation"""
        try:
            test_data = {
                "profile_details": "Food blogger, 500 followers, posts 2x per week, low engagement"
            }
            
            response = requests.post(f"{self.base_url}/api/roast-profile", json=test_data)
            success = response.status_code == 200
            
            if success:
                data = response.json()
                required_fields = ['result', 'character_count']
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    success = False
                    details = f"Missing fields: {missing_fields}"
                else:
                    char_count = data.get('character_count', 0)
                    result = data.get('result', '')
                    
                    if char_count == 0 or not result:
                        success = False
                        details = "Empty roast response"
                    else:
                        details = f"Generated roast: {char_count} chars"
            else:
                details = f"Status: {response.status_code}, Response: {response.text[:200]}"
            
            self.log_result("Roast Profile", success, details)
            return success
            
        except Exception as e:
            self.log_result("Roast Profile", False, str(e))
            return False

    def run_all_tests(self):
        """Run all API tests"""
        print("🚀 Starting HashtagHero API Tests...")
        print(f"Testing against: {self.base_url}")
        print("=" * 50)
        
        # Test basic connectivity first
        if not self.test_api_root():
            print("❌ API root test failed - stopping further tests")
            return False
        
        # Test all endpoints
        self.test_status_endpoints()
        self.test_generate_hashtags_from_image()
        self.test_generate_caption()
        self.test_generate_bio()
        self.test_generate_comment()
        self.test_generate_remix()
        self.test_roast_profile()
        
        # Print summary
        print("\n" + "=" * 50)
        print(f"📊 Test Results: {self.tests_passed}/{self.tests_run} passed")
        
        if self.failed_tests:
            print("\n❌ Failed Tests:")
            for failure in self.failed_tests:
                print(f"  - {failure}")
        
        return self.tests_passed == self.tests_run

def main():
    tester = HashtagHeroAPITester()
    success = tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())