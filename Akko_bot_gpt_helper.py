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

user_id = None
chat_id = None
mess_id = None
bot_mess_id = None
chat_GPT_switch= False
text_main_menu_message='*Выбери нужный пункт*'
text_main_welcome_menu = 'Привет я *Влади* \- твой бот помощник в Акко\! \n *Выбери нужный пункт в меню* \n Буду рад помочь\!'
#Словарь для соотношения пользователей и их сообщений
notes_users = {}

mess_to_delete=[]


# создаем клавиатуры
main_menu = types.InlineKeyboardMarkup()
# добавляем на нее кнопки
button1 = types.InlineKeyboardButton(text="Узнать информацию", callback_data="button1")
button2 = types.InlineKeyboardButton(text="Отдел абсорбции Акко", callback_data="button2")
button3 = types.InlineKeyboardButton(text="Снять квартиру", callback_data="button3")
button4 = types.InlineKeyboardButton(text="Получить корзину абсорбции", callback_data="button4")
button5 = types.InlineKeyboardButton(text="Получить банковскую карту", callback_data="button5")
button6 = types.InlineKeyboardButton(text="Подключить телефон и интернет", callback_data="button6")
button7 = types.InlineKeyboardButton(text="Транспорт", callback_data="button7")
main_menu.add(button1,button2, button3, button4, button5,button6, button7, row_width=1)

#Клавиатура возврата в главное меню

go_back_main_menu = types.InlineKeyboardMarkup()
#button99= types.InlineKeyboardButton(text="Помощь", callback_data="button99")
button100 = types.InlineKeyboardButton(text="Назад в главное меню", callback_data="button100")
go_back_main_menu.add(button100,row_width=1)



#Очистка чата с ботом
#@bot.message_handler(commands=['clear'])
#def delete_all_messages(message):
#    chat_id = message.chat.id
#    message_id = message.message_id
#    messages_to_delete = []
#
#    messages = bot.get_chat_history(chat_id)
#    for msg in messages:
#        messages_to_delete.append(msg.message_id)
#
#    for msg_id in messages_to_delete:
#        try:
#            bot.delete_message(chat_id, msg_id)
#        except Exception as e:
#            print("", e)
#
#Конец очистки


#Функция для добавления id сообщений в список для удаления
def mes_clear_add_list (c_id,m_id):
    global notes_users
    m = []
    if c_id in notes_users:
        m=notes_users[c_id]
    m.append(m_id)
    notes_users[c_id] = m
    print(notes_users)

#Функция для удаления ненужных сообщений из словаря для конкретного пользователя id сообщений в список для удаления
def delete_mes_add_list (c_id):
    pass
    for i in notes_users[c_id]:
        try:
            bot.delete_message(c_id,i,3)

        except Exception as e:
             print(e)

    notes_users[c_id] = []  # Добавляем к ключу в виде id чата значения в виде списка из id сообщений бота
    #print(notes_users)



#Главное меню
@bot.message_handler(commands=["menu"])
def menu_call_mess(call):
    global  mess_id, chat_id, bot_mess_id, notes_users,chat_GPT_switch, mess_to_delete
    #выключаем GPT
    chat_GPT_switch=False #Выключаем чат GPT

    #  mes_clear_add_list(значение chat.id, значение message_id)
    mes_clear_add_list(call.chat.id, call.message_id)  # Функция для добавления id сообщений пользователя (команды типа /start) в список для удаления

    #Сообщение главного меню с кнопками
    bot_msg = bot.send_message(call.chat.id, f"{text_main_menu_message}", parse_mode='MarkdownV2',
                               reply_markup=main_menu)

    #  mes_clear_add_list(значение chat.id, значение message_id)
    mes_clear_add_list (bot_msg.chat.id,bot_msg.message_id) #Функция для добавления id сообщений в список для удаления





#
#
 #   #Информация о сообщениях бота в каждом чате - что бы потом удалить нужную (сделана через словарь и список id сообщений)
 #   bot_mess_id = bot_msg.message_id #Получаем id текущего сообщения бота
