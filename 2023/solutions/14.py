from collections import defaultdict
inputs = [line.rstrip('\n') for line in open("inputs/14.txt")]
rocks = set()
balls = []

for y, line in enumerate(inputs):
    for x, s in enumerate(line):
        if s == "#":
            rocks.add((y,x))
        elif s == "O":
            balls.append((y, x))

def roll(b):
    bs = []
    for _ in range(len(b)):
        y, x = b.pop(0)
        row = y
        while row >= 0 and (row, x) not in rocks and (row, x) not in bs:
            row -= 1
        bs.append((row + 1, x))
    return bs

######################################################
b1 = balls.copy()################### PART 1 ##########
b1 = roll(b1)#########################################
print(sum([len(inputs) - y for y, _ in b1]))##########
######################################################

def rotate(coords):
    return sorted([(x, len(inputs)-y-1) for y, x in coords])

state = defaultdict(bool)
index = -1
for i in range(1000000000):
    for _ in range(4):
        balls = roll(balls.copy())
        rocks = set(rotate(rocks))
        balls = rotate(balls.copy())
    h = hash(tuple(balls))
    if state[h]:
        index = (state[h], i)
        break
    else:
        state[h] = i

mod = (999999999 - index[0]) % (index[1]-index[0])

for i in range(mod):
    for _ in range(4):
        balls = roll(balls.copy())
        rocks = set(rotate(rocks))
        balls = rotate(balls.copy())

print(sum([len(inputs) - y for y, _ in balls])) # part 2
