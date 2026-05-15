import openai
import re
from typing import Dict, Optional
from tenacity import retry, stop_after_attempt, wait_exponential
from config import OPENAI_API_KEY, MAX_CODE_LENGTH
from loguru import logger

client = openai.OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """أنت مساعد برمجي خبير. متخصص فقط في كتابة الأكواد البرمجية.

صيغة الرد المطلوبة:
📍 **ملخص:** شرح سريع
📝 **الكود:**
```لغة البرمجة
الكود هنا
