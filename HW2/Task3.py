# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

import random
from functools import reduce

n = int(input("Введите число: "))
seq = list(range(-n, n + 1))
indexes = [random.randint(0,n * 2) for _ in range(5)]
print( reduce(lambda x, y: x*y, [seq[i] for i in indexes]) )