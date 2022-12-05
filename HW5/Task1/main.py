# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

from game import Game
from bot import Bot


def y_n() -> bool:
    while True:
        answer = input('(Y/N)?\n').lower()
        if answer == 'y' or answer == 'yes':
            return True
        elif answer == 'n' or answer == 'no':
            return False
        print('Incorrect input.')


def play_with_bot() -> bool:
    print("Do you want play with bot")
    return y_n()


def game_info(game: Game) -> None:
    print(f"There are {game.candies} candies on the table")
    print(f"{'Player_1' if game.turn == 0 else 'Player_2'}'s move")
    print(f"You can take {game.max_candies} candies")


def move_info(game: Game, candies: int) -> None:
    print(f"{'Player_1' if game.turn == 0 else 'Player_2'} take {candies}")


def enter_numb(game: Game) -> int:
    while True:
        number = input(f'Enter a number between 1 and {game.max_candies}. \n').lower()
        if number == 'help':
            better_move = game.candies % (game.max_candies + 1)
            if better_move != 0:
                print(f"You must take {better_move} candies")
            else:
                print("You can't influence the game")
            continue
        if number.isdigit() and int(number) > 0 and int(number) <= game.max_candies:
            return int(number)


def end(game: Game):
    print(f"{'Player_1' if game.turn == 0 else 'Player_2'} won")


while True:
    game = Game(120)
    while game.game_status:
        if not game.turn:
            game_info(game)
            candies = enter_numb(game)
        else:
            candies = Bot.move(game.candies, game.max_candies)
        move_info(game, candies)
        game.take_sweets(candies)

    end(game)
    print('Do yow want play more?')
    if y_n():
        continue
    break
