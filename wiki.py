import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from wiki import wiki

dp = Dispatcher()


TOKEN = "7546718242:AAGz5LYY-eYIae761VQd4UUeL-PbNtjJE1k"


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bot szga malumot topishda yordam beradi!\n Qanaqa ma'lumot kerak: "
    await message.answer(text)

@dp.message(F.text)
async def wiki_handler(message: Message):
    text = message.text
    malumot = wiki(text)
    await message.answer(malumot)


async def main():
    await dp.start_polling(bot)


if name == "main":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())import wikipedia

def wiki(text):
    wikipedia.set_lang("uz")
    result = wikipedia.summary(text)
    return result\