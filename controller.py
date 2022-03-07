from model import Model
from tkinter import Tk
from view import View
import argparse


class Controller:
    def __init__(self):
        self._root = Tk()
        self._model = Model()
        self.__set_args__()
        self._view = View(self._root, self._model)

    def run(self):
        self._root.deiconify()
        self._root.mainloop()

    def __set_args__(self):
        parser = argparse.ArgumentParser(description='Parser')
        parser.add_argument('-s', '--string', type=str,
                            help='Input string', nargs='?')
        parser.add_argument('-p', '--pattern', type=str,
                            help='Input pattern', nargs='?')
        args = parser.parse_args()
        if args.string:
            self._model.string = args.string
        if args.pattern:
            self._model.pattern = args.pattern
