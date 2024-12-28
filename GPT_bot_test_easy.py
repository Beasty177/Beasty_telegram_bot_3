import g4f
#import provider
from g4f.client import Client

import telebot
from telebot import types
token='8147781080:AAFvPegxmvmzd5Um1ouuuEpBtWfITR2bGHU'
bot=telebot.TeleBot(token,)

#_providers = [
#    # g4f.Provider.GizAI, #это было нормальное
#    # g4f.Provider.TeachAnything #тоже норм
#    # g4f.Provider.Free2GPT #норм
#    # 4f.Provider.Flux,#картинка
#    # g4f.Provider.DarkAI, #норм
#    # g4f.Provider.DDG #норм
#    g4f.Provider.Blackbox  # Норм
#]

@bot.message_handler(func=lambda message: True)
def response_gpt_message (message):
    mes = message.text
    print(mes)
    client = Client()
    response = client.chat.completions.create(
        model=g4f.models.default,
        messages=[{"role": "user", "content": mes}],
        provider= g4f.Provider.Blackbox
        # Add any other necessary parameters
    )
    resp_gpt = (response.choices[0].message.content)
    bot.send_message(message.chat.id,resp_gpt)
    print (resp_gpt)
    print (response)


bot.infinity_polling()


