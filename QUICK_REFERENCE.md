# Quick Reference Card 📋

## ✅ Setup Status

- ✅ Zip file extracted
- ✅ Free Gemini API integrated (google-genai SDK)
- ✅ Your API key added
- ⚠️ Gemini API quota exceeded (wait 24h or get new key)
- ⏳ MongoDB Atlas setup needed (for PythonAnywhere)

---

## 🔑 Your Credentials

**Gemini API Key:**
```
AIzaSyDPoDMrwPueQwBLuDZRniYJhhXUZv0-beM
```

**Issue:** Quota exceeded for today
**Solution:** Wait 24 hours OR get new key from https://aistudio.google.com/apikey

---

## 📁 Important Files

| File | Purpose |
|------|---------|
| `/app/backend/server.py` | Main FastAPI backend (Gemini AI integration) |
| `/app/backend/.env` | API keys and database config |
| `/app/backend/requirements.txt` | Python dependencies |
| `/app/frontend/src/App.js` | Main React app |
| `/app/frontend/.env` | Backend URL configuration |
| `/app/SETUP_GUIDE.md` | Complete setup documentation |
| `/app/MONGODB_ATLAS_SETUP.md` | MongoDB Atlas tutorial |

---

## ⚡ Quick Commands

### Check Status:
```bash
sudo supervisorctl status
```

### Restart Services:
```bash
# Restart everything
sudo supervisorctl restart all

# Restart backend only
sudo supervisorctl restart backend

# Restart frontend only
sudo supervisorctl restart frontend
```

### View Logs:
```bash
# Backend logs (errors)
tail -f /var/log/supervisor/backend.err.log

# Frontend logs
tail -f /var/log/supervisor/frontend.err.log

# All backend logs
tail -f /var/log/supervisor/backend.*.log
```

### Test Backend API:
```bash
# Health check
curl http://localhost:8001/api/

# Test caption generation (will fail until quota resets)
curl -X POST http://localhost:8001/api/generate-caption \
  -H "Content-Type: application/json" \
  -d '{"content_description": "sunset beach", "platform": "instagram", "tone": "inspiring"}'
```

---

## 🌐 Access URLs

- **Frontend:** https://smart-ai-agent-8.preview.emergentagent.com/
- **Backend API:** https://smart-ai-agent-8.preview.emergentagent.com/api/

---

## 📋 Next Steps (In Order)

### 1. Fix Gemini API Quota ⏰
**Option A:** Wait 24 hours for quota reset
**Option B:** Get new API key from https://aistudio.google.com/apikey
- Create new Google account if needed
- Generate new API key
- Update in `/app/backend/.env`
- Restart backend

### 2. Setup MongoDB Atlas ☁️
**Why:** PythonAnywhere doesn't support local MongoDB
**Time:** 5 minutes
**Guide:** Read `/app/MONGODB_ATLAS_SETUP.md`
**Steps:**
1. Create free account at https://www.mongodb.com/cloud/atlas/register
2. Create M0 (free) cluster
3. Get connection string
4. Update `/app/backend/.env`
5. Restart backend

### 3. Test Locally 🧪
Once quota resets and MongoDB Atlas is set up:
```bash
# Test health
curl http://localhost:8001/api/

# Test caption generation
curl -X POST http://localhost:8001/api/generate-caption \
  -H "Content-Type: application/json" \
  -d '{"content_description": "sunset", "platform": "instagram", "tone": "inspiring"}'

# Test frontend
Open: https://smart-ai-agent-8.preview.emergentagent.com/
```

### 4. Deploy to PythonAnywhere 🚀
**Guide:** See "Deploying to PythonAnywhere" section in `/app/SETUP_GUIDE.md`

---

## 🎯 Features Your App Has

1. **🖼️ AI Hashtag Generator** - Upload image → Get 30 trending hashtags
2. **✍️ Caption Generator** - Platform-specific captions
3. **👤 Bio Generator** - Optimized profile bios
4. **💬 Comment Generator** - Context-aware comments
5. **🔄 Content Remixer** - Adapt content for all platforms
6. **🔥 Profile Roaster** - Brutally honest profile audit

All powered by **FREE** Google Gemini AI!

---

## 🆘 Common Issues

### "Quota exceeded" error:
- Wait 24 hours OR get new API key
- Check https://ai.google.dev/gemini-api/docs/rate-limits

### Backend won't start:
```bash
# Check logs
tail -n 50 /var/log/supervisor/backend.err.log

# Reinstall dependencies
cd /app/backend
pip install -r requirements.txt
sudo supervisorctl restart backend
```

### MongoDB connection error:
- Using localhost? Set up MongoDB Atlas instead
- Check connection string format
- Make sure password is correct (no `<>` brackets)

---

## 📚 Documentation

- **Full Setup Guide:** `/app/SETUP_GUIDE.md`
- **MongoDB Atlas Guide:** `/app/MONGODB_ATLAS_SETUP.md`
- **Gemini API Docs:** https://ai.google.dev/gemini-api/docs
- **PythonAnywhere Help:** https://help.pythonanywhere.com/

---

## 🎉 Summary

**What's Done:**
- ✅ Extracted your project
- ✅ Switched to FREE Gemini API (no more paid Emergent LLM)
- ✅ Added your API key
- ✅ Updated all code to use google-genai SDK
- ✅ Set up for local testing
- ✅ Created comprehensive guides

**What You Need To Do:**
1. ⏰ Wait for API quota reset (24h) OR get new key
2. ☁️ Set up MongoDB Atlas (5 minutes, free)
3. 🧪 Test locally
4. 🚀 Deploy to PythonAnywhere

**Time to Fully Working:** ~24 hours (mostly waiting for quota reset)

---

## 📞 Get Help

- Gemini API Issues: https://ai.google.dev/gemini-api/docs/rate-limits
- MongoDB Atlas: https://www.mongodb.com/docs/atlas/
- PythonAnywhere: https://help.pythonanywhere.com/

---

**Happy Building! 🚀**
