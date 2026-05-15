import os
from dotenv import load_dotenv

load_dotenv()

# توكنات API
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# قاعدة البيانات
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///codebot.db")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# إعدادات البوت
MAX_CODE_LENGTH = int(os.getenv("MAX_CODE_LENGTH", 2000))
DAILY_LIMIT = int(os.getenv("DAILY_LIMIT", 50))
PREMIUM_DAILY_LIMIT = int(os.getenv("PREMIUM_DAILY_LIMIT", 500))

# إدارة البوت
ADMIN_IDS = [int(x.strip()) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]

# التحقق من وجود المفاتيح
if not TELEGRAM_TOKEN:
    raise ValueError("❌ الرجاء وضع TELEGRAM_BOT_TOKEN في ملف .env")
if not OPENAI_API_KEY:
    raise ValueError("❌ الرجاء وضع OPENAI_API_KEY في ملف .env")

print("✅ تم تحميل الإعدادات بنجاح")
