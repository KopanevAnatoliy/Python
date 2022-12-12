import os
from typing import Optional


class TrueFalse:

    def __init__(self, faults: int = 2, path: Optional[str] = None):
        if path is None:
            self.__path = '../../PycharmProjects/TrueFalse/data/Questions.csv'
        elif os.path.exists(path):
            self.__path = path
        else:
            raise FileNotFoundError('No such file or directory')
        self.__q_a = self.convert_text()
        self.__faults = faults
        self.__numb_qa = 0

    def convert_text(self) -> list[tuple[str, bool, str]]:
        def string_to_bool(string):
            lst = string.split(';')
            lst[1] = True if lst[1] == 'Yes' else False
            return tuple(lst)

        with open(self.__path) as file:
            text = file.read()
        q_a = [string_to_bool(i) for i in text.split('\n')]
        return q_a

    def give_an_answer(self, answer: bool):
        if self.__q_a[self.__numb_qa][1] != answer:
            self.__faults -= 1
        self.__numb_qa += 1

    def game_status(self) -> Optional[bool]:
        if self.__faults == 0:
            return False
        if self.__numb_qa >= len(self.__q_a):
            return True
        else:
            return None

    @property
    def faults(self):
        return self.faults

    def get_answer(self):
        return self.__q_a[self.__numb_qa]