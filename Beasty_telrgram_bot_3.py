import telebot
from telebot import formatting
from telebot import types


token = '8147781080:AAFvPegxmvmzd5Um1ouuuEpBtWfITR2bGHU'
bot = telebot.TeleBot(token)

link_main="https://t.me/vtornikshow"

text_top_post = "[VTRNK Radio Show] (https://t.me/vtornikshow)"

vtrnk_data="10 декабря 2024"
vtrnk_dj_nik = "Beasty"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, TEST how are you doing?" )


@bot.message_handler(commands=['button'])
def button_message(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("Кнопка")
	markup.add(item1)
	bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.chat.id,"https://t.me/vtornikshow")



@bot.message_handler(func=lambda message: True)
def echo_all(message):

	bot.reply_to(message, message.text)

	bot.send_message(message.chat.id, f'{text_top_post} \n Прив прив прив \n {message.text} Hello, *world*')

	bot.send_message(message.chat.id, formatting.format_text(formatting.mbold(text_top_post),

	(f'Приглашаем на эфир {vtrnk_data} c 20:00 до 02:00 \n'),
	formatting.mbold(vtrnk_dj_nik.upper()),(''), (message.text)),

	parse_mode='MarkdownV2')

	#print (message)

bot.infinity_polling()