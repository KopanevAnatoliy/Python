# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from itertools import product
print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
[print(f"x = {x}, y = {y}, z = {z} {(not (x or y or z) == (not x and not y and not z))}") for x,y,z in product('01', repeat=3)]