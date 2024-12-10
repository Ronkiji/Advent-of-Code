def one(disk):
    compact = []
    for i in disk:
        if i != ".":
            compact.append(i)
        else:
            last = disk.pop()
            while last == ".":
                last = disk.pop()
            compact.append(last)
    return sum(i * c for i, c in enumerate(compact))

def two(disk):
    from itertools import groupby
    groups = [(key, len(list(group))) for key, group in groupby(disk)]
    compact = groups[::]
    for i in range(len(groups) - 1, 0, -1):
        x, y = groups[i]
        if x != ".":
            for j, (k, v) in enumerate(compact):
                if k == "." and v >= y:
                    if (x, y) in compact:
                        index = compact.index((x, y))
                        if index <= j: 
                            break
                        compact[index] = (".", y)
                    compact.pop(j)
                    if v - y > 0:
                        compact.insert(j, (".", v - y))
                    compact.insert(j, (x, y))
                    break

    result = []
    for value, count in compact:
        result.extend([value] * count)
    T = 0
    for i, r in enumerate(result):
        if r != ".":
            T += i * int(r)
    return T

line = [line.rstrip('\n') for line in open("inputs/09.txt")][0]
disk = []
for i, n in enumerate(line):
    char = i // 2 if i % 2 == 0 else "."
    for _ in range(int(n)):
        disk.append(char)

print(one(disk[::]))
print(two(disk[::]))






