from aiogram import Bot, Dispatcher, executor
import requests
import json


bot = Bot(token='6011056539:AAFIH7wQOM-jsc4CXZdiU9POiEBl93gpWfc')
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'Привет')

@dp.message_handler(regexp='[0-9]+')
async def start(message):
    answer = requests.get(f'http://numbersapi.com/{message.text}?json')
    await bot.send_message(message.chat.id, json.loads(answer.text)['text'])

executor.start_polling(dp)