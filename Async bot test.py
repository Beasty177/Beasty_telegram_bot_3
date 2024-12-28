import asyncio
import g4f
from telebot.async_telebot import AsyncTeleBot


token='8147781080:AAFvPegxmvmzd5Um1ouuuEpBtWfITR2bGHU'
bot = AsyncTeleBot(token)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)

# Провайдеры для ИИ
_providers = [
    # g4f.Provider.GizAI, #это было нормальное
    # g4f.Provider.TeachAnything #тоже норм
    # g4f.Provider.Free2GPT #норм
    # 4f.Provider.Flux,#картинка
    # g4f.Provider.DarkAI, #норм
    # g4f.Provider.DDG #норм
    g4f.Provider.Blackbox  # Норм
]





# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):


    await bot.reply_to(message, message.text)




asyncio.run(bot.polling())