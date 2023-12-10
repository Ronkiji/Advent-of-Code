inputs = [line.rstrip('\n') for line in open("inputs/08.txt")]

from itertools import cycle
import math

cycle = cycle(inputs[0])
data = {}
for line in inputs[2:]:
    key, elem = line.split(" = ")
    data[key] = elem[1:-1].split(", ")

def find(e, s):
    c = 0
    while not e.endswith(s):
        move = next(cycle)
        e = data[e][1] if move == 'R' else data[e][0]
        c += 1
    return c

print(find("AAA", "ZZZ")) # part 1
ans = [find(e, "Z") for e in data if e.endswith("A")]
print(math.lcm(*ans)) # part 2