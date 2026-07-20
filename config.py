import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

OPENAI_API_TOKEN = os.getenv("OPENAI_API_TOKEN")

if not OPENAI_API_TOKEN:
    raise ValueError('OPENAI_API_TOKEN is not found!')

client = AsyncOpenAI(
    api_key=OPENAI_API_TOKEN, 
    base_url="https://openrouter.ai/api/v1", 
    timeout=60,
)