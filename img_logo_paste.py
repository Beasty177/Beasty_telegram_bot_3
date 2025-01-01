from PIL import Image
try:

     filename = "photo_2025-01-01_20-25-27.jpg"
     logo_filename = 'logo_vtrnk.png'

     img=Image.open(filename)
     logo=Image.open(logo_filename)
     logo=logo.reduce(8)

     w_img= img.width
     h_img= img.height






     print(img.format)
     print(img.width)
     print(img.size)
     print(img.mode)

     print(logo.format)
     print(logo.size)
     print(logo.mode)
     #logo.show()

     #blank = logo.point(lambda _: 0)
     #logo_segmented = Image.composite(logo, blank, logo)
     #logo_segmented.show()


     #img=img.convert("PNG")
     img.paste(logo,(w_img-260,h_img-200),logo)
     #img_low=img.resize((img.width//2,img.height//2))
     #img_low.show()
     img.show()






     img.save("new_img.jpg")
except Exception as e:
     print(e)


#   type(img)
#   <class 'PIL.JpegImagePlugin.JpegImageFile'>

#   isinstance(img, Image.Image)

#   True