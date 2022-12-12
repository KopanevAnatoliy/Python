from random import randint


class Hangman:

    __RUS_ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    def __init__(self, faults: int = 5):
        self.__faults = faults
        self.__word = self.generate_word().upper()
        self.__hidden_word = ['_' for _ in self.__word]
        self.__trying_letters = []

    @staticmethod
    def generate_word() -> str:
        with open(r'C:\Users\kami-\PycharmProjects\The_Gallows\src\WordsStockRus.txt', encoding='utf-8-sig') as words:
            lst_words = words.read().split()
        return lst_words[randint(0, len(lst_words) - 1)]

    def try_letter(self, letter: str) -> None:
        letter = letter.upper()
        if letter in self.__word:
            for i, item in enumerate(self.__word):
                if item == letter:
                    self.__hidden_word[i] = letter
        else:
            self.__faults -= 1
        self.__trying_letters.append(letter)
        self.__trying_letters.sort()

    @property
    def word(self) -> str:
        return self.__word

    @property
    def faults(self) -> int:
        return self.__faults

    @property
    def hidden_word(self) -> str:
        return ''.join(self.__hidden_word)

    @property
    def trying_letters(self) -> str:
        return ' '.join(self.__trying_letters)

    def check_letter(self, letter: str) -> bool:
        if len(letter) == 1 and letter not in self.__trying_letters and letter in Hangman.__RUS_ALPHABET:
            return True
        else:
            return False

    def check_win(self) -> bool:
        return '_' not in self.hidden_word

    def check_defeat(self) -> bool:
        return not self.__faults