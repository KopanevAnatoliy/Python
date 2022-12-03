# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# 24
# 2 2 2 3

def to_simple(n, nd = 2):
    for i in range(nd,n):
        if n % i == 0:
            return [i] + to_simple(int(n / i), nd = i)
    return [n]

print(to_simple(24))