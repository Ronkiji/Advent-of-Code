lines = [line.rstrip('\n') for line in open("inputs/21.txt")]
from collections import deque, defaultdict
from itertools import product

numpad = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2)
}

dirpad = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

N = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

npd = defaultdict(set)
dpd = defaultdict(set)

def bfs(start, target, keypad):    
    queue = deque([(start, "")])
    visited = {start: 0}  
    paths = []
    length = float('inf')

    while queue:
        current, sequence = queue.popleft()

        if len(sequence) > length:
            continue

        if current == target:
            if len(sequence) < length:
                paths = [sequence]
                length = len(sequence)
            elif len(sequence) == length:
                paths.append(sequence)
            continue

        for move, (dx, dy) in N.items():
            nx, ny = current[0] + dx, current[1] + dy
            next_pos = (nx, ny)
            if next_pos in keypad.values():
                path_length = len(sequence) + 1
                if next_pos not in visited or path_length <= visited[next_pos]:
                    visited[next_pos] = path_length
                    queue.append((next_pos, sequence + move))
    
    return paths

for _, i1 in numpad.items():
    for _, i2 in numpad.items():
        if i1 != i2:
            npd[(i1, i2)] = set(bfs(i1, i2, numpad))
        else:
            npd[(i1, i2)] = {""}

for _, i1 in dirpad.items():
    for _, i2 in dirpad.items():
        if i1 != i2:
            dpd[(i1, i2)] = set(bfs(i1, i2, dirpad))
        else:
            dpd[(i1, i2)] = {""}

def find(lines, dict, pad):
    results = []
    for code in lines:
        paths = [""]
        cur = ["A"]

        for char in code:
            next_paths = []
            next_positions = []
            for path, cur in zip(paths, cur):
                sequences = dict[(pad[cur], pad[char])]
                for seq in sequences:
                    next_paths.append(path + seq + "A")
                    next_positions.append(char)

            paths = next_paths
            cur = next_positions

        results.extend(paths)
    return results

T = 0
for code in lines:

    first = find([code], npd, numpad)
    second = find(first, dpd, dirpad)
    third = find(second, dpd, dirpad)

    short = min(len(item) for item in third)
    T += short * int(code.rstrip('A'))

print(T)

# not my solution for part 2
def two(dat):
    from functools import cache
    buttonlocs = ["789","456","123","_0A"]
    buttonlocs = {c: (x,y) for y, row in enumerate(buttonlocs) for x, c in enumerate(row)}
    buttonlocs2 = ["_^A","<v>"]
    buttonlocs2 = {c: (x,y) for y, row in enumerate(buttonlocs2) for x, c in enumerate(row)}

    @cache
    def doroute(frompos, topos, depth, badrow):
        if frompos[0] < topos[0]:
            horiz = ">" * (topos[0] - frompos[0])
        elif frompos[0] > topos[0]:
            horiz = "<" * (frompos[0] - topos[0])
        else:
            horiz = ""
        if frompos[1] < topos[1]:
            vert = "v" * (topos[1] - frompos[1])
        elif frompos[1] > topos[1]:
            vert = "^" * (frompos[1] - topos[1])
        else:
            vert = ""

        if horiz == "":
            opts = [vert]
        elif vert == "":
            opts = [horiz]
        elif frompos[0] == 0 and topos[1] == badrow:
            opts = [horiz + vert]
        elif topos[0] == 0 and frompos[1] == badrow:
            opts = [vert + horiz]
        else:
            opts = [horiz + vert, vert + horiz]

        def checkopts():
            for i in opts:
                yield routecode(i + "A", depth - 1, True)
        return min(checkopts())

    def routecode(code, depth, arrows):
        if depth <= 0:
            return len(code)
        locs = buttonlocs2 if arrows else buttonlocs
        badrow = 0 if arrows else 3
        pos = locs["A"]
        res = 0
        for i in code:
            newpos = locs[i]
            res += doroute(pos, newpos, depth, badrow)
            pos = newpos
        return res

    def go(depth):
        n = 0
        for i in dat:
            a = routecode(i, depth, False)
            #print(f"{i}: {a}")
            n += int(i[:-1]) * a
        return n
    print(go(26))

two(lines)


