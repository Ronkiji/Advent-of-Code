inputs = [line.rstrip('\n') for line in open("inputs/15.txt")]
from collections import deque
sensors = []
beacons = []
distances = []
visited = set()
ranges = []

for line in inputs:
    left, right = line.split(": closest beacon is at x=")
    x, y = left.split(", y=") 
    x, y = int(x[12:]), int(y)
    sensors.append((x,y))
    x, y = right.split(", y=")
    x, y = int(x), int(y)
    beacons.append((x, y))

def man_dis(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

for x in range(len(sensors)):
    distances.append(man_dis(sensors[x], beacons[x]))

def one():
    for i in range(len(sensors)):
        s = sensors[i]
        d = distances[i]
        key = 2000000
        if s[1] - d <= key <= s[1] + d:
            diff = d - abs(s[1] - key)       
            ranges.append((s[0] - diff, s[0] + diff))

    counter = 0
    visited = set()
    for r in ranges:
        for i in range(r[0], r[1] + 1):
            visited.add(i)

    for b in set(beacons):
        if b[1] == key and b[0] in visited:
            counter += 1

    print(len(visited) - counter)

def two():

    for i in range(len(sensors)):
        sx, sy, sd = sensors[i][0], sensors[i][1], distances[i]

        for outerx in range(sd + 2):
            outery = (sd+1) - outerx 
            for r, c in [(outerx, outery), (-outerx, outery), (outerx, -outery), (-outerx, -outery)]:
                nx, ny = sx + r, sy + c
                if 0 <= nx <= 4000000 and 0 <= ny <= 4000000:
                    found = True
                    for j in range(len(sensors)):
                        x, y, d = sensors[j][0], sensors[j][1], distances[j]
                        if man_dis((x, y), (nx, ny)) <= d:
                            found = False
                            break
                    if found:
                        print(nx * 4000000 + ny)
                        exit(0)

one()
two()