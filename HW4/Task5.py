# Дополнительное Даны два файла, в каждом из которых находится запись 
# многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Файл1: 2*x² + 4*x + 5

# Файл2: 41*x^3 + 6*x² + 2*x + 98

# Вывод Файл3: 41*x^3 + 8*x^2 + 6*x + 103

import re

def eq_split(string):    
    coef = dict()
    for i in string.split(" + "):
        match = re.findall("\d+",i)
        if len(match) > 1: 
            coef.update( {match[1] : int(match[0])} )
        if "x" in i:
            coef.update( {"1" : int(match[0])} )
        else:
            coef.update( {"0" : int(match[0])} )
    return coef

def eq_to_string(coef):
    return " + ".join(
        f"{v}" if k == "0" else
        f"{v}*x" if k == "1" else 
        f"{v}*x^{k}"
            for k, v in sorted(coef.items(), key=lambda x:x[0])[::-1])

def eq_sum(coef_1, coef_2):
    coef_1.update( {k : coef_1.get(k,0) + v for k,v in coef_2.items()} )
    return coef_1

def read_eq(path):
    with open(path, "r") as f:
        return f.read().strip()
    
def write_eq(path,string):
    with open(path, "w") as f:
        f.write(string)

files = ["a.txt", "b.txt"]
equations = map(read_eq, files)

result_equation = eq_to_string( eq_sum(*map(eq_split, equations)) )

write_eq("c.txt",result_equation)