from collections import deque

inputs = [line.rstrip('\n') for line in open("inputs/18.txt")]

m = (100, 100, 100)
M = (-100, -100, -100)

plots = set()
for line in inputs:
    x, y, z = map(int, line.split(","))
    
    m = (min(m[0], x), min(m[1], y), min(m[2], z))
    M = (max(M[0], x), max(M[1], y), max(M[2], z))
    
    plots.add((x,y,z))
    
m = (m[0] - 1, m[1] - 1, m[2] - 1)
M = (M[0] + 1, M[1] + 1, M[2] + 1)

neighbors = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]

def one():
    edges = len(plots) * 6
    for p in plots:   
        for n in neighbors:
            if (p[0] + n[0], p[1] + n[1], p[2] + n[2]) in plots: edges -= 1

    print(edges)

def two():

    q = deque([(m[0], m[1], m[2])])
    surround = {(m[0], m[1], m[2])}
    
    while q:
        x, y, z = q.popleft()
        for n in neighbors:
            p = nx, ny, nz = x + n[0], y + n[1], z + n[2]
            if not (m[0] <= nx <= M[0] and m[1] <= ny <= M[1] and m[2] <= nz <= M[2]):
                continue
            if p in plots or p in surround:
                continue
            surround.add(p)
            q.append(p)
    
    def surfaces(cubes):
        offset = [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)]
        sf = set()
        for c in cubes:
            for o in offset:
                sf.add((c[0] + o[0], c[1] + o[1], c[2] + o[2]))
        return sf
    
    print(len(surfaces(plots) & surfaces(surround)))
    
one()
two()