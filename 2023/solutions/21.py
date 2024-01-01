grid = [list(r) for r in [line.rstrip('\n') for line in open("inputs/21.txt")]]
xsize = len(grid[0])
ysize = len(grid)

for i in range(64):
    L = []
    for y in range(ysize):
        for x in range(xsize):
            if grid[y][x] == "O" or grid[y][x] == "S":
                L.append((y,x))
    for py, px in L:
        for yy, xx in [[-1,0],[0,1],[1,0],[0,-1]]:
            ny, nx = py + yy, px + xx
            if 0 <= ny < ysize and 0 <= nx < xsize: 
                if grid[ny][nx] == ".":
                    grid[ny][nx] = "O"
        grid[py][px] = "."

print(sum(1 for row in grid for cell in row if cell == "O"))