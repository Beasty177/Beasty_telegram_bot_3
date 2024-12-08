import telebot
#from telebot import formatting
from random import choice
#from telebot import types

token = '8147781080:AAFvPegxmvmzd5Um1ouuuEpBtWfITR2bGHU'
bot = telebot.TeleBot(token)

random_hello=['Ну здарова, ёпта','Хули надо, кожаный',"🖕",'Бля, отъебись нахуй, я занят','Лан, привет, чё надо, давай только быстро','Добрейшего денёчка']

link_main="https://t.me/vtornikshow"

text_top_post = {"VTRNK Radio Show":"https://t.me/vtornikshow"}

vtrnk_data="10 декабря 2024"
vtrnk_dj_nik = "Beasty"
#mes=[]
bot_name = ["уебок","пиздюк", "ушлепок", "уебок,","пиздюк,", "ушлепок,""уебок?","пиздюк?", "ушлепок?" ]

@bot.message_handler(commands=['hello'])
def rand_hello(message):
	task = choice(random_hello)
	bot.send_message(message.chat.id, task)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "🖕" )


@bot.message_handler(func=lambda message: True)
def hello_message (message):
	mes=None
	mes= message.text.lower().split()
	for i in bot_name:
		print (i)
		if i in mes:
			task = choice(random_hello)
			bot.reply_to(message, task)
			#mes = None
			return

	#print (mes)
	#mes=None
	echo_all(message)


#@bot.message_handler(func=lambda message: True)
def echo_all(message):
	# Это эхо бот
	bot.reply_to(message, message.text)

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
									  f'\n \n  ', parse_mode='MarkdownV2')


	#print (message)

bot.infinity_polling()