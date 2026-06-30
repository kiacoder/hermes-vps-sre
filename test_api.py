# =============================================================================
# test_api.py — Hermes API & Telegram bot validator / عیب‌یاب اعتبارنامه‌ها
# =============================================================================
# Run this script on your VPS or local machine to test if your API keys 
# and Telegram tokens are active and correct before starting the gateway daemon.
# این اسکریپت درستی کلیدهای جمینای و توکن تلگرام شما را قبل از راه‌اندازی تست می‌کند.

import os
import sys
import urllib.request
import json

def test_gemini(api_key):
    print("🧠 Testing Gemini API key...")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": "Hello, confirm that you are online."}]}]
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode("utf-8"))
            text = res["candidates"][0]["content"]["parts"][0]["text"]
            print(f"✅ Gemini responds: {text.strip()}")
            return True
    except Exception as e:
        print(f"❌ Gemini API test failed: {e}")
        return False

def test_telegram(bot_token, user_id):
    print("📱 Testing Telegram Bot Token and User ID...")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    headers = {"Content-Type": "application/json"}
    data = {
        "chat_id": user_id,
        "text": "🧙‍♂️ Ron Weasley SRE Bot Connection Test: Connection Successful! Blimey, it works!"
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode("utf-8"))
            if res.get("ok"):
                print("✅ Telegram test message sent successfully! Check your Telegram chat!")
                return True
            else:
                print(f"❌ Telegram API returned error: {res}")
                return False
    except Exception as e:
        print(f"❌ Telegram Bot test failed: {e}")
        print("   Make sure you have started/messaged your bot in Telegram first before running this test!")
        return False

if __name__ == "__main__":
    # Attempt to load from .env file / تلاش برای خواندن فایل env.
    env_path = ".env"
    if os.path.exists(env_path):
        print(f"📂 Loading credentials from {env_path}...")
        with open(env_path, "r") as f:
            for line in f:
                if "=" in line and not line.strip().startswith("#"):
                    k, v = line.strip().split("=", 1)
                    os.environ[k] = v.strip("'\"")
                    
    gemini_key = os.getenv("GEMINI_API_KEY")
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    allowed_user = os.getenv("TELEGRAM_ALLOWED_USERS")
    
    if not gemini_key or not bot_token or not allowed_user:
        print("❌ Error: Missing credentials in .env file.")
        print("   Make sure you copy env.example to .env and fill in the values.")
        sys.exit(1)
        
    print("--------------------------------------------------")
    print("🚀 Starting Diagnostic Pre-Checks...")
    print("--------------------------------------------------")
    
    gemini_ok = test_gemini(gemini_key)
    tg_ok = test_telegram(bot_token, allowed_user)
    
    print("--------------------------------------------------")
    if gemini_ok and tg_ok:
        print("🎉 ALL PRE-CHECKS PASSED! You are ready to run setup.sh! 🚀")
    else:
        print("❌ Diagnostics failed. Please fix the credentials above and try again.")
        sys.exit(1)
