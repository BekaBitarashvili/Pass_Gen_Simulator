# ბიბლიოთეკები
from tkinter import *
import random, string
import pyperclip

# ფანჯარა
root = Tk()
root.geometry("400x300")
root.resizable(0,0)
root.title("პაროლის გენერატორი")

Label(root, text = 'გენერატორი' , font ='arial 15 bold').pack()
Label(root, text ='ბექა', font ='arial 15 bold').pack(side = BOTTOM)

# პაროლის სიგრძე
pass_label = Label(root, text = 'პაროლის სიგრძე', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

# ფუნქცია
pass_str = StringVar()
def Generator():
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

# ღილაკი
Button(root, text = "გენერირება" , command = Generator ).pack(pady= 5)
Entry(root , textvariable = pass_str).pack()

# კოპირების ფუნქცია
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'კოპირება', command = Copy_password).pack(pady=5)

# გაშვება
root.mainloop()