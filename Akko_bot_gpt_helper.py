import telebot
#from telebot import formatting
from random import choice
from telebot import types
import g4f
#import provider
from g4f.client import Client
import telebot


token='7976548226:AAFXV7cqzXWaWPfJjF9_Xi_Aog0oyXMIB2U'
bot = telebot.TeleBot(token)

chat_id = None
mess_id = None
bot_mess_id = None
chat_GPT_switch= False
text_main_menu_message='*Выбери нужный пункт*'

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


@bot.message_handler(commands=["menu"])
def menu_call_mess(call):
    global mess_id, chat_id, bot_mess_id, notes_users,chat_GPT_switch, text_main_menu_message
    chat_GPT_switch=False

    bot_msg = bot.send_message(call.chat.id, f"{text_main_menu_message}", parse_mode='MarkdownV2',
                               reply_markup=main_menu)
    bot_mess_id = bot_msg.message_id
    chat_id = bot_msg.chat.id


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


# функция запустится, когда пользователь нажимает на кнопку
@bot.callback_query_handler(func=lambda call: True)

def callback_inline(call):
    global bot_mess_id, chat_id, chat_GPT_switch
    #Сделал переменную для функции кнопок можно так можно так
    btn_funk= call.data


    print(f'в главном меню \n chat_id {chat_id}\n mess_id {mess_id}')

    # bot.delete_message(chat_id=chat_id, message_id=mess_id, timeout=6)

    if call.message:
        if call.data == "button1":  #Переход в чат GPT
            chat_gpt(call)

        if call.data == "button2":
            bot.send_message(call.message.chat.id, "Вы нажали на вторую кнопку.")

        if call.data == "button3":
            bot.send_message(call.message.chat.id, "Вы нажали на третью кнопку.")

        if call.data == "button4":
            bot.send_message(call.message.chat.id, "Вы нажали на четвертую кнопку.")

        if call.data == "button5":
            #Переход на страницу банка
            #bot.send_message(call.message.chat.id, "Вы нажали на пятую кнопку.")
            bank_page(call)

        if btn_funk == "button100":
            main_bot_menu(call)
            chat_GPT_switch = False



def main_bot_menu (call):
    global mess_id, chat_id, bot_mess_id, notes_users, text_main_menu_message

    bot_msg = bot.send_message(call.message.chat.id, f'{text_main_menu_message}', parse_mode='MarkdownV2',
                               reply_markup=main_menu)
    bot_mess_id = bot_msg.message_id
    chat_id = bot_msg.chat.id



#Страница банка
def bank_page (call):

    try:
        bot.delete_message(chat_id, bot_mess_id) #Удаляем сообщение с главным меню
    except Exception as e:
        print (e)

    bot.send_message(call.message.chat.id,f"*[\nКак дойти до Дисконт банка в Акко](https://maps.app.goo.gl/HPrqV1JQrk8SrWDMA)*"
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)



def chat_gpt (call): #Эта функция для разрешения чата GPT
    global chat_GPT_switch
    bot.send_message(call.message.chat.id, f"Напиши чем я могу быть полезен, \n"
                                           f"я могу рассказать про историю Акко, \n "
                                           f"посоветовать что приготовить на ужин, помочь составить резюме на иврите или просто поболтать \n"
                                           f"Просто отправь свой запрос в сообщении", parse_mode='MarkdownV2',
                     reply_markup=go_back_main_menu)

    chat_GPT_switch = True




# Блок чата GPT

@bot.message_handler(func=lambda message: True)
def response_gpt_message (message):
    #global chat_GPT_switch
    mes = message.text
    if chat_GPT_switch==True:

        print(mes)
        client = Client()
        response = client.chat.completions.create(
            model=g4f.models.default,
            messages=[{"role": "user", "content": mes}],
            provider= g4f.Provider.Blackbox
            # Add any other necessary parameters
        )
        resp_gpt = (response.choices[0].message.content)
        bot.send_message(message.chat.id,f'{resp_gpt} \n\n'
                                         f'Для главного меню нажмите /menu',)
        print (resp_gpt)
        print (response)
    else:
        bot.send_message(message.chat.id,'oops')









bot.polling(none_stop=True)



