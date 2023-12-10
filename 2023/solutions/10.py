inputs = [line.rstrip('\n') for line in open("inputs/10.txt")]
ysize = len(inputs)
xsize = len(inputs[0])
for i, s in enumerate(inputs):
    if "S" in s:
        S = [i, s.find("S")]

neighbors = {(1, 0):["|", "J", "L"], # down
             (-1, 0):["|", "F", "7"], # up
             (0, 1):["-", "7", "J"], # right
             (0, -1):["-", "F", "L"]} # left

d = {((-1, 0), "F"):(0, 1),
    ((0, -1), "F"):(1, 0),
    ((1, 0), "|"): (1, 0),
    ((-1, 0), "|"): (-1, 0),
    ((0, -1), "-"): (0, -1),
    ((0, 1), "-"): (0, 1),
    ((1, 0), "J"): (0, -1),
    ((0, 1), "J"): (-1, 0),
    ((0, -1), "L"): (-1, 0),
    ((1, 0), "L"): (0, 1),
    ((0, 1), "7"): (1, 0),
    ((-1, 0), "7"): (0, -1)}

for n in neighbors.keys():
    ns = (S[0] + n[0], S[1] + n[1])
    if 0 <= ns[0] < ysize and 0 <= ns[1] < xsize:
        if inputs[ns[0]][ns[1]] in neighbors[n]:
            move = n
            break

distance = 0
cur = S.copy()
loop = set()
while True:
    loop.add((cur[0], cur[1]))
    cur[0] += move[0]
    cur[1] += move[1]
    if cur == S:
        print(distance//2 + 1)
        break
    move = d[(move, inputs[cur[0]][cur[1]])]
    distance += 1

inside = 0

for y in range(ysize):
    enter = False
    for x in range(xsize):
        c = inputs[y][x]
        if (y, x) in loop and (c == '|' or c == '7' or c == 'F'):
            enter = not enter
        if (y, x) not in loop and enter:
            inside += 1

print(inside)