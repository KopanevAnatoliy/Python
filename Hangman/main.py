import Hangman


def difficult() -> int:
    while True:
        print('Введите колличество допустимых ошибок')
        temp = input()
        try:
            numb = int(temp)
        except ValueError:
            print('Ошибка: вы ввели не число')
        else:
            if numb > 0:
                print(f'Колличество попыток: {numb}')
                return numb
            else:
                print('Ошибка: вы ввели отрицательное число')
                continue


def next_game() -> Hangman:
    while True:
        answer = str(input('Y/N ')).lower()
        if answer == 'n' or answer == 'н':
            exit()
        else:
            return Hangman.Hangman(difficult())


word = Hangman.Hangman(difficult())
while True:
    inp_letter = input('Введит букву ').upper()
    if not word.check_letter(inp_letter):
        continue
    word.try_letter(inp_letter)

    if inp_letter in word.hidden_word:
        print(f'Вы угадали букву {inp_letter}!')
    else:
        print(f'Вы ошиблись, буквы {inp_letter} нет в слове.')

    print(f'{word.hidden_word}\n'
          f'Вы называли буквы: {word.trying_letters}\n'
          f'Осталось попыток: {word.faults}')

    if word.check_win():
        print(f'Поздравляем, вы победили!\n'
              f'Хотите сыграть еще?')
        word = next_game()
        continue

    if word.check_defeat():
        print(f'Вы проиграли.\n'
              f'Загаданное слово: {word.word}\n'
              f'Хотите сыграть еще?')
        word = next_game()
        continue