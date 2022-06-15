import aiogram
import Config
import random
bot = aiogram.Bot(token=Config.TOKEN_BOT)

dp = aiogram.Dispatcher(bot)

a = ['Відпочинь', 'Все буде добре']
b = ['У тебе дуже гарна посмішка', 'Не думай про погане', 'Все буде добре']
c = ['У тебе все вийде', 'Все буде добре']


@dp.message_handler(commands=['start'])
async def start(message: aiogram.types.Message):
    await message.reply('Привіт')


@dp.message_handler(content_types=['text'])
async def support(message: aiogram.types.Message):
    x = {

        'Я втомився': a[random.randrange(0, len(a))],
        'Мені сумно': b[random.randrange(0, len(b))],
        'Я більше не можу': [random.randrange(0, len(c))],
        'Я втомилася': a[random.randrange(0, len(a))]
    }
    for key in x:
        if message.text == key:
            await message.answer(x[key])



if __name__ =='__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)