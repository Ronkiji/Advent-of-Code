inputs = [(line.rstrip('\n')) for line in open("inputs/02.txt")]
total1, total2 = 0, 0
for line in inputs:
    playable = True
    r, g, b = 0, 0, 0
    parts = line.strip().split(":")
    sets = parts[1].split(";")
    for set in sets:
        colours = set.split(",")
        for cs in colours:
            n, c = cs.split()
            n = int(n)

            # part 1
            if c == 'red' and n > 12:
                playable = False
            elif c == 'green' and n > 13:
                playable = False
            elif c == 'blue' and n > 14:
                playable = False

            # part 2
            if c == 'red' and n > r:
                r = n
            elif c == 'green' and n > g:
                g = n
            elif c == 'blue' and n > b:
                b = n
    
    id = int(parts[0].split(" ")[1])
    if playable == True:
        total1 += id
    total2 += r * g * b
    
print(total1, total2)