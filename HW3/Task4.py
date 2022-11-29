# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def to_bit(n):    

    result = []
    while True:
        if n / 2 == 0:
            break
        step = n % 2
        if step == 0:
            result.append("0")
        else:
            result.append("1")
        n //= 2
    return "".join(result[::-1])

print(to_bit(20))