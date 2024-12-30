from telebot import types
import g4f
from g4f.client import Client
import telebot

token='7976548226:AAFXV7cqzXWaWPfJjF9_Xi_Aog0oyXMIB2U'
bot = telebot.TeleBot(token)

user_id = None
chat_id = None
mess_id = None
bot_mess_id = None
chat_GPT_switch= False
text_main_menu_message='*Выбери нужный пункт в меню* \n Что бы узнать о преимуществах телеграмм бота \- нажми /info'
text_main_welcome_menu = 'Привет я *Влади* \- твой бот помощник в *Акко*\! \n *Выбери нужный пункт в меню* \n Буду рад помочь\!\n Что бы узнать о преимуществах телеграмм бота \- нажми /info'
#Преимущества чат бота перед приложениями еулсе для поста
bot_goods='🌟 **Преимущества чат-ботов в Telegram по сравнению с приложениями** 🌟\n\nВ современном мире, где технологии развиваются с невероятной скоростью, чат-боты становятся все более популярными. Особенно это касается платформы Telegram. Давайте рассмотрим, почему чат-боты в Telegram могут быть более выгодными по сравнению с традиционными приложениями.\n\n1. **Доступность и простота использования** 📱\n   - Чат-боты в Telegram доступны на всех устройствах, где установлено приложение. Вам не нужно скачивать и устанавливать отдельное приложение, достаточно просто открыть Telegram и начать общение с ботом.\n\n2. **Экономия времени и ресурсов** ⏳\n   - Разработка чат-бота зачастую требует меньше времени и финансовых вложений, чем создание полноценного мобильного приложения. Это позволяет быстро запустить проект и начать взаимодействие с пользователями.\n\n3. **Обновления без проблем** 🔄\n   - В отличие от приложений, которые требуют обновлений через магазины, изменения в чат-ботах можно вносить мгновенно. Пользователи всегда получают актуальную версию без необходимости скачивания обновлений.\n\n4. **Интуитивный интерфейс** 💬\n   - Чат-боты предлагают простой и понятный интерфейс, который не требует обучения. Пользователи могут легко взаимодействовать с ботом, используя привычные команды и сообщения.\n\n5. **Интеграция с другими сервисами** 🔗\n   - Чат-боты могут легко интегрироваться с различными API и сервисами, что позволяет расширять их функционал и улучшать пользовательский опыт.\n\n6. **Высокая степень вовлеченности** 📈\n   - Пользователи чаще взаимодействуют с чат-ботами, так как они могут получать мгновенные ответы на свои вопросы и выполнять задачи в реальном времени. Это повышает уровень вовлеченности и удовлетворенности.\n\n7. **Персонализация** 🎯\n   - Чат-боты могут адаптироваться под предпочтения пользователей, предлагая персонализированные рекомендации и контент, что делает взаимодействие более приятным и эффективным.\n\n8. **Безопасность и конфиденциальность** 🔒\n   - Telegram предлагает высокий уровень безопасности и шифрования, что делает общение с чат-ботами более защищенным по сравнению с некоторыми приложениями.\n\nВ заключение, чат-боты в Telegram представляют собой удобное и эффективное решение для бизнеса и пользователей. Они обеспечивают простоту, доступность и высокую степень взаимодействия, что делает их отличной альтернативой традиционным приложениям. 🚀\n\nПопробуйте использовать чат-бота в Telegram и убедитесь в его преимуществах сами!'
#Словарь для хранения id сообщений для удаления
notes_users = {}

# создаем клавиатуры и разные меню
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
    try:
        for i in notes_users[c_id]:
            bot.delete_message(c_id,i,3)

    except Exception as e:
         print(e)

    notes_users[c_id] = []  # Добавляем к ключу в виде id чата значения в виде списка из id сообщений бота
    #print(notes_users)


#Текст о преимуществах телеграм ботов вызывается командой /info
@bot.message_handler(commands=["info"])
def info_goods(call):
    global  chat_GPT_switch
    #выключаем GPT
    chat_GPT_switch=False #Выключаем чат GPT

    #Сообщение только текст главного меню с кнопками
    bot.send_message(call.chat.id, f"{bot_goods}  \n\n Для главного меню нажмите /start")


