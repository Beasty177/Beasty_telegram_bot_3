import telebot
#from telebot import formatting
from random import choice
from telebot import types

token='8147781080:AAFvPegxmvmzd5Um1ouuuEpBtWfITR2bGHU'
bot = telebot.TeleBot(token)

chat_id = None
mess_id = None
bot_mess_id = None

# создаем клавиатуры
main_menu = types.InlineKeyboardMarkup()
# добавляем на нее кнопки
button1 = types.InlineKeyboardButton(text="Узнать информацию", callback_data="button1")
button2 = types.InlineKeyboardButton(text="Первые необходимые шаги", callback_data="button2")
button3 = types.InlineKeyboardButton(text="Снять квартиру", callback_data="button3")
button4 = types.InlineKeyboardButton(text="Получить корзину", callback_data="button4")
button5 = types.InlineKeyboardButton(text="Получить банковскую карту", callback_data="button5")
main_menu.add(button1,button2, button3, button4, button5,row_width=1)


#Клавиатура возврата в главное меню

go_back_main_menu = types.InlineKeyboardMarkup()
button99= types.InlineKeyboardButton(text="Помощь", callback_data="button99")
button100 = types.InlineKeyboardButton(text="Назад в главное меню", callback_data="button100")
go_back_main_menu.add(button100,button99,row_width=1)






#Словарь для записи пользователей и доп информации к ним
notes_users = {}


#Запоминалка на всякий случай
#@bot.message_handler(commands=['remind'])
#def remind(message):
#    user_id = message.chat.id
#    if user_id not in notes_users:
#        bot.send_message(user_id, "Вы мне еще не писали.")
#    else:
#        bot.send_message(user_id, notes_users[user_id])
#
#@bot.message_handler(content_types=['text'])
#def remember(message):
#    user_id = message.chat.id
#    notes_users[user_id] = message.text
#    bot.send_message(user_id, "Я запомнил")
#Конец запоминалки


@bot.message_handler(commands=["start"])

def main_hello(call):

    # Обьявляем переменные глобальными
    global mess_id, chat_id, bot_mess_id, notes_users

    #Запоминаем первый chat_id для того что бы вернуться к главному меню
    user_id = call.chat.id
    notes_users [user_id]= call

    # отправляем сообщение пользователю
    bot_msg= bot.send_message(call.chat.id, f"Привет я *Влади* \- твой бот помощник в Акко\!"
                                      f"\n"
                                      f"*Выбери нужный пункт в меню* \n"
                                      f"Буду рад помочь\!"
                                      ,parse_mode='MarkdownV2', reply_markup=main_menu)


    chat_id = call.chat.id
    mess_id = call.message_id
    bot_mess_id = bot_msg.message_id
    # Удаляем команду старт если захотим
    #bot.delete_message(chat_id, mess_id)

    print (f'в главном меню \n chat_id {chat_id}\n mess_id {mess_id} '
           f'\n bot_mess_id {bot_mess_id}')




# функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call: True)

def callback_inline(call):
    global bot_mess_id, chat_id
    #Сделал переменную для функции кнопок можно так можно так
    btn_funk= call.data


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

        if btn_funk == "button100":
            bot_msg=bot.send_message(call.message.chat.id, "*Выбери нужный пункт в меню*", parse_mode='MarkdownV2', reply_markup=main_menu )
            bot_mess_id = bot_msg.message_id
            chat_id= bot_msg.chat.id





def bank_page (call):

    bot.delete_message(chat_id, bot_mess_id) #Удаляем сообщение с главным меню

    bot.send_message(call.message.chat.id,f"*[\nКак дойти до Дисконт банка в Акко](https://maps.app.goo.gl/HPrqV1JQrk8SrWDMA)*"
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)








bot.polling(none_stop=True)



