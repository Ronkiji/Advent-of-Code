inputs = [line.rstrip('\n') for line in open("inputs/23.txt")]

points = set()

for r, row in enumerate(inputs):
    for c, col in enumerate(list(row)):
        if col == "#":
            points.add((r, c))

dirs = {"N": [(-1, 0), (-1, -1), (-1, 1)],
        "S": [(1, 0), (1, -1), (1, 1)],
        "E": [(0, 1), (-1, 1), (1, 1)],
        "W": [(0, -1), (-1, -1), (1, -1)]}

from itertools import cycle

cycles = cycle([    ["N", "S", "W", "E"],
                    ["S", "W", "E", "N"],
                    ["W", "E", "N", "S"],
                    ["E", "N", "S", "W"]    ]) 

def check(p, direction):
    for d in dirs[direction]:
        if (p[0] + d[0], p[1] + d[1]) in points: return False
    return True

neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1,1)]

r = 0
while True:
    r += 1
    tocheck = set()
    directions = next(cycles)
    for p in points:
        for n in neighbors:
            if (p[0] + n[0], p[1] + n[1]) in points:
                tocheck.add(p)
                
    if len(tocheck) == 0:
        break
    
    valid = {}
    
    for p in tocheck:
        for d in directions:
            move = dirs[d][0]
            if check(p, d):
                if (p[0] + move[0], p[1] + move[1]) in valid:
                    valid.pop((p[0] + move[0], p[1] + move[1]))
                else:
                    valid[(p[0] + move[0], p[1] + move[1])] = p
                break

    for v in valid:
        rm = valid[v]
        points.remove(rm)
        points.add(v)
    
    if r == 10:
        pointscp = set(points)

min_x = min(point[0] for point in pointscp)
max_x = max(point[0] for point in pointscp)
min_y = min(point[1] for point in pointscp)
max_y = max(point[1] for point in pointscp)

area = (abs(max_x - min_x) + 1) * (abs(max_y - min_y) + 1)

print(area - len(points)) # part 1
print(r) # part 2