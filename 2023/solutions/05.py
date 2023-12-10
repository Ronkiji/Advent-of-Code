inputs = [line.rstrip('\n') for line in open("inputs/05.txt")]
seeds = [int(i) for i in inputs[0].split(":")[1].split()]

maps = []
checked = set()

for i in range(1, len(inputs)):
    if i in checked or inputs[i] == "" or not inputs[i][0].isdigit():
        continue
    map = []
    c = 0
    while i + c < len(inputs) and inputs[i+c] != "" and inputs[i + c][0].isdigit():
        checked.add(i + c)
        map.append([int(x) for x in inputs[i+c].split()])
        c += 1
    maps.append(map)

def locate(pos):
    skips = float('inf')
    for map in maps:
        for (dest, src, n) in map:
            if pos >= src and pos < src + n:
                # how many we can skip over
                skips = min(skips, src + n - pos) 
                pos = dest + pos - src
                break

    return pos, skips

# part 1
low = float('inf')
for s in seeds:
    location, skips = locate(s)
    low = min(low, location)

print(low)

# part 2
low = float('inf')
for i in range(0, len(seeds), 2):
    seed, n = seeds[i], seeds[i+1]
    s = seed
    while s < seed + n:
        location, skips = locate(s)
        low = min(low, location)
        s += skips

print(low)
