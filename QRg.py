from tkinter import *
import pyqrcode
from PIL import Image, ImageTk
import png

root = Tk()


def QRcode():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + '.png'
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    img_lb = Label(root, image=image)
    img_lb.image=image
    canvas.create_window(200, 450, window=img_lb)


canvas = Canvas(root, width=400, height=600)
canvas.pack()
can_label = Label(root, text="QR code generator", fg='red', font=('Arial', 30))
canvas.create_window(200, 50, window=can_label)
name_label = Label(root, text="Link name")
link_label = Label(root, text='Link')
name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 190, window=link_entry)

button = Button(root, text="Generate QR code", command=QRcode)
canvas.create_window(200, 220, window=button)

root.mainloop()
