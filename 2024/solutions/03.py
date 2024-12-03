lines  = [line.rstrip('\n') for line in open("inputs/03.txt")]
import re

def one():
    P = r"mul\((\d{1,3}),(\d{1,3})\)"
    T = 0
    for L in lines:
        M = re.findall(P, L)
        T +=  sum(int(x) * int(y) for x, y in M)
    return T

def two():
    mul = r"mul\((\d{1,3}),(\d{1,3})\)"
    do = r"do\(\)"
    dont = r"don't\(\)"
    T = 0
    B = True  
    for L in lines:
        M = list(re.finditer(f"{mul}|{do}|{dont}", L))
        for m in M:
            if m.group(0) == "do()":
                B = True
            elif m.group(0) == "don't()":
                B = False
            elif m.group(1) and B:
                x, y = int(m.group(1)), int(m.group(2))
                T += x * y
    return T

print(one())
print(two())