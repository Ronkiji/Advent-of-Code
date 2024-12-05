from collections import defaultdict
inputs = [line.rstrip('\n') for line in open("inputs/05.txt")]
D = defaultdict(set)
L = []
B = True

for line in inputs:
    if line == "":
        B = False
        continue

    if B:
        x, y = map(int, line.split("|"))
        D[x].add(y)
    else:
        L.append(list(map(int, line.split(","))))

def one():

    T = 0
    invalid = [] # this is for part two
    for l in L:
        valid = True
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                a, b = l[i], l[j]
                if b not in D[a]:
                    valid = False
                    break
            if not valid:
                invalid.append(l) # this is for part two
                break

        if valid:
            T += int(l[len(l) // 2])

    return T, invalid

def two(invalid):
    T = 0
    for inv in invalid:
        bad = set(inv)
        good = []
        while bad:
            for key in bad:
                # checks which number has no dependencies, and remove it
                # this is the last number in the 'correctly ordered' list
                if all(val not in bad for val in D[key]):
                    good.append(key)
                    bad.remove(key)
                    break
        good = good[::-1] # reverse it
        T += int(good[len(good) // 2])
    return T

T, invalid = one()
print(T)
print(two(invalid))



