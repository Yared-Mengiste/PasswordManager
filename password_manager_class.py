import string
import random
import os
from tkinter import *
from tkinter import messagebox
PINK = "#e2979c"
RED = "#e7305b"
GREEN = 'green'  # "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


path = 'key.key'
char = " " + string.digits + string.ascii_letters + string.punctuation

if os.path.exists(path):
    pass
else:
    char = " " + string.digits + string.ascii_letters + string.punctuation
    char = list(char)
    print(char)
    key = ''
    random.shuffle(char)
    for x in char:
        key += x
    with open(path, 'wb') as file:
        file.write(key.encode())

with open(path, 'rb') as file:
    key = file.read().decode('utf-8')
    key = list(key)


def view(num):
    counter = 1
    raw = 2
    labels = []
    label2 = ''
    if not os.path.exists(f'password_manager{num}.txt'):
        messagebox.showerror(title='oops', message='No account to view please add to view')
        return
    os.system('cls')
    text = Text(font=(FONT_NAME, 15, 'bold'), fg=GREEN, highlightthickness=0, bg=YELLOW, height=10, width=50)
    text.grid(row=2, column=1)
    with open(f'password_manager{num}.txt') as file:
        for user1 in file.readlines():
            user1 = user1.rstrip()
            user, app, encryption = user1.split("|")
            passwd = ''
            for x in encryption:
                index = key.index(x)
                passwd += char[index]
            labels.append(Label(text=f'{counter}.User Name : {user:<15}\n  App       : {app:<15}\n  Password  : {passwd:<15}'
                                , font=(FONT_NAME, 15, 'bold'), fg=GREEN, highlightthickness=0, bg=YELLOW))
            label2 += f'\n{counter}.User Name : {user:<15}\n  App       : {app:<15}\n  Password  : {passwd:<15}'
            counter += 1
    text.insert(END, label2)

    def back():
        button.grid_forget()
        text.grid_forget()
        # for label1 in labels:
        #     label1.grid_forget()
        # return True
    button = Button(text='Back', foreground=RED, bg=GREEN, command=back, width=10)
    button.grid(row=raw + 1, column=1)


def decrypt(encryption):
    passwd = ''
    for x in encryption:
        index = key.index(x)
        passwd += char[index]
    return passwd


def encrypt(passwd):
    encryption = ''
    for x in passwd:
        index = char.index(x)
        encryption += key[index]
    return encryption


class PasswordManager:

    def __init__(self, user_name, app, password):
        self.user_name = user_name
        self.password = password
        self.app = app
        self.encryption = self.encrypt()

    def encrypt(self):
        encryption = ""
        for x in self.password:
            index = char.index(x)
            encryption += key[index]
        return encryption

    def decrypt(self):
        passwd = ""
        for x in self.encryption:
            index = key.index(x)
            passwd += char[index]
        return passwd

    def write(self, num):
        with open(f'password_manager{num}.txt', 'a') as file:
            file.write(self.user_name + '|' + self.app + '|' + self.encryption + '\n')
