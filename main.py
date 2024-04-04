import string
import random
import password_manager_class
import os
from tkinter import messagebox
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = 'green'  # "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
user_name_fill = ''


def forget():
    option_select.grid_forget()


def first_gui():
    option_select.grid(row=2, column=0, columnspan=2)


def enter(event):
    answer = option_select.curselection()

    def enter_name():
        get_pwd = user_pwd_entry.get()
        name = user_name_entry.get()

        def user_forget():
            user_pwd1.grid_forget()
            user_pwd_entry.grid_forget()
            user_name_entry.grid_forget()
            user_name_button.grid_forget()
            user_name1.grid_forget()

        def enter1(event1):
            def add_account():
                user_name3 = user_name3_entry.get()
                password = user_pwd3_entry.get()
                app = user_app_entry.get()
                save = password_manager_class.PasswordManager(user_name3, app, password)
                save.write(account_number)
                user_pwd3_entry.grid_forget()
                user_name3_entry.grid_forget()
                user_name3_label.grid_forget()
                user_pwd3.grid_forget()
                user_name3_button.grid_forget()
                user_app.grid_forget()
                user_app_entry.grid_forget()
                back_button.grid_forget()
                generate()

            def forget1():
                option_select1.grid_forget()
                print('bye')

            def generate():
                print('hello')
                option_select1.grid(row=2, column=0, columnspan=2)

            def back_ward():
                user_pwd3_entry.grid_forget()
                user_name3_entry.grid_forget()
                user_name3_label.grid_forget()
                user_pwd3.grid_forget()
                user_name3_button.grid_forget()
                user_app.grid_forget()
                user_app_entry.grid_forget()
                back_button.grid_forget()
                generate()

            num = option_select1.curselection()
            if len(num) > 0:
                if num[0] == 0:
                    forget1()
                    user_name3_label = Label(text="User Name :", font=(FONT_NAME, '20', 'bold'), fg=GREEN,
                                             highlightthickness=0,
                                             bg=YELLOW)
                    user_name3_label.grid(row=2, column=0)
                    user_name3_entry = Entry(width=50)
                    user_name3_entry.insert(END, string=user_name_fill)
                    user_name3_entry.grid(row=2, column=1)
                    user_name3_button = Button(text='ENTER', foreground=RED, bg=GREEN, command=add_account, width=20)
                    user_name3_button.grid(row=5, column=1)
                    user_pwd3 = Label(text="Password :", font=(FONT_NAME, '20', 'bold'), fg=GREEN,
                                      highlightthickness=0, bg=YELLOW)
                    user_pwd3.grid(row=4, column=0)
                    user_pwd3_entry = Entry(width=50)
                    user_pwd3_entry.grid(row=4, column=1)
                    user_app = Label(text="App :", font=(FONT_NAME, '20', 'bold'), fg=GREEN, highlightthickness=0,
                                     bg=YELLOW)
                    user_app.grid(row=3, column=0)
                    user_app_entry = Entry(width=50)
                    user_app_entry.grid(row=3, column=1)
                    back_button = Button(text='BACK', foreground=RED, bg=GREEN, command=back_ward, width=10)
                    back_button.grid(row=5, column=2)
                elif num[0] == 1:
                    forget1()
                    print('work')
                    password_manager_class.view(account_number)
                    generate()
                    generate()
                elif num[0] == 2:
                    forget1()
                    first_gui()
            else:
                forget1()

        print(name)
        account_number = -1
        with open('useraccounts.account', 'r') as file:
            closer = True
            while closer:
                user_counter = 1
                for line in file.readlines():
                    check_account = line.rstrip()
                    check_name, check_pwd = check_account.split('|')
                    if check_name == name:
                        if get_pwd == password_manager_class.decrypt(check_pwd):
                            closer = False
                            global user_name_fill
                            user_name_fill = name
                            user_forget()
                            print('works')
                            account_number = user_counter
                            break
                        else:
                            messagebox.showerror(title='Password', message='Incorrect Password')
                            closer = False
                            user_forget()
                            first_gui()
                            break
                    user_counter += 1
                if closer:
                    messagebox.showerror(title='User', message="No account by that name!!")
                    user_forget()
                    first_gui()
                    break
        if account_number == -1:
            first_gui()
            return
        path = 'key.key'

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
            with open(path, 'wb') as file1:
                file1.write(key.encode())

        with open(path, 'rb') as file:
            key = file.read().decode('utf-8')
            list(key)
        options_list1 = ['1.Add account', '2.View all accounts', '3.Sign Out']
        option_select1 = Listbox(height=3, font=(FONT_NAME, '20', 'bold'), fg=GREEN
                                 , highlightthickness=0, bg=YELLOW)
        for item1 in options_list1:
            option_select1.insert(options_list1.index(item1), item1)
        option_select1.grid(row=2, column=0, columnspan=2)
        option_select1.bind("<<ListboxSelect>>", enter1)
        for j in range(3):
            option_select1.itemconfig(j, selectbackground=YELLOW, selectforeground=GREEN)

    def sign_up_forget():
        user_signup_label.grid_forget()
        user_signup_entry.grid_forget()
        user_signup_pwd3.grid_forget()
        user_pwd_signup_entry.grid_forget()
        user_signup_confirm_pwd.grid_forget()
        user_signup_pwd_confirm_entry.grid_forget()
        user_signup_button.grid_forget()

    def sign_up():
        user = user_signup_entry.get()
        pwd = user_pwd_signup_entry.get()
        confirm_pwd = user_signup_pwd_confirm_entry.get()
        if pwd == confirm_pwd:
            messagebox.showinfo(title='Great', message='Successfully signed up')
            with open(path, 'a') as file2:
                account = user + '|' + password_manager_class.encrypt(pwd) + '\n'
                file2.write(account)
            sign_up_forget()
            first_gui()
        else:
            sign_up_forget()
            first_gui()
            messagebox.showerror(title='oops', message='Password and confirmation are different!!')

    print('bsda')
    if len(answer) > 0:
        if answer[0] == 0:
            forget()
            if not os.path.exists('useraccounts.account'):
                messagebox.showerror(title='OOPS', message='No account is signed up please signup to start')
                first_gui()
                return
            user_name1 = Label(text="User Name :", font=(FONT_NAME, '20', 'bold'), fg=GREEN, highlightthickness=0,
                               bg=YELLOW)
            user_name1.grid(row=2, column=0)
            user_name_entry = Entry(width=50, font=(FONT_NAME, 10, 'italic'), foreground=GREEN)
            user_name_entry.grid(row=2, column=1)
            user_name_button = Button(text='ENTER', foreground=RED, bg=GREEN, command=enter_name, width=30)
            user_name_button.grid(row=4, column=1)
            user_pwd1 = Label(text="Password :", font=(FONT_NAME, '20', 'bold'), fg=GREEN,
                              highlightthickness=0, bg=YELLOW)
            user_pwd1.grid(row=3, column=0)
            user_pwd_entry = Entry(width=50, font=(FONT_NAME, 10, 'italic'), foreground=GREEN)
            user_pwd_entry.grid(row=3, column=1)

        elif answer[0] == 1:
            forget()
            path = 'useraccounts.account'
            if os.path.exists(path):
                pass
            else:
                with open(path, 'a') as file:
                    pass
            user_signup_label = Label(text="User Name :", font=(FONT_NAME, '20', 'bold'), fg=GREEN,
                                      highlightthickness=0, bg=YELLOW)
            user_signup_label.grid(row=2, column=0)
            user_signup_entry = Entry(width=50)
            user_signup_entry.grid(row=2, column=1)
            user_signup_button = Button(text='ENTER', foreground=RED, bg=GREEN, command=sign_up, width=20)
            user_signup_button.grid(row=5, column=1)
            user_signup_pwd3 = Label(text="Confirm Password :", font=(FONT_NAME, '20', 'bold'), fg=GREEN,
                                     highlightthickness=0, bg=YELLOW)
            user_signup_pwd3.grid(row=4, column=0)
            user_pwd_signup_entry = Entry(width=50)
            user_pwd_signup_entry.grid(row=4, column=1)
            user_signup_confirm_pwd = Label(text="Password :", font=(FONT_NAME, '20', 'bold'), fg=GREEN, highlightthickness=0,
                                            bg=YELLOW)
            user_signup_confirm_pwd.grid(row=3, column=0)
            user_signup_pwd_confirm_entry = Entry(width=50)
            user_signup_pwd_confirm_entry.grid(row=3, column=1)

        elif answer[0] == 2:
            is_ok = messagebox.askyesno(title='Exit', message='Do You want to close the program')
            if is_ok:
                window.quit()

    else:
        forget()


window = Tk()
window.title('Password Manager')
window.config(padx=300, pady=100, bg=YELLOW)
canvas = Canvas(height=200, width=200, bg=YELLOW, highlightthickness=0)
logo: PhotoImage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
screen_title = Label(text="Password Manager", font=(FONT_NAME, '30', 'bold'), fg=RED, highlightthickness=0, bg=YELLOW)
screen_title.grid(row=1, column=1)
option_select = Listbox(height=3, font=(FONT_NAME, '20', 'bold'), fg=GREEN
                        , highlightthickness=0, bg=YELLOW)
options_list = ['1.Sign In', '2.Sign Up', '3.Exit']
for item in options_list:
    option_select.insert(options_list.index(item), item)
for i in range(3):
    option_select.itemconfig(i, selectbackground=YELLOW, selectforeground=GREEN)

option_select.grid(row=2, column=0, columnspan=2)
option_select.bind("<<ListboxSelect>>", enter)

window.mainloop()
