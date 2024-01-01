inputs = [line.rstrip('\n') for line in open("inputs/19.txt")]
b = False
from collections import defaultdict
W = defaultdict(list)
R = []
for line in inputs:
    if line == "":
        b = True
        continue
    if not b:
        T, M = line.split("{")
        flows = M[:-1].split(",")
        for f in flows:
            if ":" not in f:
                W[T].append([f])
                break
        
            # print(f)
            c, g = f.split(":")
            if ">" in c:
                l, r = c.split(">")
                W[T].append((l, r, g) )
            else:
                l, r = c.split("<")
                W[T].append((r, l , g))
    else:
        R.append(line[1:-1].split(","))

# print(R)

total = 0
for r in R:
    D = defaultdict(int)
    for z in r:
        x, n = z.split("=")
        D[x] = int(n)
    
    cur = "in"

    while cur != "A" and cur != "R":
        flows = W[cur]
        update = False
        for f in flows:
            if len(f) == 3:
                x, y, z = f
                if x.isdigit():
                    if D[y] < int(x):
                        cur = z
                        update = True
                else:
                    if D[x] > int(y):
                        
                        cur = z
                        update = True
            else:
                cur = f[0]
                update = True
            
            if update:
                break
    if cur == "A":
        total += sum(D.values())

print(total)
