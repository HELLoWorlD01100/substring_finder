import tkinter.scrolledtext as tk_scrolled
from tkinter import ttk, Button, Entry, Label, WORD, font as tk_font


class SidePanel:
    def __init__(self, root):
        self.__root__ = root

        root.title('Substring Hunter')
        self.main_font = tk_font.Font(family="Times")
        self.auxiliary_font = tk_font.Font(family="Times")
        #
        # Текстовый виджет
        self.text = tk_scrolled.ScrolledText(wrap=WORD, font=self.main_font)
        self.text.place(relwidth=0.6, relheight=0.85, relx=0.02, rely=0.02)


        #
        # Кнопка старта
        self.button_start = Button(text='Start', font=self.auxiliary_font)
        self.button_start.place(relwidth=0.3, relheight=0.07,
                                relx=0.65, rely=0.02)
        #
        # Кнопка хода
        self.button_move = Button(text='Make a move', font=self.auxiliary_font)
        self.button_move.place(relwidth=0.3, relheight=0.07,
                               relx=0.65, rely=0.12)
        #
        # Кнопка финиша
        self.button_finish = Button(text='Finish', font=self.auxiliary_font)
        self.button_finish.place(relwidth=0.3, relheight=0.07,
                                 relx=0.65, rely=0.22)
        #
        # Лейбл для выбора алгоритма
        self.label_help_combobox = Label(text='Select algorithm', font=self.auxiliary_font)
        self.label_help_combobox.place(relwidth=0.3, relheight=0.07,
                                       relx=0.65, rely=0.3)
        #
        # Комбобокс выбора алгоритма
        self.algorithms_box = ttk.Combobox(values=['Brut Force',
                                                   'Boyer-Moore',
                                                   'Rabin-Karp',
                                                   'Knuth-Morris-Pratt'],
                                           state='readonly', font=self.auxiliary_font)
        self.algorithms_box.current(0)
        self.algorithms_box.place(relwidth=0.3, relheight=0.07,
                                  relx=0.65, rely=0.37)
        #
        # Лейбл для ввода подстроки
        self.label_help_entry = Label(text='Enter a substring:', font=self.auxiliary_font)
        self.label_help_entry.place(relwidth=0.3, relheight=0.07,
                                    relx=0.65, rely=0.45)
        #
        # Энтри для ввода подстроки
        self.pattern_entry = Entry(font=self.auxiliary_font)
        self.pattern_entry.place(relwidth=0.3, relheight=0.07,
                                 relx=0.65, rely=0.52)

        self.button_start.bind('<Configure>', self.auxiliary_resize)
        self.text.bind('<Configure>', self.main_resize)

    def main_resize(self, event):
        self.main_font['size'] = int(event.widget.winfo_height() / 25)

    def auxiliary_resize(self, event):
        self.auxiliary_font['size'] = int(event.widget.winfo_height() / 3)
