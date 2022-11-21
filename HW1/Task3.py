# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите X: "))
y = int(input("Введите Y: "))
if x == 0 or y == 0:
    raise Exception("x,y must be not null")
if x > 0:
    if y > 0:
        print("1-ая четверть.")
    else:
        print("2-ая четверть.")
elif y > 0:
        print("4-ая четверть.")
else:
    print("3-ая четверть.")