#Главное меню вызывается командой /menu
@bot.message_handler(commands=["menu"])
def menu_call_mess(call):
    global  chat_GPT_switch
    #выключаем GPT
    chat_GPT_switch=False #Выключаем чат GPT

    #  mes_clear_add_list(значение chat.id, значение message_id)
    mes_clear_add_list(call.chat.id, call.message_id)  # Функция для добавления id сообщений пользователя (команды типа /start) в список для удаления

    ##Сообщение только текст главного меню с кнопками
    #bot_msg = bot.send_message(call.chat.id, f"{text_main_menu_message}", parse_mode='MarkdownV2',
    #                           reply_markup=main_menu)

    # Отправка фото с тестом
    photo = open('akko_im.jpg', 'rb')

    bot_msg =bot.send_photo(call.chat.id, photo,
                   f"{text_main_menu_message}", parse_mode='MarkdownV2', reply_markup=main_menu)

    #  функция для запоминания id сообщений mes_clear_add_list(значение chat.id, значение message_id)
    mes_clear_add_list (bot_msg.chat.id,bot_msg.message_id) #Функция для добавления id сообщений в список для удаления


#Меню и стартовое приветствие вызывается командой /start
@bot.message_handler(commands=["start"])
def main_hello(call):

    # Обьявляем переменные глобальными
    global  chat_GPT_switch

    chat_GPT_switch = False #Выключаем чат GPT

    #  функция запоминания id сообщений mes_clear_add_list(значение chat.id, значение message_id)
    mes_clear_add_list(call.chat.id,call.message_id)  # Функция для добавления id сообщений пользователя (команды типа /start) в список для удаления

    ## отправляем сообщение пользователю
    #bot_msg= bot.send_message(call.chat.id, f'{text_main_welcome_menu}',parse_mode='MarkdownV2', reply_markup=main_menu)

    # Отправка фото с текстом
    photo = open('image_1.png', 'rb')

    bot_msg = bot.send_photo(call.chat.id, photo, f'{text_main_welcome_menu}', parse_mode='MarkdownV2',
                             reply_markup=main_menu)


    #  функция запоминания id сообщений которые послал бот mes_clear_add_list(значение chat.id, значение message_id)
    mes_clear_add_list(bot_msg.chat.id, bot_msg.message_id)  # Функция для добавления id сообщений в список для удаления



# Реакция на нажатия кнопок в боте, когда пользователь нажимает на кнопку
@bot.callback_query_handler(func=lambda call: True)

def callback_inline(call):
    global chat_GPT_switch


    if call.message:
        if call.data == "button1":  #Переход в чат GPT

            chat_gpt(call)

        if call.data == "button2": #Отдел абсорбции Акко

            absorb_office(call)
            #print(call.message.chat.id) #Это id чата для кнопок
            #bot.send_message(call.message.chat.id, "Вы нажали на вторую кнопку.")

        if call.data == "button3": #Аренда квартиры

            arenda_kvartir(call)
            #bot.send_message(call.message.chat.id, "Вы нажали на третью кнопку.")

        if call.data == "button4": #Корзина абсорбции

            korzina_absorb(call)
            #bot.send_message(call.message.chat.id, "Вы нажали на четвертую кнопку.")

        if call.data == "button5": #Переход на страницу банка

            bank_page(call)
            #bot.send_message(call.message.chat.id, "Вы нажали на пятую кнопку.")

        if call.data == "button6": #Телефон и интернет

            telefon_internet(call)
            #bot.send_message(call.message.chat.id, "Вы нажали на шестую кнопку.")

        if call.data == "button7": #Транспорт

            tranport_rules(call)
            #bot.send_message(call.message.chat.id, "Вы нажали на седьмую кнопку.")

        if call.data == "button100": #Возврат в главное меню

            main_bot_menu(call) #Нажатие кнопки из другого меню для возврата в главное меню
            chat_GPT_switch = False #Выключаем GPT


#Главное меню вызывается кнопкой на клавиатуре из сообщений
def main_bot_menu (call):

    #print(call.message.chat.id)
    delete_mes_add_list (call.message.chat.id) #Функция удаления ненужных сообщений из чата меню передает значение id чата

    #Сообщение главного меню с кнопками

    #Сообщение только текст
    #bot_msg = bot.send_message(call.message.chat.id, f'{text_main_menu_message}', parse_mode='MarkdownV2',
    #                           reply_markup=main_menu)

    # Отправка фото с текстом
    photo = open('image_1.png', 'rb')

    bot_msg =bot.send_photo(call.message.chat.id, photo,f'{text_main_menu_message}', parse_mode='MarkdownV2',
                               reply_markup=main_menu)


    #  функция запоминания id сообщений которые послал бот mes_clear_add_list(значение chat.id, значение message_id)
    mes_clear_add_list(bot_msg.chat.id, bot_msg.message_id)  # Функция для добавления id сообщений в список для удаления


