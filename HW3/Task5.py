# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = 9

def get_fibo_seq():
    result = []
    for i in range(k):
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        else:
            result.append(result[i-1] + result[i-2])
    return result

seq = get_fibo_seq()
result = [-seq[i] if i % 2 == 0 else seq[i] for i in range(k)][:0:-1] + seq
print(result)