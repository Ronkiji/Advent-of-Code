from collections import deque
lines = [line.rstrip('\n') for line in open("inputs/18.txt")]

b = 1024
start = (0, 0)
goal = (70, 70) 
size = 71 

def bfs(corrupt):
    visited = set((0,0))
    Q = deque([(0,0,0)])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    while Q:
        x, y, dist = Q.popleft()
        if (x,y) == goal:
            return dist
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                if (ny,nx) not in corrupt and (ny,nx) not in visited:
                    visited.add((ny,nx))
                    Q.append((nx, ny, dist+1))
    return False

# part 1
corrupt = set()
for line in lines[:b]: 
    x, y = map(int, line.split(","))
    corrupt.add((x,y))
print(bfs(corrupt))

# part 2
corrupt = set()
for line in lines: 
    x, y = map(int, line.split(","))
    corrupt.add((x,y))
    if bfs(corrupt) == False:
        print(f"{x},{y}")
        break