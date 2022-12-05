import random


class Bot:

    @staticmethod
    def move(candies: int, max_candies):
        better_move = candies % (max_candies + 1)
        if better_move == 0:
            return random.randint(0, max_candies)
        else:
            return candies % (max_candies + 1)
