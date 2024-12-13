from math import gcd

inputs = [line.rstrip('\n') for line in open("inputs/13.txt")]
P = []
for i in range(0, len(inputs), 4):
    ax, ay = inputs[i].split(": ")[1].split(", ")
    ax, ay = int(ax[2:]), int(ay[2:])
    bx, by = inputs[i+1].split(": ")[1].split(", ")
    bx, by = int(bx[2:]), int(by[2:]) 
    px, py = inputs[i+2].split(": ")[1].split(", ")
    px, py = int(px[2:]), int(py[2:])
    P.append((ax, ay, bx, by, px, py))

def one(ax, ay, bx, by, px, py):
    cost = float('inf')
    for a in range(101):
        for b in range(101):
            if a * ax + b * bx == px and a * ay + b * by == py:
                cost = min(cost, a * 3 + b * 1)
    return cost if cost != float('inf') else 0
                
def two(ax, ay, bx, by, px, py):
    # googled solution, had to go bed
    # a * ax + b * bx = px
    # a * ay + b * by = py
    A = ax * py - px * ay
    B = ax * by - bx * ay
    if A % B != 0:
        return None
    
    b = A // B
    C = px - b * bx
    D = ax
    
    if C % D != 0:
        return None
    a = C // D
    if a >= 0 and b >= 0:
        return (a, b)
    return None


T1, T2 = 0, 0
for ax, ay, bx, by, px, py in P:
    T1 += one(ax, ay, bx, by, px, py)
    s = two(ax, ay, bx, by, px + 10000000000000, py + 10000000000000)
    if s:
        a, b = s
        T2 += 3 * a + b

print(T1)
print(T2)
