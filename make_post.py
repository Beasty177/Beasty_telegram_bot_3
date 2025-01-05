import telebot
from tkinter import *


#from aiohttp.web_fileresponse import content_type
#from soupsieve.util import lower
from telebot import types
from PIL import Image

token='8147781080:AAFvPegxmvmzd5Um1ouuuEpBtWfITR2bGHU'
bot=telebot.TeleBot(token,)

user_dict = {}


class Vtrnk:
    def __init__(self,dj):
        self.dj = dj
        self.date = None
        self.afisha = None
        self.photo= None
        self.post_mode=False

Vtrnk.post_mode=False
logo_past=False


@bot.message_handler(commands=['logo'])
def logo_welcome(message):
    global logo_past
    bot.send_message(message.chat.id, f'Пришли мне фото и я добавлю на него логотип VTRNK')
    chat_id = message.chat.id
    user_id = message.from_user.id
    print(chat_id)
    print(user_id)
    if chat_id != user_id:
        logo_past=True



# Handle '/post'
@bot.message_handler(commands=['post'])

def send_welcome(message):

    msg = bot.reply_to(message, """\
Йо, я Beasty Bot, давай делать пост с афишей.
Напиши ник DJ, который будет выступать
""")
    bot.register_next_step_handler(msg, dj_nik_set)


