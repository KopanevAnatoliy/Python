# Вычислить число Pi c заданной точностью d, не используя ф. round()

# Пример:

# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

import math

d = 0.000001

print( float(str(int(math.pi)) + "." + str(int(math.pi % 1 // d))) )