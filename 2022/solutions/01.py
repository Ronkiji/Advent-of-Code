inputs = [line.rstrip('\n') for line in open("inputs/01.txt")]

# part 1
snacks = []
counter = 0
for x in inputs:
    if x != "":
        counter += int(x)
    else:
        snacks.append(counter)
        counter = 0

# part 1
print(max(snacks))

# part 2
snacks.sort(reverse=True)
print(snacks[0] + snacks[1] + snacks[2])