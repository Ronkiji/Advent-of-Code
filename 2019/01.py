content = [(line.rstrip('\n')) for line in open("inputs/01.txt")]

import math

# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2

# part 1
# fuel = 0
# for x in content:
#   fuel += math.floor(int(x)/3) -2
# print(fuel)

# part 2
f = 0
for x in content:
  cfuel = int(x)
  while 1==1:
    fuel = math.floor(cfuel/3) - 2
    if fuel <= 0:
      break
    else:
      f += fuel
      cfuel = fuel
print(f)