#Отдел абсорбции Акко
def absorb_office(call):
    #bot.send_message(call.message.chat.id,
    #                 f"Рассказ о отделе абсорбции, его функциях, руководстве, контакты, полезная информация, возможность построения маршрута в навигаторе\. "
    #                 , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)
#
    # Отправка фото с текстом
    photo = open('akko_mun.jpg', 'rb')

    bot.send_photo(call.message.chat.id, photo,
                   f"Рассказ о отделе абсорбции, его функциях, руководстве, контакты, полезная информация, возможность построения маршрута в навигаторе\. "
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)


#Аренда квартиры
def arenda_kvartir(call):
    bot.send_message(call.message.chat.id,
                     f"В этом разделе можно разместить информацию о риелторах и их контактах, о порядке аренды крартир\. Рекомендации и на что обратить внимание при выборе\. Примерные цены\. "
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)


#Корзина абсорбции
def korzina_absorb(call):
    #bot.send_message(call.message.chat.id,
    #                 f"Как получить корзину абсорбции, калькулятор расчета размера корзины, правила предоставления и тп\. "
    #                 , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)

    #Отправка фото с тестом
    photo = open('akko_im.jpg', 'rb')

    bot.send_photo(call.message.chat.id, photo, f"Как получить корзину абсорбции, калькулятор расчета размера корзины, правила предоставления и тп\. "
                     , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)

#Страница банка
def bank_page (call):
    #Отправка только сообщения без фото
    #bot.send_message(call.message.chat.id,f"В этом разделе может быть рассказано о времени работы банка, как записаться на прием, адрес, основные принципы и отличия банковской системы, что такое чековая книжка и тп \n"
    #                                      f"Так же тут можно быстро построить маршрут до банка, нажав на ссылку \n *[Построить маршрут до офиса Дисконт банка в Акко](https://maps.app.goo.gl/HPrqV1JQrk8SrWDMA)*"
    #                 , parse_mode='MarkdownV2', reply_markup=go_back_main_menu)

    # Отправка фото с текстом
    photo = open('bank_fasad2.jpg', 'rb')

    bot.send_photo(call.message.chat.id, photo, f"В этом разделе может быть рассказано о времени работы банка, как записаться на прием, адрес, основные принципы и отличия банковской системы, что такое чековая книжка и тп \n"
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

    #Отправка фото с текстом
    photo = open('image_1.png', 'rb')
    bot.send_photo(call.message.chat.id, photo, f"Напиши чем я могу быть полезен, \n"
                                           f"я могу рассказать про историю *Акко*, \n "
                                           f"посоветовать что приготовить на ужин, помочь составить резюме на иврите или просто поболтать \n"
                                           f"Просто отправь свой запрос в сообщении", parse_mode='MarkdownV2',
                     reply_markup=go_back_main_menu)


   #bot.send_message(call.message.chat.id, f"Напиши чем я могу быть полезен, \n"
   #                                       f"я могу рассказать про историю Акко, \n "
   #                                       f"посоветовать что приготовить на ужин, помочь составить резюме на иврите или просто поболтать \n"
   #                                       f"Просто отправь свой запрос в сообщении", parse_mode='MarkdownV2',
   #                 reply_markup=go_back_main_menu)

    chat_GPT_switch = True #Подключаем чат GPT


# Блок чата GPT
@bot.message_handler(func=lambda message: True)
def response_gpt_message (call):

    #global chat_GPT_switch
    mes = call.text
    if chat_GPT_switch==True:

        print(mes)
        client = Client()
        try:
            response = client.chat.completions.create(
                model=g4f.models.default,
                messages=[{"role": "user", "content": mes}],
                provider= g4f.Provider.Blackbox
                # Add any other necessary parameters
            )
            resp_gpt = (response.choices[0].message.content)
            bot.send_message(call.chat.id,f'{resp_gpt} \n\n Для главного меню нажмите /menu',)
        except Exception:
            bot.send_message(call.chat.id, f'Упс, что то пошло не по плану, попробуйте позже \n Для главного меню нажмите /menu \n Что бы узнать о преимуществах телеграмм бота \- нажми /info', )
        print (resp_gpt)
        print (response)
    else:
        bot_msg = bot.send_message(call.chat.id, f'Нажми /start что бы начать \nНажми /menu для перехода в основное меню \n Что бы узнать о преимуществах телеграм бота \- нажми /info'
                                   , parse_mode='MarkdownV2')

        #  функция запоминания id сообщений которые послал бот mes_clear_add_list(значение chat.id, значение message_id)
        mes_clear_add_list(bot_msg.chat.id,bot_msg.message_id)  # Функция для добавления id сообщений в список для удаления


bot.polling(none_stop=True)