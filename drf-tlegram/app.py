import os
import logging
import requests
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(f"""
        Hi @{username}.
        Commands:
            1. /artist
            2. /albom
            3. /songs
    """)


@dp.message_handler(commands=['artist',])
async def send_artists(message: types.Message):
    artists_data = requests.get('http://localhost:8000/api/artists-tele').json()

    for artist in artists_data:
        await message.reply(f"""
            {artist['image']}
            First Name: {artist['first_name']}
            Last Name: {artist['last_name']}
            Nick: {artist['nick_name']}
        """)

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)