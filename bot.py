import logging
import wikipedia
from aiogram import Dispatcher, executor, Bot, types

wikipedia.set_lang('uz')

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['help', 'start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom!\nInternet Bo`ylab Sayohat ruxsatiga ega robotman!\nPowered by @rmkvlly")


@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        response = wikipedia.summary(message.text)
        if len(response) > 4095:
            for x in range(0, len(response), 4095):
                await message.answer(response[x:x+4095])
        else:
            await message.answer(response)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