#  chat_id = bot_msg.chat.id #Получаем id текущего чата
 #   #mess_to_delete.append(bot_mess_id) #Записываем в список id сообщений бота для дальнейшего удаления если нужно
 #
 #
 #
 #   m=[]
#
 #   if chat_id in notes_users:
 #       m=notes_users[chat_id]
 #       #print('m ', m)
#
 #   m.append(bot_mess_id)
 #   notes_users[chat_id]=m
 #   print (notes_users)
#
#
#
#
#



#Меню и стартовое приветствие
@bot.message_handler(commands=["start"])
def main_hello(call):

    # Обьявляем переменные глобальными
    global mess_id, chat_id, notes_users, chat_GPT_switch

    chat_GPT_switch = False #Выключаем чат GPT

    #  mes_clear_add_list(значение chat.id, значение message_id)
    mes_clear_add_list(call.chat.id,call.message_id)  # Функция для добавления id сообщений пользователя (команды типа /start) в список для удаления

    # отправляем сообщение пользователю
    bot_msg= bot.send_message(call.chat.id, f'{text_main_welcome_menu}'
                                      ,parse_mode='MarkdownV2', reply_markup=main_menu)

    #  mes_clear_add_list(значение chat.id, значение message_id)
    mes_clear_add_list(bot_msg.chat.id, bot_msg.message_id)  # Функция для добавления id сообщений в список для удаления


    chat_id = call.chat.id
    #mess_id = call.message_id
    #bot_mess_id = bot_msg.message_id
    # Удаляем команду старт если захотим
    #bot.delete_message(chat_id, mess_id)

    # Информация о сообщениях бота в каждом чате - что бы потом удалить нужную (сделана через словарь и список id сообщений)
   # bot_mess_id = bot_msg.message_id  # Получаем id текущего сообщения бота
   # chat_id = bot_msg.chat.id  # Получаем id текущего чата
   # mess_to_delete.append(bot_mess_id)  # Записываем в список id сообщений бота для дальнейшего удаления если нужно
#
   # m = notes_users[chat_id] = []
   # m.append(bot_mess_id)
   # print(notes_users)

    #print (f'в главном меню \n chat_id {chat_id}\n mess_id {mess_id} '
    #       f'\n bot_mess_id {bot_mess_id}')


# функция запустится, когда пользователь нажимает на кнопку
@bot.callback_query_handler(func=lambda call: True)

def callback_inline(call):
    global mess_id, chat_id, bot_mess_id, notes_users, chat_GPT_switch, mess_to_delete

    #print(f'в главном меню \n chat_id {chat_id}\n mess_id {mess_id}')

    # bot.delete_message(chat_id=chat_id, message_id=mess_id, timeout=6)

    if call.message:
        if call.data == "button1":  #Переход в чат GPT
            chat_gpt(call)

        if call.data == "button2": #Отдел абсорбции Акко
            absorb_office(call)
            print(call.message.chat.id)
            #print(call)

            #print(call.message.json.chat.id)
            #bot.send_message(call.message.chat.id, "Вы нажали на вторую кнопку.")

        if call.data == "button3": #Аренда квартиры
            arenda_kvartir(call)
            #bot.send_message(call.message.chat.id, "Вы нажали на третью кнопку.")

        if call.data == "button4": #Корзина абсорбции
            korzina_absorb(call)
            #bot.send_message(call.message.chat.id, "Вы нажали на четвертую кнопку.")

        if call.data == "button5":
            #Переход на страницу банка
            #bot.send_message(call.message.chat.id, "Вы нажали на пятую кнопку.")
            bank_page(call)

        if call.data == "button6": #Телефон и интернет
            telefon_internet(call)
            #bot.send_message(call.message.chat.id, "Вы нажали на шестую кнопку.")

        if call.data == "button7": #Транспорт
            tranport_rules(call)
            #bot.send_message(call.message.chat.id, "Вы нажали на седьмую кнопку.")

        if call.data == "button100": #Возврат в главное меню
            main_bot_menu(call)
            chat_GPT_switch = False


