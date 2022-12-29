with open("inputs/day10.txt") as fp:
    inputs = [int(line.rstrip('\n')) for line in fp.readlines()]
inputs.sort()

dif1 = 0
dif3 = 1

for x in range(len(inputs)):
  if x == 0:
    dif = inputs[x]
  else:
    dif = inputs[x] - inputs[x-1]
  
  if dif == 1:
    dif1 += 1
  elif dif == 3:
    dif3 += 1

print(dif1 * dif3)