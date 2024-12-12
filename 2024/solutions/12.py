G = [line.rstrip('\n') for line in open("inputs/12.txt")]
R, C = len(G), len(G[0])
visited = set()

N = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(s):
    Q = [s]
    V = set()

    while Q:
        y, x = Q.pop(0)
        V.add((y,x))

        for dy, dx in N:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < R and 0 <= nx < C):
                continue

            if (ny, nx) in V:
                continue

            if G[ny][nx] == G[y][x]:
                Q.append((ny, nx))
                V.add((ny, nx))

    # return all points of region based on starting point
    return V

def calculate(r):
    perim = 0
    from collections import defaultdict
    sides = defaultdict(list)
    for y, x in r:
        for dy, dx in N:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < R and 0 <= nx < C) or (ny, nx) not in r:
                perim += 1
                if dy != 0: # stores all x values on unique horizontal line
                    sides[("y", (dy/2) + y, y)].append(x)
                else: # stores all y values on unique vertical line
                    sides[("x", x + (dx/2), x)].append(y)

    S = len(sides)
    for l in sides.values():
        l.sort()
        for i in range(1, len(l)):
            if l[i] != l[i - 1] + 1:
                # if horizontal line has perim points on 2,3,4,6,7 theres actually two sides
                S += 1 

    return perim, S

regions = []

for y in range(R):
    for x in range(C):
        if (y,x) not in visited:
            region = bfs((y,x))
            visited.update(region)
            regions.append(region)

T1 = 0
T2 = 0
for region in regions:
    area = len(region)
    perimeter, sides = calculate(region) 
    T1 += area * perimeter
    T2 += area * sides

print(T1)
print(T2)