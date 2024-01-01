import heapq
grid = [[int(x) for x in line.rstrip('\n')] for line in open("inputs/17.txt")]

rows = len(grid)
cols = len(grid[0])

def find(p):
    q = [(0,0,0,-1,-1)]
    d = {}
    while q:
        dist, row, col, move, s = heapq.heappop(q)
        if (row, col, move, s) in d:
            continue
        d[(row,col,move,s)] = dist
        for i, (x, y) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
            r = row + x
            c = col + y
            new = i
            steps = (1 if new != move else s + 1)
            
            if not (new + 2) % 4 != move:
                continue
            if p == 1 and not (steps <= 3): # part 1
                continue
            if p == 2 and not (steps <= 10 and (new == move or s>=4 or s==-1)): # part 2
                continue

            if 0 <= r < rows and 0 <= c < cols:
                cost = int(grid[r][c])
                heapq.heappush(q, (dist + cost, r, c, new, steps))

    low = float('inf')
    for (row, col, _, s), distance in d.items():
        if row == rows - 1 and col == cols - 1:
            if p == 1: # part 1
                low = min(low, distance)
            elif p == 2 and s >= 4: # part 2
                low = min(low, distance)
    return low

print(find(1))
print(find(2))