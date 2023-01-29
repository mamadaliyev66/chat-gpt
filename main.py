import os
from aiogram import Bot, Dispatcher, types,executor
import openai


bot = Bot(token='5729278564:AAGdikcTbpQXhsumuMLiuNXgf4Bagcn5lBE')
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("Hello! I'm a Telegram bot powered by Chat-GPT. How can I help you today?")


async def generate_response(prompt):
    api_key = "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"
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        api_key=api_key
    )

    message = completions.choices[0].text
    return message.strip()

@dp.message_handler()
async def echo_message(message: types.Message):
    prompt = (f"{message.text}")
    response = await generate_response(prompt)
    await message.reply(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
