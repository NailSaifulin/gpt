import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
openai.api_key = os.getenv("OPENAI_API_KEY")
dp = Dispatcher(bot)


@dp.message_handler()
async def on_message(message: types.Message):
    response = await get_response(message.text)
    await message.answer(response)


async def get_response(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

executor.start_polling(dp, skip_updates=True)

