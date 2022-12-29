inputs = [line.rstrip('\n') for line in open("inputs/14.txt")]

visited = set()

lowest = {}

def lows(coord):
    if coord[0] in lowest.keys():
        if coord[1] >  lowest[coord[0]]:
            lowest[coord[0]] = coord[1]
    else:
        lowest[coord[0]] = coord[1]
    

for line in inputs:
    pairs = line.split(" -> ")
    tx, ty = pairs[0].split(",")
    tx, ty = int(tx), int(ty)
    visited.add((tx, ty))
    lows((tx, ty))
    for p in pairs[1:]: 
        x, y = p.split(",")
        x, y = int(x), int(y)
        diffx, diffy = abs(x - tx), abs(y - ty)
        if diffy != 0:
            for d in range(diffy):
                ty = ty + 1 if y > ty else ty - 1
                visited.add((tx, ty))
                lows((tx,ty))
        if diffx != 0:
            for d in range(diffx):
                tx = tx + 1 if x > tx else tx - 1
                visited.add((tx, ty))
                lows((tx,ty))
        tx, ty = x, y


def one(visited):
    counter = 0

    while True:
        sand = (500, 0)
        while True:
            if sand[0] not in lowest.keys() or lowest[sand[0]] < sand[1]:
                print(counter)
                return
            if (sand[0], sand[1] + 1) not in visited:
                sand = (sand[0], sand[1] + 1)
                continue
            if (sand[0] - 1, sand[1] + 1) not in visited:
                sand = (sand[0] - 1, sand[1] + 1)
                continue
            if (sand[0] + 1, sand[1] + 1) not in visited:
                sand = (sand[0] + 1, sand[1] + 1)
                continue
            visited.add(sand)
            counter += 1
            break

def two(visited):
    counter = 0
    while (500, 0) not in visited:
        sand = (500, 0)
        while True:
            if sand[1] > max(lowest.values()):
                break
            if (sand[0], sand[1] + 1) not in visited:
                sand = (sand[0], sand[1] + 1)
                continue
            if (sand[0] - 1, sand[1] + 1) not in visited:
                sand = (sand[0] - 1, sand[1] + 1)
                continue
            if (sand[0] + 1, sand[1] + 1) not in visited:
                sand = (sand[0] + 1, sand[1] + 1)
                continue
            break
        visited.add(sand)
        counter += 1

    print(counter)

one(visited.copy())
two(visited.copy())