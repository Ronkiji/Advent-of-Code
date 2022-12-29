inputs = [line.rstrip('\n') for line in open("inputs/22.txt")]

grid = inputs[:-2]

import re
pattern = r'\d+|[A-Za-z]'
directions = [match.group(0) for match in re.finditer(pattern, inputs[-1])]

points = {}

for i, r in enumerate(grid):
    for j in range(len(r)):
        if r[j] != " ": points[i+1, j+1] = r[j]


rows, cols = len(grid) + 2, len(grid[0]) + 2

ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "%": lambda x, y: x % y,
    "**": lambda x, y: x ** y
}

cur = None
for x in range(1, cols):
    if (1, x) in points: 
        cur = (1, x)
        break

def move(first, second, op, cur, m, bound):
    while (m != 0):
        temp = (cur[0] + first[0], cur[1] + first[1])
        if temp in points and points[temp] != '#':
            cur = temp
            m -= 1
            continue
        elif temp in points and points[temp] == '#':
            m = 0
            continue
        else: 
            x = bound
            temp = (cur[0], x) if second == True else (x, cur[1])
            while temp not in points:
                x = ops[op](x, 1)
                temp = (cur[0], x) if second == True else (x, cur[1])
            if points[temp] == '#':
                m = 0
                continue
            else:
                cur = temp
                m -= 1
                continue
        m = 0
    return cur 
        
face = 0
for d in directions:
    if d.isdigit():
        m = int(d)
        if   face == 0: cur = move((0, 1), True, '+', cur, m, 0)
        elif face == 2: cur = move((0, -1), True, '-', cur, m, cols)
        elif face == 1: cur = move((1, 0), False, '+', cur, m, 0)
        elif face == 3: cur = move((-1, 0), False, '-', cur, m, rows)
    else:
        if d == 'R': face = (face + 1) % 4
        elif d == 'L': face = (face - 1) % 4
    
print(1000 * cur[0] + 4 * cur[1] + face)