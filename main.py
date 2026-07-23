import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.handlers import router
from app.payments_handler import router as payment_router

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in environment variables")

async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher() 
    dp.include_router(router, payment_router)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot was closed!')


