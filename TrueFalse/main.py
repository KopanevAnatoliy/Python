from typing import Optional

from game import TrueFalse


def difficult() -> int:
    while True:
        print('Enter the number of allowed mistakes')
        temp = input()
        try:
            numb = int(temp)
        except ValueError:
            print('Error: you entered not number')
        else:
            if numb > 0:
                return numb
            else:
                print('Error: you entered negative number')
                continue


def y_n() -> bool:
    while True:
        answer = input('(Y/N)?').lower()
        if answer == 'y' or answer == 'yes':
            return True
        elif answer == 'n' or answer == 'no':
            return False
        print('Incorrect input')


def path() -> Optional[str]:
    print(f'Do you want to change questions?')
    if y_n():
        print('Enter the directory.')
        return input()
    else:
        return None


print("Let's play a game TrueFalse")

game = TrueFalse(difficult(), path())

while game.game_status() is None:
    question, answer, info = game.get_answer()
    print(f'{question} \n'
          f"It's True?")
    player_answer = y_n()
    game.give_an_answer(player_answer)
    if player_answer == answer:
        print(f"You answered right, it's {answer}")
    else:
        print(f"You answered wrong, it's {answer}")
    print(f"{info}")

    if game.game_status() is True:
        print(f'Congratulations! You have answered all the questions')
    elif game.game_status() is False:
        print(f'You lose.')
    else:
        continue

    print(f'Do you want to play more?')
    if y_n():
        game = TrueFalse(difficult(), path())