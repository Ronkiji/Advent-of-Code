from collections import deque

valves = {}
tunnels = {}

for line in open("inputs/16.txt"):
    line = line.strip()
    valve = line.split()[1]
    flow = int(line.split(";")[0].split("=")[1])
    targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
    valves[valve] = flow
    tunnels[valve] = targets

dists = {}
nonempty = []

for valve in valves:
    if valve != "AA" and not valves[valve]:
        continue
    
    if valve != "AA":
        nonempty.append(valve)

    dists[valve] = {valve: 0, "AA": 0}
    visited = {valve}
    
    queue = deque([(0, valve)])
    
    while queue:
        distance, position = queue.popleft()
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if valves[neighbor]:
                dists[valve][neighbor] = distance + 1
            queue.append((distance + 1, neighbor))

    del dists[valve][valve]
    if valve != "AA":
        del dists[valve]["AA"]
    
indices = {}

for index, element in enumerate(nonempty):
    indices[element] = index

print(valves)
print()
print(tunnels)
print()
print(dists)
print()
print(nonempty)
print()
print(indices)