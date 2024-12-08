import telebot
#from telebot import formatting
from random import choice
from telebot import types

token = '8147781080:AAFvPegxmvmzd5Um1ouuuEpBtWfITR2bGHU'
bot = telebot.TeleBot(token)

bot_name = ["уебок","пиздюк", "ушлепок", "уебок,","пиздюк,", "ушлепок,""уебок?","пиздюк?", "ушлепок?" ]
random_hello=['Ну здарова, ёпта','Хули надо, кожаный',"🖕",'Бля, отъебись нахуй, я занят','Лан, привет, чё надо, давай только быстро','Добрейшего денёчка']



vtrnk_data="10 декабря 2024"
vtrnk_dj_nik = "Beasty"

name_user="Бро"

@bot.message_handler(commands=['hello'])
def rand_hello(message):
	task = choice(random_hello)
	bot.send_message(message.chat.id, task)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	#bot.reply_to(message, f" {message.from_user.first_name}🖕" )
	bot.reply_to(message, "🖕")

@bot.message_handler(commands=['menu', 'buttons'])

#Кнопки в сообщении

#def main_menu(message):
#	markup = types.InlineKeyboardMarkup()
#	#Кнопки одна под другой
#	#markup.add(types.InlineKeyboardButton("Наш канал Тг", url="https://t.me/vtornikshow"))
#	#markup.add(types.InlineKeyboardButton("Сделать афишу", callback_data='afi'))
#
#	#Кнопки вряд
#	btn1= types.InlineKeyboardButton("Наш канал Тг", url="https://t.me/vtornikshow")
#	btn2= types.InlineKeyboardButton("Сделать афишу", callback_data='afi')
#	markup.row(btn1, btn2)
#
#	#Вывод кнопок и текста
#	bot.send_message(message.chat.id, f'*Гля какие кнопочки\!* ',parse_mode='MarkdownV2', reply_markup=markup)


#     # Действия на кнопку
#@bot.callback_query_handler(func=lambda callback: True)
#def btn_callback(callback):
#	if callback.data == 'afi':
#		bot.send_message(callback.message.chat.id, f'Сейчас займемся')

# Кнопки внизу большие

def main_menu(message):
	markup=types.ReplyKeyboardMarkup()
	btn1=types.KeyboardButton('Наш канал')
	btn2 = types.KeyboardButton('Сделать афишу')
	markup.row(btn1,btn2)
	bot.send_message(message.chat.id, f'*Гля какие кнопочки\!* ',
					 parse_mode='MarkdownV2', reply_markup=markup)
	bot.register_next_step_handler(message,btn_answer)

def btn_answer(message):
	if message.text == 'Сделать афишу':
		bot.send_message(message.chat.id, f'Не бойся {message.from_user.first_name} Сейчас займемся', parse_mode='MarkdownV2')
	elif message.text == 'Наш канал':
		bot.send_message(message.chat.id, f'Вообще то {name_user} адрес канала нужно помнить'
												   f'\n [VTRNK](https://t.me/vtornikshow)', parse_mode='MarkdownV2')





@bot.message_handler(func=lambda message: True)
def hello_message (message):
	mes=None
	mes= message.text.lower().split()
	for i in bot_name:
		#i это варианты написания имени в списке имен бота
		#print (i)
		if i in mes:
			task = choice(random_hello)
			bot.reply_to(message, task)
			#mes = None
			return

	#print (mes)
	#mes=None
	echo_all(message)

#@bot.message_handler(func=lambda message: True)
def echo_all(message ):
	# Это эхо бот
	#bot.reply_to(message, message.text, entities=message.entities )


	#Ответ бота - сообщение пользователя с добавлением верхней и нижней части поста
	bot.send_message(message.chat.id, f'\n *[VTRNK Radio Show](https://t.me/vtornikshow)*'
									  f'\n {vtrnk_data} '
									  f'\n  с 20:00 до 02:00'
									  f'\n \n *{vtrnk_dj_nik.upper()}* \n '
									  f'\n {message.text}'
									  f'\n '
									  f'\n Клуб *[Лахесис](https://t.me/lachesis_groves)*'
									  f'\n Бесплатный вход, FC \n c 20:00 до 02:00 \n Покровка 21\-23/25с4'
									  f'\n \n *[Наш чат и стрим в Tg ](https://t.me/beastybeats23)*'
									  f'\n *[Группа VK фото и видео ](https://vk.com/vtornikshow)*'
									  f'\n *[Архив сетов наших резидентов и друзей ](https://t.me/vtrnkmix)*'
									  f'\n \n ||Поддержать наш проект можно тут  \n @VTRNK_Donat_bot||'
									  f'\n \n  ',parse_mode='MarkdownV2')


	#print (message)

bot.infinity_polling()