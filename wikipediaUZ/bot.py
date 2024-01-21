import sys
import wikipedia
import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

wikipedia.set_lang('uz')

dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message):
    """
    This handler will be called when user sends '/start' or '/help/' command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@dp.message()
async def sendWiki(message: types.Message):
    try: 
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

async def main():
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
