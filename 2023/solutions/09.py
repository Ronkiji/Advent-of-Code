inputs = [line.rstrip('\n') for line in open("inputs/09.txt")]
p1, p2 = 0, 0

for line in inputs:
    s = [int(i) for i in line.split(" ")]
    d1, d2 = [s[-1]], [s[0]]
    cur= s
    c = 0
    while set(cur) != {0}:
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        d1.append(cur[-1])
        d2.append(cur[0])
    p1 += sum(d1)
    d2 = d2[::-1]
    sub = 0
    for n in d2[1:]:
        sub = n - sub
    p2 += sub
print(p1)
print(p2)