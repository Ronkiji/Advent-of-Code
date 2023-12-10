inputs = [(line.rstrip('\n')) for line in open("inputs/04.txt")]
total = 0
d = {}
for i, line in enumerate(inputs):
    win, got = line.strip().split(": ")[1].split(" | ")
    win = win.split()
    got = got.split()
    d[i] = (1, [win, got])

for i in d:
    instances, vals = d[i]
    counter = 0
    points = 0
    for y in vals[0]:
        if y in vals[1]:
            counter += 1
            if points == 0:
                points = 1
            else: 
                points *= 2
    total += points
    for c in range(1, counter+1):
        if i+c in d.keys():
            x, y = d[i+c]
            d[i+c] = (x+instances, y)

scratches = 0
for i in d:
    scratches += d[i][0]
print(total)
print(scratches)