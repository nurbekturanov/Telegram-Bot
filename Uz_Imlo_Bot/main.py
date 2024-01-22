import logging
import asyncio
from checkWord import checkWord

import os
from dotenv import load_dotenv


from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types.message import Message
 
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Uz Imlo botiga xush kelibisz!")

@dp.message(Command('help'))
async def help_user(message: Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring.")

@dp.message()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✔ {word.capitalize()}"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f"✔ {text.capitalize()}\n"
    await message.answer(response)



async def main():
    bot = Bot(API_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())