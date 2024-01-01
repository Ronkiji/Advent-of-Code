from collections import deque, defaultdict
inputs = [line.rstrip('\n') for line in open("inputs/16.txt")]
ysize = len(inputs)
xsize = len(inputs[0])

neighbors = [(1, 0), # down
             (-1, 0), # up
             (0, 1), # right
             (0, -1)] # left

d = {
     ((0, 1), "|"):((-1, 0), (1, 0)),
     ((0, -1), "|"):((-1, 0), (1, 0)),
     ((-1, 0), "-"):((0, -1), (0, 1)),
     ((1, 0), "-"):((0, -1), (0, 1)),
     ((1, 0), "/"): [(0, -1)],
     ((0, 1), "/"): [(-1, 0)],
     ((-1, 0), "/"): [(0, 1)],
     ((0, -1), "/"): [(1, 0)],
     ((0, -1), "\\"): [(-1, 0)],
     ((1, 0), "\\"): [(0, 1)],
     ((0, 1), "\\"): [(1, 0)],
     ((-1, 0), "\\"): [(0, -1)]}

high = 0

def find(q):
    visited = set()
    
    poss = set()
    while q:
        pos, move = q.popleft()
        if (pos, move) in visited:
            continue
        visited.add((pos, move))
        poss.add(pos)   
        new = (pos[0] + move[0], pos[1] + move[1])
        if 0 <= new[0] and ysize > new[0] and 0 <= new[1] and xsize > new[1]:
            
            char = inputs[new[0]][new[1]]
            if (move, char) in d:
                moves = d[(move, char)]
                for m in moves:
                    q.append((new, m))
            else:
                q.append((new, move))
    return len(poss) - 1

print(find(deque([((0, -1), (0, 1))]))) # p1

for y in range(ysize):
    high = max(high, find(deque([((y, -1), (0, 1))])))
    high = max(high, find(deque([((y, xsize), (0, -1))])))

for x in range(xsize):
    high = max(high, find(deque([((-1, x), (1, 0))])))
    high = max(high, find(deque([((ysize, x), (-1, 0))])))

print(high) # p2

