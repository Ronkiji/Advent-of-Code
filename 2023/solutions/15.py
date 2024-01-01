from collections import defaultdict
inputs = [line.rstrip('\n') for line in open("inputs/15.txt")][0].split(",")

def hash(st):
    cur = 0
    for s in st:
        cur = (cur + ord(s)) * 17 % 256
    return cur

print(sum(hash(x) for x in inputs))

d =  defaultdict(list)

for string in inputs:
    last = string[-1]
    if last.isdigit(): st = string[:-2]
    else: st = string[:-1]
    
    label = hash(st)
    found = -1
    for index, (x, _) in enumerate(d[label]):
        if x == st:
            found = index
    if last.isdigit():
        if found != -1:
            d[label][found] = (st, int(last))
        else:
            d[label].append((st, int(last)))
    else:
        if found != -1:
            d[label].pop(found)

p2 = 0
for n in d:
    for i, len in enumerate(d[n]):
        p2 += (n + 1) * (i + 1) * len[1]

print(p2)
