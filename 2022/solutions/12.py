from collections import deque
inputs = [line.rstrip('\n') for line in open("inputs/12.txt")]

grid = []

for line in inputs:
    l = [ord(c) - ord('a') + 1 for c in line]
    grid.append(l)

d = dict( (j,(x, y)) for x, i in enumerate(grid) for y, j in enumerate(i) )

source = d[-13]
target = d[-27]
grid[source[0]][source[1]] = 1 
grid[target[0]][target[1]] = 26 

def bfs(grid, source, target):
    q = deque()

    steps = 0
    q.append((steps, source[0], source[1]))

    visited = {(source[0], source[1])}

    while len(q) > 0:
        steps, row, col = q.popleft()
        for r, c in [(row + 1, col), (row, col + 1), (row, col - 1), (row - 1, col)]:
            
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                continue
            if (r, c) in visited:
                continue
            if grid[r][c] - grid[row][col] > 1:
                continue
            if r == target[0] and c == target[1]:
                return steps + 1 
            
            visited.add((r, c))
            q.append((steps+1, r, c))

# part 1
print(bfs(grid, source, target))


# part 2
allsteps = []

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 1:
            source = (x, y)
            allsteps.append(bfs(grid, source, target))

allsteps = [i for i in allsteps if i != None]

print(sorted(allsteps)[0])