from collections import defaultdict
G = [line.rstrip('\n') for line in open("inputs/08.txt")]
R, C = len(G), len(G[0])
D = defaultdict(list)
for y in range(R):
    for x in range(C):
        if G[y][x] != ".":
            D[G[y][x]].append((y,x))

anti1 = set()
anti2 = set()
for _, ants in D.items():
    for a in ants:
        # part 2
        anti2.add(a)
    for i in range(len(ants)):
        for j in range(i + 1, len(ants)):
            a1, a2 = ants[i], ants[j]
            y1, x1 = a1
            y2, x2 = a2
            dy, dx = y2 - y1, x2 - x1
            r1 = (y1 - dy, x1 - dx) 
            r2 = (y2 + dy, x2 + dx)
            
            # part 1
            if 0 <= r1[0] < R and 0 <= r1[1] < C:
                anti1.add(r1)
            if 0 <= r2[0] < R and 0 <= r2[1] < C:
                anti1.add(r2)

            # part 2
            while 0 <= r1[0] < R and 0 <= r1[1] < C:
                anti2.add(r1)
                r1 = (r1[0] - dy, r1[1] - dx)
            while 0 <= r2[0] < R and 0 <= r2[1] < C:
                anti2.add(r2)          
                r2 = (r2[0] + dy, r2[1] + dx)

print(len(anti1))
print(len(anti2))