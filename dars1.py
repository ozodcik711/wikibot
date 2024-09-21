import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "7015438221:AAGQYE-XxJwfNnOr_2fxGPctceAPLvhHDYQ"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.first_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)

# @dp.message(F.audio)
# async def audio(message:Message):
#     audio = message.audio
    
#     await message.answer("Xabar yuborildi")
#     await message.answer_audio(audio.file_id)


#document,video, photo, audio, location, animation,video_note
#contact, game, dice, voice,media_group, poll, sticker


async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from viki import viki

dp = Dispatcher()

TOKEN = "7232392821:AAHDV9rsZLOVowiVxREB7MiiLiJWk-ElO7g"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, sizga nima haqida malumot kerak ?"

    await message.answer(text)
    


@dp.message(F.text)
async def wiki_handler(massage:Message):
    text = massage.text

    malumot = viki(text)
    await massage.answer(malumot)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
