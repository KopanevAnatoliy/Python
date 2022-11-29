# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

LEN = 11

arr = [random.random()*10 for _ in range(LEN)]
result = max(i % 1 for i in arr) - min(i % 1 for i in arr)
print(result)