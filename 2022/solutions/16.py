inputs = [line.rstrip('\n') for line in open("inputs/16.txt")]

valves = {}

for line in inputs:
    parts = line.split(' ')
    v = parts[1]
    r = int(parts[4][5:-1])
    print(parts[9:])
    to = [valve[:2] for valve in parts[9:]]
    print(to)
    valves[v] = (r, to)

print(valves)
totals = []

import copy
def dfs(start, time, path):
    # print("enter " + start)
    if time < 0:
        # print(path)
        return sum(p for p in path)
    
    path.append(time * valves[start][0])
    # print("path ", path)
    totals = []
    for n in valves[start][1]:
        totals.append(dfs(n, time-2, path[:]))
    # print(start, totals)
    return max(totals)        
    
print(dfs("AA", 30, []))