def dj_nik_set (message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        print(chat_id)
        print(user_id)
        if chat_id != user_id:

            return


        dj = str(message.text)
        print (dj)
        print (len(dj))



        if len(dj) <=1:

            msg = bot.reply_to(message, 'Не, давай по нормальному ник напиши)')
            bot.register_next_step_handler(msg, dj_nik_set)
            return



        user = Vtrnk(dj)
        user_dict[chat_id] = user
        user.post_mode=True

        print(user.post_mode)

        msg = bot.reply_to(message, 'Хуя се..., а когда? напиши дату, может я гляну в трансляции потом)')
        bot.register_next_step_handler(msg, process_date_step)
    except Exception as e:
        bot.reply_to(message, 'oooops, все хуня, переделываем... нажми /post')

def process_date_step(message):
    try:
        chat_id = message.chat.id
        vtrnk_date = message.text
        #if not age.isdigit():
        #    msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #    bot.register_next_step_handler(msg, process_age_step)
        #    return
        user = user_dict[chat_id]
        user.date = vtrnk_date



        msg = bot.reply_to(message, 'Заебись, теперь добавь основной текст для афиши или напиши что угодно - потом можно изменить')
        bot.register_next_step_handler(msg, afisha_past_user_step)
    except Exception as e:
        bot.reply_to(message, 'oooops, все хуня, переделываем... нажми /post')


def afisha_past_user_step(message):
    try:

        chat_id = message.chat.id
        afisha = message.text
        user = user_dict[chat_id]
        # '_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!'
        z=['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
        for i in z:
            afisha = afisha.replace(i, f"\{i}")


        print (afisha)


        user.afisha = afisha

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Добавить ФОТО', 'Не нужно')
        msg = bot.reply_to(message, '*ФOTO будем добавлять в пост?* \n Вообще уже нормально получается?',parse_mode='MarkdownV2',
                           reply_markup=markup)
        bot.register_next_step_handler(msg, photo_past_step)
    except Exception as e:
        print (e)
        bot.reply_to(message, 'oooops, все хуня, переделываем... нажми /post')


def photo_past_step (message):
    try:
        chat_id = message.chat.id
        photo_y_n= message.text
        user = user_dict[chat_id]
        if (photo_y_n == 'Не нужно'):
            msg = bot.reply_to(message, 'Фотку можешь потом вставить самостоятельно')

            #bot.register_next_step_handler(msg, post_bez_photo)
            post_bez_photo(message)

        elif (photo_y_n == 'Добавить ФОТО'):
            msg = bot.reply_to(message, 'Присылай фотку, сейчас вставлю в афишу')
            bot.register_next_step_handler(msg, photo_past_afisha) # Тут нужно разобраться

        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Добавить ФОТО', 'Не, не нужно')
            msg = bot.reply_to(message, 'Нехуя непонятно, просто нажми кнопку, надо или нет)',reply_markup=markup)


            bot.register_next_step_handler(msg, photo_past_step)
            return

    except Exception as e:
        bot.reply_to(message, 'oooops, все хуня, переделываем... нажми /post')


def post_bez_photo (message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]

        msg=bot.send_message(message.chat.id, f'\n *[VTRNK Radio Show](https://t.me/vtornikshow)*'
									                           f'\n *{user.date}* '
									                           f'\n  с 20:00 до 02:00'
									                           f'\n \n *{user.dj.upper()}* \n '
									                           f'\n {user.afisha}'
									                           f'\n '
									                           f'\nКлуб *[Лахесис](https://t.me/lachesis_groves)*'
									                           f'\nБесплатный вход, FC \n c 20:00 до 02:00 \n Покровка 21\-23/25с4'
									                           f'\n*[Наш чат и стрим в Tg ](https://t.me/beastybeats23)*'
									                           f'\n*[Группа VK фото и видео ](https://vk.com/vtornikshow)*'
									                           f'\n*[Архив сетов наших резидентов и друзей ](https://t.me/vtrnkmix)*'
									                           f'\n \n||Поддержать наш проект можно тут  \n @VTRNK_Donat_bot||'
									                           ,parse_mode='MarkdownV2')



    except Exception as e:

        bot.reply_to(message, 'oooops, все хуня, переделываем... нажми /post')

def photo_past_afisha(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        c_tipe = message.content_type
        if c_tipe != 'photo':
            msg = bot.reply_to(message, 'Не, лучше пришли фоткой, а не файлом или чем то еще')
            bot.register_next_step_handler(msg, afisha_past_user_step)
            return

        user.photo = message.photo[-1]
        bot.send_photo(message.chat.id, message.photo[-1].file_id, f'\n *[VTRNK Radio Show](https://t.me/vtornikshow)*'
        								                           f'\n*{user.date}* '
        								                           f'\nс 20:00 до 02:00'
        								                           f'\n \n*{user.dj.upper()}* \n '
        								                           f'\n{user.afisha}'
        								                           f'\n '
        								                           f'\nКлуб *[Лахесис](https://t.me/lachesis_groves)*'
        								                           f'\nБесплатный вход, FC \n c 20:00 до 02:00 \n Покровка 21\-23/25с4'
        								                           f' \n*[Наш чат и стрим в Tg ](https://t.me/beastybeats23)*'
        								                           f'\n*[Группа VK фото и видео ](https://vk.com/vtornikshow)*'
        								                           f'\n*[Архив сетов наших резидентов и друзей ](https://t.me/vtrnkmix)*'
        								                           f'\n \n||Поддержать наш проект можно тут  \n @VTRNK_Donat_bot||'
        								                            ,parse_mode='MarkdownV2')

    except Exception as e:
        bot.reply_to(message, 'oooops, все хуня, переделываем... нажми /post')








@bot.message_handler(content_types=['photo'])
def photo_past_logo(message):
    global logo_past
    chat_id = message.chat.id
    user_id = message.from_user.id
    print(chat_id)
    print(user_id)
    if chat_id != user_id and logo_past == False :
        return

    try:

        chat_id = message.chat.id
        user=Vtrnk
        user_dict[chat_id]=user
        user = user_dict[chat_id]
        user.post_mode = False

        #print(message)
        photo = message.photo[-1]

        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        save_path = 'photo_for_logo_past.jpg'
        filename = bot.download_file(file_info.file_path)
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        # bot.reply_to(message, 'Фотография сохранена.')
        #print(photo)
        # print(photo2)
        print(file_info)

        filename = save_path
        # filename=downloaded_file
        # print (filename)
        try:

             logo_filename = 'logo_vtrnk.png'

             img = Image.open(filename)
             logo = Image.open(logo_filename)
             logo = logo.reduce(8)

             w_img = img.width
             h_img = img.height

             print(img.format)
             print(img.width)
             print(img.size)
             print(img.mode)

             print(logo.format)
             print(logo.size)
             print(logo.mode)
             # logo.show()

             # blank = logo.point(lambda _: 0)
             # logo_segmented = Image.composite(logo, blank, logo)
             # logo_segmented.show()
             img.paste(logo, (w_img - 260, h_img - 220), logo)
             # img.show()
             img.save("new_img.jpg")
             # Отправка фото с тестом
             photo = open('new_img.jpg', 'rb')

             bot_msg = bot.send_photo(message.chat.id, photo,
                                      f"Logo добавлено", parse_mode='MarkdownV2')

        except Exception as er:
            print(er)

    except Exception as e:
         bot.reply_to(message, 'oooops, все хуня, переделываем... нажми /logo или /start')

    logo_past=False



@bot.message_handler(func=lambda message: True)
def hello_message (message):
    chat_id = message.chat.id
    user_id= message.from_user.id
    print (chat_id)
    print(user_id)
    if chat_id == user_id:

        bot.reply_to(message, 'Йо, отправь мне фото и я добавлю на него лого VTRNK \nЧто бы подготовить афишу нажми /post')
    else:
        return







bot.polling()