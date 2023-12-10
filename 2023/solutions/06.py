input = [line.rstrip('\n') for line in open("inputs/06.txt")]

time = [int(i) for i in input[0].split(":")[1].split()]
dist = [int(i) for i in input[1].split(":")[1].split()]

total = 1

for i in range(len(time)):
    beat = dist[i]
    for x in range(time[i]):
        if x * (time[i]-x) > beat:
            total *= (time[i]-x) - x  + 1
            break

print(total)

time = int(input[0].split(":")[1].replace(" ", ""))
dist = int(input[1].split(":")[1].replace(" ", ""))
for x in range(time):
    if x * (time-x) > dist:
        print((time-x) - x  + 1)
        quit()