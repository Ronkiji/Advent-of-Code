inputs = [line.rstrip('\n') for line in open("inputs/03.txt")]

symbols = []
gears = {}
for r in range(len(inputs)):
    for c in range(len(inputs[0])):
        if inputs[r][c] not in "0123456789.":
            symbols.append((r,c))
        if inputs[r][c] == "*":
            gears[(r,c)] = []

neighbors = [
    (0, 1),(1, 0), (1, 1),(0, -1),(-1, 0),(-1, -1),(-1, 1),(1, -1)   
]
results = []

checked = set()
for r in range(len(inputs)):
    for c in range(len(inputs[0])):
        if (r,c) in checked:
            continue
        
        checked.add((r,c))
        if inputs[r][c].isdigit():
            pos = set()
            num = inputs[r][c]
            pos.add((r,c))
            c += 1
            if c >= len(inputs[0]):
                break
            checked.add((r,c))
            while inputs[r][c].isdigit():
                num += inputs[r][c]
                pos.add((r,c))
                c += 1
                checked.add((r,c))
                if c >= len(inputs[0]):
                    break
            found = False
            for (m,n) in pos:
                if found:
                    break
                for (x,y) in neighbors:
                    if (m+x, n+y) in symbols:
                        if (m+x, n+y) in gears:
                            gears[(m+x, n+y)].append(int(num))
                        results.append(int(num))
                        found = True
                        break
print(sum(results)) # part 1
sum2 = 0
for g in gears:
    if len(gears[g]) == 2:
        sum2 += gears[g][0] * gears[g][1]
print(sum2) # part 2
    