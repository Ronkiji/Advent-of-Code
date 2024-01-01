grid = [list(line.rstrip('\n')) for line in open("inputs/11.txt")]

def solve(m):
    points = []
    xpand = [i for i in range(0, len(grid[0]))]
    ypand = [i for i in range(0, len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[x][y] == "#":
                points.append([x, y])
                if y in xpand:
                    xpand.remove(y)
                if x in ypand:
                    ypand.remove(x)

    while xpand:
        x = xpand.pop(0)
        for p in points:
            if p[1] >= x:
                p[1] += m
        xpand = sorted([v + m for v in xpand])
    while ypand:
        y = ypand.pop(0)
        for p in points:
            if p[0] >= y:
                p[0] += m
        ypand = sorted([v + m for v in ypand])
    
    d = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            p1, p2 = points[i], points[j]
            d += abs((p2[0] - p1[0])) + abs((p2[1] - p1[1]))
    return d

print(solve(1))
print(solve(999999))