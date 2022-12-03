# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.(Вывод тех элементов, которые были без повторов)

# Ввод: 1 2 3 2 4 4
# Вывод: 1 3

from collections import Counter
seq = [1, 2, 3, 2, 4, 4]
cnt = Counter(seq)
print([i for i in cnt if cnt[i] == 1])