#Главное меню
def main_bot_menu (call):
    global mess_id, chat_id, bot_mess_id, notes_users, text_main_menu_message, mess_to_delete
    print(call.message.chat.id)
    delete_mes_add_list (call.message.chat.id) #Функция удаления ненужных сообщений из чата меню




    bot_msg = bot.send_message(call.message.chat.id, f'{text_main_menu_message}', parse_mode='MarkdownV2',
                               reply_markup=main_menu)



#Отдел абсорбции Акко
def absorb_office(call):
    bot.send_message(call.message.chat.id,
                     f"Рассказ о отделе абсорбции, его функциях, руководстве, контакты, полезная информация, возможность построения маршрута в навигаторе\. "
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)



#Аренда квартиры
def arenda_kvartir(call):
    bot.send_message(call.message.chat.id,
                     f"В этом разделе можно разместить информацию о риелторах и их контактах, о порядке аренды крартир\. Рекомендации и на что обратить внимание при выборе\. Примерные цены\. "
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)


#Корзина абсорбции
def korzina_absorb(call):
    bot.send_message(call.message.chat.id,
                     f"Как получить корзину абсорбции, калькулятор расчета размера корзины, правила предоставления и тп\. "
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)




#Страница банка
def bank_page (call):

    #try:
    #    bot.delete_message(chat_id, bot_mess_id) #Удаляем сообщение с главным меню
    #except Exception as e:
    #    print (e)

    bot.send_message(call.message.chat.id,f"В этом разделе может быть рассказано о времени работы банка, как записаться на прием, адрес, основные принципы и отличия банковской системы, что такое чековая книжка и тп \n"
                                          f"Так же тут можно быстро построить маршрут до банка, нажав на ссылку \n *[Построить маршрут до офиса Дисконт банка в Акко](https://maps.app.goo.gl/HPrqV1JQrk8SrWDMA)*"
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)



#Телефон и интернет

def telefon_internet(call):
    bot.send_message(call.message.chat.id,
                     f"Где купить сим карту, какие есть выгодные тарифы на мобильную связь, как подключить домашний проводной интернет\. "
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)





#Транспорт
def tranport_rules(call):
    bot.send_message(call.message.chat.id,
                     f"Виды транспорта, как оплачивать проезд и его стоимость\. Правила аренды и покупки автомобилей\."
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)


#Переходим в чат GPT или отвечаем простым сообщением если выключен

def chat_gpt (call): #Эта функция для разрешения чата GPT
    global chat_GPT_switch

    #Отправка фото тест
    photo = open('image_1.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)


    bot.send_message(call.message.chat.id, f"Напиши чем я могу быть полезен, \n"
                                           f"я могу рассказать про историю Акко, \n "
                                           f"посоветовать что приготовить на ужин, помочь составить резюме на иврите или просто поболтать \n"
                                           f"Просто отправь свой запрос в сообщении", parse_mode='MarkdownV2',
                     reply_markup=go_back_main_menu)

    chat_GPT_switch = True #Подключаем чат GPT


# Блок чата GPT

@bot.message_handler(func=lambda message: True)
def response_gpt_message (call):
    global user_id, mess_id, chat_id, bot_mess_id, notes_users
    #global chat_GPT_switch
    mes = call.text
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
        bot.send_message(call.chat.id,f'{resp_gpt} \n\n'
                                         f'Для главного меню нажмите /menu',)
        print (resp_gpt)
        print (response)
    else:
        bot_msg = bot.send_message(call.chat.id, f'Нажми /start что бы начать \nНажми /menu для перехода в основное меню '
                                   , parse_mode='MarkdownV2')
        #bot_msg = bot.send_message(call.chat.id, f'{text_main_welcome_menu}'
        #                           , parse_mode='MarkdownV2', reply_markup=main_menu)

        user_id=call.from_user.first_name
        chat_id = call.chat.id
        mess_id = call.message_id
        bot_mess_id = bot_msg.message_id

        #print(mess_id)
        #print(user_id)
        #print(call)



bot.polling(none_stop=True)



