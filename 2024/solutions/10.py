G = [line.rstrip('\n') for line in open("inputs/10.txt")]
R, C = len(G), len(G[0])
from collections import defaultdict
S = []

for y in range(R):
    for x in range(C):
        if G[y][x] == "0":
            S.append((y,x))

N = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(s):
    Q = [s]
    V = set()
    dest = set()

    while Q:
        y, x = Q.pop(0)
        V.add((y,x))

        for dy, dx in N:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < R and 0 <= nx < C):
                continue

            if (ny, nx) in V:
                continue

            if int(G[ny][nx]) == int(G[y][x]) + 1:
                Q.append((ny, nx))
                V.add((ny, nx))
                
                if G[ny][nx] == "9":
                    dest.add((ny, nx))

    return len(dest)


def dfs(y, x, visited):
    if G[y][x] == "9":
        return 1
    
    count = 0
    visited.add((y, x))
    
    for dy, dx in N:
        ny, nx = y + dy, x + dx

        if not (0 <= ny < R and 0 <= nx < C):
            continue

        if (ny, nx) not in visited and int(G[ny][nx]) == int(G[y][x]) + 1:
            count += dfs(ny, nx, visited) 
    
    visited.remove((y, x)) # for backtracking
    return count

T1, T2 = 0, 0
for s in S:
    T1 += bfs(s)
    T2 += dfs(s[0], s[1], set())

print(T1)
print(T2)