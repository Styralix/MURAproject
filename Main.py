from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd

import pytesseract as pt
from PIL import Image

root = tk.Tk()
root.title('Image Reader v1.00')
root.geometry('700x600')
path = None

explanation = Label(root, text="Select a file(image) (browse with all files if you can't see your file) and then press 'Show Image Path'").pack()
explanation2 = Label(root, text='Press CTRL + A to select the text').pack()


def select_file():
    global path
    filetypes = (('png files', '*.png'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir='Desktop', filetypes=filetypes)
    path = filename


def show_info():
    if path:
        pt.pytesseract.tesseract_cmd = r'D:\pytesseract\tesseract.exe'
        img_object = Image.open(path)
        img_text = pt.image_to_string(img_object)

        label = Entry(root, font=('Helvetica', 20), bd=0, width=50)
        label.insert(0, img_text)
        label.config(state='readonly')
        label.pack()


open_button = Button(root, text='Open a File', command=select_file)
open_button.pack(expand=True)

button = Button(root, text='Show Image Path', command=show_info)
button.pack()

root.mainloop()
