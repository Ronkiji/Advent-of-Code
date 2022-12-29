inputs = [line.rstrip('\n') for line in open("inputs/24.txt")]

height, width = len(inputs) - 2, len(inputs[0]) - 2
start = (0, 1)
end = (height + 1, width)
blizz = {}

for i, r in enumerate(inputs):
    for j, c in enumerate(list(r)):
        if c != "." and c != "#":
            blizz[(i, j)] = [c]

blizzards = {0: blizz}


def moveblizz(blizz):
    new = {}
    for elem in blizz:
        bl = blizz[elem]
        for b in bl:
            
            if b == ">":
                n = (elem[0], elem[1] + 1)
                if n[1] > width: n = (elem[0], 1)
            elif b == "<":
                n = (elem[0], elem[1] - 1)
                if n[1] < 1: n = (elem[0], width)
            elif b == "^":
                n = (elem[0] - 1, elem[1])
                if n[0] < 1: n = (height, elem[1])
            elif b == "v":
                n = (elem[0] + 1, elem[1])
                if n[0] > height: n = (1, elem[1])
                
            if n not in new:
                new[n] = [b]
            else:
                new[n].append(b)
    return new

from collections import deque

def trip(start, end, steps, second=False):

    q = deque([(start, steps)])
    visited = set()
    while q:
        
        if second:
            print(q)
        
        node, steps = q.popleft()
        steps += 1
        
        if steps in blizzards:
            b = blizzards[steps]
        else:
            blizzards[steps] = moveblizz(blizzards[steps-1])
            b = blizzards[steps]
        
        for ne in [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]:
            n = (node[0] + ne[0], node[1] + ne[1])
            if (n, steps) in visited:
                continue
            if n == end:
                return steps
            if n in b:
                continue
            if not(0 < n[0] <= height and 0 < n[1] <= width) and n != start:
                continue
            visited.add((n, steps))
            q.append((n, steps))
    
first = trip(start, end, 0)
second = trip(end, start, first)
third = trip(start, end, second)
print(first)
print(third)