import telebot
from telebot import formatting
from random import choice
from telebot import types

token = '8147781080:AAFvPegxmvmzd5Um1ouuuEpBtWfITR2bGHU'
bot = telebot.TeleBot(token)

random_hello=['Ну здарова, ёпта','Хули надо, кожаный','Бля, отъебись, я занят нахуй','Лан, привет, чё надо, давай только быстро','Добрейшего денёчка']

link_main="https://t.me/vtornikshow"

text_top_post = "[VTRNK Radio Show](https://t.me/vtornikshow)"

vtrnk_data="10 декабря 2024"
vtrnk_dj_nik = "Beasty"
mes=[]
bot_name = "уебок"

@bot.message_handler(commands=['hello'])
def rand_hello(message):
    task = choice(random_hello)
    bot.send_message(message.chat.id, task)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, TEST how are you doing?" )


@bot.message_handler(func=lambda message: True)
def hello_message (message):
	mes= message.text.split()
	if bot_name in mes:
		task = choice(random_hello)
		bot.reply_to(message, task)
	print (mes)

	mes=None


#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#
#	#bot.reply_to(message, message.text)
#	bot.send_message(message.chat.id, f'__Нижнее подчёркивание__ '
#									  f'\n ~Зачёркнутый~ '
#									  f'\n *text* '
#									  f'\n ||spoiler|| '
#									  f'\n *[VTRNK Radio Show](https://t.me/vtornikshow)*', parse_mode='MarkdownV2')
#	bot.send_message(message.chat.id, f'{text_top_post} \n Прив прив прив \n {message.text} Hello, *world*')


	#print (message)

bot.infinity_polling()