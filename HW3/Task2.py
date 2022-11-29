# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
import numpy as np

N = 9
LEN = 11

arr = [random.randint(0, N) for _ in range(LEN)]
result = np.array(arr)[len(arr) // 2 :] * np.array(arr)[: (len(arr) + 1) // 2]
print(result)