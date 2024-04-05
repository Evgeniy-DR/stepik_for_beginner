from tkinter import *
import random
import tkinter as tk
from tkinter import Entry, Label, Button, StringVar

class MagicBallApp:
    def __init__(self, master):
        self.master = master
        master.title("Магический Шар 8")

        self.answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
                        "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
                        "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
                        "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
                        "Перспективы не очень хорошие", "Весьма сомнительно"]

        self.exit_word = "exit"

        self.label = Label(master, text="Задайте свой вопрос:", background="white", foreground="black")
        self.label.pack()

        self.entry = Entry(master, background="white", foreground="black")
        self.entry.pack()

        self.answer_var = StringVar()
        self.answer_label = Label(master, textvariable=self.answer_var, background="white", foreground="black")
        self.answer_label.pack()

        self.ask_button = Button(master, text="Спросить", command=self.ask_question, background="gray", foreground="white")
        self.ask_button.pack()

    def ask_question(self):
        question = self.entry.get().lower()
        if question == self.exit_word:
            self.answer_var.set("Завершение программы")
            self.master.quit()
        else:
            self.answer_var.set(self.answers[random.randint(0, 19)])

if __name__ == "__main__":
    root = tk.Tk()
    app = MagicBallApp(root)
    root.mainloop()
