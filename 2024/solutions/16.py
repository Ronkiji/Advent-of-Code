G = [line.rstrip('\n') for line in open("inputs/16.txt")]

from heapq import heappush, heappop, heapify
from collections import defaultdict

R, C = len(G), len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == "S":
            sr, sc = r, c
        elif G[r][c] == "E":
            er, ec = r, c

Q = [(0, sr, sc, 0)]
visited = set()

N = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while Q:
    cost, r, c, d = heappop(Q)
    
    if (r, c) == (er, ec):
        break
    
    if (r, c, d) in visited:
        continue

    visited.add((r, c, d))
    
    dr, dc = N[d]
    nr, nc = r + dr, c + dc
    if G[nr][nc] != "#":
        heappush(Q, (cost + 1, nr, nc, d))
    
    # both 90 degree rotations
    heappush(Q, (cost + 1000, r, c, (d + 1) % 4))
    heappush(Q, (cost + 1000, r, c, (d - 1) % 4))

print(cost)

Q = [(0, sr, sc, 0, [(sr, sc)])]  # (cost, row, col, direction, path)
heapify(Q)
tiles = set()

while Q:
    c, y, x, d, path = heappop(Q)

    if c > cost:
        continue

    if (y, x) == (er, ec):
        tiles.update(set(path))
        continue

    for i, (dy, dx) in enumerate(N):
        ny, nx = y + dy, x + dx

        if G[ny][nx] == "#": 
            continue
        if (ny, nx) in path:  
            continue

        if i == d: 
            c_new = c + 1
        else: 
            c_new = c + 1001
        if c_new > cost:
            continue

        heappush(Q, (c_new, ny, nx, i, path + [(ny, nx)]))

print(len(tiles))

# a more efficient solution by mrphlip
# CY = len(G)
# CX = len(G[0])

# G = [list(row) for row in G]
# sx = sy = ex = ey = None
# for y, row in enumerate(G):
# 	for x, c in enumerate(row):
# 		if c == "S":
# 			sx, sy = x, y
# 		elif c == "E":
# 			ex, ey = x, y
# G = [[c == "#" for c in row] for row in G]

# def solve():
# 	bests = {(sx, sy, 1, 0): 0}
# 	bestpaths = defaultdict(set)
# 	bestpaths[sx, sy, 1, 0] = {(sx, sy)}
# 	solved = set()
# 	todo = {(sx, sy, 1, 0)}
# 	while todo:
# 		x, y, dx, dy = min(todo, key=bests.__getitem__)
# 		todo.remove((x, y, dx, dy))
# 		solved.add((x, y, dx, dy))
# 		cost = bests[x, y, dx, dy]
# 		nx, ny = x + dx, y + dy
# 		i = 1
# 		while 0 <= nx < CX and 0 <= ny < CY and not G[ny][nx]:
# 			if (nx, ny, dx, dy) not in solved and ((nx, ny, dx, dy) not in bests or bests[nx,ny,dx,dy] > cost + i):
# 				bests[nx, ny, dx, dy] = cost + i
# 				bestpaths[nx, ny, dx, dy] = set(bestpaths[x, y, dx, dy])
# 				bestpaths[nx, ny, dx, dy].add((nx, ny))
# 				todo.add((nx, ny, dx, dy))
# 			elif (nx, ny, dx, dy) in bests and bests[nx,ny,dx,dy] == cost + i:
# 				bestpaths[nx, ny, dx, dy].update(bestpaths[x, y, dx, dy])
# 			nx += dx
# 			ny += dy
# 			i += 1
# 		rx, ry = dy, -dx
# 		if (x, y, rx, ry) not in solved and ((x, y, rx, ry) not in bests or bests[x,y,rx,ry] >= cost + 1000):
# 			bests[x, y, rx, ry] = cost + 1000
# 			bestpaths[x, y, rx, ry] = set(bestpaths[x, y, dx, dy])
# 			bestpaths[x, y, rx, ry].add((x, y))
# 			todo.add((x, y, rx, ry))
# 		elif (x, y, rx, ry) in bests and bests[x, y, rx, ry] == cost + 1000:
# 			bestpaths[x, y, rx, ry].update(bestpaths[x, y, dx, dy])
# 		rx, ry = -dy, dx
# 		if (x, y, rx, ry) not in solved and ((x, y, rx, ry) not in bests or bests[x,y,rx,ry] >= cost + 1000):
# 			bests[x, y, rx, ry] = cost + 1000
# 			bestpaths[x, y, rx, ry] = set(bestpaths[x, y, dx, dy])
# 			bestpaths[x, y, rx, ry].add((x, y))
# 			todo.add((x, y, rx, ry))
# 		elif (x, y, rx, ry) in bests and bests[x, y, rx, ry] == cost + 1000:
# 			bestpaths[x, y, rx, ry].update(bestpaths[x, y, dx, dy])
# 		if (ex, ey, -1, 0) in solved and (ex, ey, 1, 0) in solved and (ex, ey, 0, -1) in solved and (ex, ey, 0, 1) in solved:
# 			break
# 	#return min(bests[ex, ey, i, j] for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)])
# 	m = min(bests[ex, ey, i, j] for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)])
# 	n = set.union(*[bestpaths[ex, ey, i, j] for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)] if bests[ex, ey, i, j] == m])
# 	return m, len(n)

# print(solve())