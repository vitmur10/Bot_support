import aiogram
import Config

bot = aiogram.Bot(token=Config.TOKEN_BOT)

dp = aiogram.Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: aiogram.types.Message):
    await message.reply('Hello')

@dp.message_handler(content_types=['text'])
async def a(message: aiogram.types.Message):
    await message.reply('1')

if __name__ =='__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)