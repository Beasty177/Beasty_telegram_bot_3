import telebot
#from telebot import formatting
from random import choice
from telebot import types

token='8147781080:AAFvPegxmvmzd5Um1ouuuEpBtWfITR2bGHU'
bot = telebot.TeleBot(token)

chat_id = None
mess_id = None
bot_mess_id = None

def bank_page (call):

    keyboard = types.InlineKeyboardMarkup()
    button100 = types.InlineKeyboardButton(text="Назад в главное меню", callback_data="button100")
    keyboard.add(button100)
    bot.delete_message(chat_id, bot_mess_id)


    bot.send_message(call.message.chat.id,f"*[\nКак дойти до Дисконт банка в Акко](https://maps.app.goo.gl/HPrqV1JQrk8SrWDMA)*"
                     , parse_mode='MarkdownV2', reply_markup=keyboard)

    print(f'вторая ступень \n chat_id {chat_id}\n mess_id {mess_id}')






@bot.message_handler(commands=["start"])
def main_hello(call):
    global mess_id, chat_id, bot_mess_id
    # создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup()

    # добавляем на нее две кнопки
    button1 = types.InlineKeyboardButton(text="Узнать информацию", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Первые необходимые шаги", callback_data="button2")
    button3 = types.InlineKeyboardButton(text="Снять квартиру", callback_data="button3")
    button4 = types.InlineKeyboardButton(text="Получить корзину", callback_data="button4")
    button5 = types.InlineKeyboardButton(text="Получить банковскую карту", callback_data="button5")
    #keyboard.add(button1,button2, button3, button4, button5)
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)
    keyboard.add(button5)

    # отправляем сообщение пользователю
    bot_msg= bot.send_message(call.chat.id, f"Привет я *Влади* \- твой бот помощник в Акко\!"
                                      f"\n"
                                      f"*Выбери нужный пункт в меню* \n"
                                      f"Буду рад помочь\!"
                                      ,parse_mode='MarkdownV2', reply_markup=keyboard)
    chat_id = call.chat.id
    mess_id = call.message_id
    bot_mess_id = bot_msg.message_id
# Удаляем команду старт если захотим
    bot.delete_message(chat_id, mess_id)


    print (f'в главном меню \n chat_id {chat_id}\n mess_id {mess_id} '
           f'\n bot_mess_id {bot_mess_id}')




# функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call: True)

def callback_inline(call):


    print(f'в главном меню \n chat_id {chat_id}\n mess_id {mess_id}')

    # bot.delete_message(chat_id=chat_id, message_id=mess_id, timeout=6)

    if call.message:
        if call.data == "button1":

            bot.send_message(call.message.chat.id, "Вы нажали на первую кнопку.")
        if call.data == "button2":
            bot.send_message(call.message.chat.id, "Вы нажали на вторую кнопку.")

        if call.data == "button3":
            bot.send_message(call.message.chat.id, "Вы нажали на третью кнопку.")

        if call.data == "button4":
            bot.send_message(call.message.chat.id, "Вы нажали на четвертую кнопку.")

        if call.data == "button5":

            #bot.send_message(call.message.chat.id, "Вы нажали на пятую кнопку.")

            bank_page(call)

        if call.data == "button100":
            bot.send_message(call.message.chat.id, "На главное меню /start")






bot.polling(none_stop=True)



