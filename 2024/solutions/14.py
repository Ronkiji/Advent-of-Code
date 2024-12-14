inputs = [line.rstrip('\n') for line in open("inputs/14.txt")]
R = []
for i in range(len(inputs)):
    pos, vel = inputs[i].split(" ")
    px, py = list(map(int,pos[2:].split(",")))
    x, y = list(map(int,vel[2:].split(",")))
    R.append((px, py, x, y))
rows, cols = 103, 101

def one(R):
    for t in range(100):
        
        R = [((px + x) % cols, (py + y) % rows, x, y) for px, py, x, y in R]

    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for px, py, vx, vy in R:
        grid[py][px] += 1

    mid_row, mid_col = rows // 2, cols // 2

    q1 = sum(grid[r][c] for r in range(0, mid_row) for c in range(mid_col + 1, cols))
    q2 = sum(grid[r][c] for r in range(0, mid_row) for c in range(0, mid_col))
    q3 = sum(grid[r][c] for r in range(mid_row + 1, rows) for c in range(0, mid_col))
    q4 = sum(grid[r][c] for r in range(mid_row + 1, rows) for c in range(mid_col + 1, cols))

    T = q1 * q2 * q3 * q4

    print(T)

def two(R):
    for t in range(20000):
        
        R = [((px + x) % cols, (py + y) % rows, x, y) for px, py, x, y in R]

        # determined by judging the grid
        if sum(1 for px, _, _, _ in R if px == 23) > 20:

            grid = [[0 for _ in range(cols)] for _ in range(rows)]
            for px, py, vx, vy in R:
                grid[py][px] += 1

            with open("solutions/14_states.txt", "a") as f:
                f.write(f"{t + 1}\n")
                for row in grid:
                    f.write("".join(str(cell) if cell > 0 else "." for cell in row) + "\n")
                f.write("\n") 

one(R[::])
two(R[::])

