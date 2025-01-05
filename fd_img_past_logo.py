from tkinter import *
from PIL import Image
from tkinter import filedialog as fd



def get_file():
    file= fd.askopenfilename()


    return file



def image_add_logo():
    filename=get_file()
    print (filename)
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

        img.show()

        img.save("new_img.jpg")

    except Exception as er:
        print(er)




win = Tk()
win.title("Вставка лого в фото")
win.geometry("500x100")

Button(win, text="Выбрать файл",font=("Arial",14), command=image_add_logo).pack(pady=30)


win.mainloop()
















