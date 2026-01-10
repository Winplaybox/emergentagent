# MongoDB Atlas Setup Guide (FREE) 🍃

## Why MongoDB Atlas?

PythonAnywhere doesn't support MongoDB locally, so we need a cloud database. MongoDB Atlas offers a **100% FREE tier** that's perfect for your project!

---

## Step-by-Step Setup (5 minutes)

### 1. Create Account
1. Go to: **https://www.mongodb.com/cloud/atlas/register**
2. Sign up with email or Google account
3. Choose **FREE** tier (M0 Sandbox)

### 2. Create a Cluster
1. After login, click **"Build a Database"**
2. Choose **"M0 FREE"** tier
3. Select a region close to you (e.g., AWS us-east-1)
4. Name your cluster: `hashtaghero-cluster`
5. Click **"Create Deployment"**

### 3. Create Database User
1. You'll see "Security Quickstart"
2. Create a username: `hashtaghero_user`
3. Click "Autogenerate Secure Password" - **SAVE THIS PASSWORD!**
4. Click "Create User"

### 4. Allow Network Access
1. On the same page, you'll see "Where would you like to connect from?"
2. Choose "My Local Environment"
3. Click "Add My Current IP Address"
4. **IMPORTANT**: Also add `0.0.0.0/0` (allow from anywhere) for PythonAnywhere
5. Click "Finish and Close"

### 5. Get Connection String
1. Click "Database" in left sidebar
2. Click "Connect" button on your cluster
3. Choose "Drivers"
4. Select: Python, Version 3.12 or later
5. Copy the connection string - looks like:
   ```
   mongodb+srv://hashtaghero_user:<password>@hashtaghero-cluster.xxxxx.mongodb.net/
   ```
6. **Replace `<password>` with your actual password**

---

## Update Your Backend

### Edit `/app/backend/.env`:

Replace this line:
```
MONGO_URL=mongodb://localhost:27017/
```

With your Atlas connection string:
```
MONGO_URL=mongodb+srv://hashtaghero_user:YOUR_PASSWORD_HERE@hashtaghero-cluster.xxxxx.mongodb.net/
```

**Example:**
```
MONGO_URL=mongodb+srv://hashtaghero_user:MySecurePass123@hashtaghero-cluster.abc123.mongodb.net/
```

### Restart Backend:
```bash
sudo supervisorctl restart backend
```

---

## Verify Connection

Test if MongoDB Atlas is working:

```bash
curl http://localhost:8001/api/status
```

If successful, you should see status checks data!

---

## 📊 Free Tier Limits

Your free MongoDB Atlas cluster includes:
- ✅ 512 MB storage (plenty for thousands of users)
- ✅ Shared RAM
- ✅ No credit card required
- ✅ Never expires
- ✅ Perfect for development and small projects

---

## 🔒 Security Tips

1. **Never commit .env files to GitHub** (already in .gitignore)
2. **Use strong passwords** for database users
3. **Rotate API keys** periodically
4. **For production**: Restrict IP addresses (remove 0.0.0.0/0)

---

## 🐛 Troubleshooting

### "Authentication failed" error:
- Check username/password in connection string
- Make sure you replaced `<password>` with actual password
- No special characters? If yes, URL-encode them

### "Connection timeout" error:
- Check Network Access: is 0.0.0.0/0 allowed?
- Check your internet connection

### "Database not found" error:
- MongoDB will create database automatically on first write
- No action needed!

---

## 🎉 That's It!

Your HashtagHero app is now connected to a cloud database that works everywhere - locally, on PythonAnywhere, or anywhere else!

**Connection String Format:**
```
mongodb+srv://<username>:<password>@<cluster-url>/<database-name>?retryWrites=true&w=majority
```

**Your Settings:**
```
MONGO_URL=mongodb+srv://hashtaghero_user:YOUR_PASSWORD@hashtaghero-cluster.xxxxx.mongodb.net/
DB_NAME=hashtaghero
```

---

Need help? Check MongoDB Atlas docs: https://www.mongodb.com/docs/atlas/getting-started/
