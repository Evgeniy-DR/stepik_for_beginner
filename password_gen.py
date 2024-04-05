# программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то,
# какие символы требуется в него включить, а какие исключить.
# import string
# import random
#
#
# length = int(input('Enter length password: '))
# alphabet_password = input('Use alphabet (yes/not): ')
# digit_password = input('Use digit (yes/not): ')
# symbol_password = input('Use symbol (yes/not): ')
#
#
# def gen_password(alphabet_password):
#     if alphabet_password == 'yes':
#         alphabet_password_gen = string.ascii_letters
#     if digit_password == 'yes':
#         digit_password_gen = string.digits
#     if symbol_password == 'yes':
#         symbol_password_gen = string.punctuation
#
#     all_characters_symbols = alphabet_password_gen + digit_password_gen + symbol_password_gen
#
#     result_password = ''.join(random.choice(all_characters_symbols) for _ in range(length))
#     return result_password
#
#
#
# print(gen_password(alphabet_password))


# __________________my code and tkinter________________


import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
import string
import random


class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        self.length_label = Label(master, text="Enter password length:")
        self.length_label.pack()

        self.length_entry = Entry(master)
        self.length_entry.pack()

        self.alphabet_var = StringVar()
        self.alphabet_var.set("yes")
        self.alphabet_checkbox = tk.Checkbutton(master, text="Use alphabet", variable=self.alphabet_var)
        self.alphabet_checkbox.pack()

        self.digit_var = StringVar()
        self.digit_var.set("yes")
        self.digit_checkbox = tk.Checkbutton(master, text="Use digit", variable=self.digit_var)
        self.digit_checkbox.pack()

        self.symbol_var = StringVar()
        self.symbol_var.set("yes")
        self.symbol_checkbox = tk.Checkbutton(master, text="Use symbol", variable=self.symbol_var)
        self.symbol_checkbox.pack()

        self.generate_button = Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        alphabet_password = self.alphabet_var.get()
        digit_password = self.digit_var.get()
        symbol_password = self.symbol_var.get()

        if alphabet_password == 'yes':
            alphabet_password_gen = string.ascii_letters
        else:
            alphabet_password_gen = ''

        if digit_password == 'yes':
            digit_password_gen = string.digits
        else:
            digit_password_gen = ''

        if symbol_password == 'yes':
            symbol_password_gen = string.punctuation
        else:
            symbol_password_gen = ''

        all_characters_symbols = alphabet_password_gen + digit_password_gen + symbol_password_gen

        result_password = ''.join(random.choice(all_characters_symbols) for _ in range(length))
        self.result_label.config(text=result_password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
