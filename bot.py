import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def to_upper(message: types.Message):
    await message.answer(message.text.upper())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
