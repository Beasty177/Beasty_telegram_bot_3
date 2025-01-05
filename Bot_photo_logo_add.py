import telebot
from PIL import Image

token='8147781080:AAFvPegxmvmzd5Um1ouuuEpBtWfITR2bGHU'
bot=telebot.TeleBot(token,)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    print(message)
    photo = message.photo[-1]

    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = 'photo_for_logo_past.jpg'
    filename = bot.download_file(file_info.file_path)
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    #bot.reply_to(message, 'Фотография сохранена.')
    print (photo)
    #print(photo2)
    print (file_info)

    filename= save_path
    #filename=downloaded_file
    #print (filename)
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
       #img.show()
       img.save("new_img.jpg")
       # Отправка фото с тестом
       photo = open('new_img.jpg', 'rb')

       bot_msg = bot.send_photo(message.chat.id, photo,
                                f"Logo добавлено", parse_mode='MarkdownV2')

    except Exception as er:
        print(er)













bot.polling()