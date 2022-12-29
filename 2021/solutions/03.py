inputs = []
for line in open("inputs/day03.txt"):
  line = line.rstrip('\n')
  inputs.append(line)

def part1():
  global inputs
  count = 0
  pos = -3

  for x in inputs:
    pos += 3
    if pos >= 31:
      pos -= 31
    if x[pos] == '#':
      count += 1
  return count

def part2():
  global inputs
  c1 = 0
  pos1 = -1

  for x in range(len(inputs)):
    pos1 += 1
    if pos1 >= 31:
      pos1 -= 31
    if inputs[x][pos1] == '#':
      c1 += 1

  c2 = 0
  pos2 = -3

  for x in range(len(inputs)):
    pos2 += 3
    if pos2 >= 31:
      pos2 -= 31
    if inputs[x][pos2] == '#':
      c2 += 1

  c3 = 0
  pos3 = -5

  for x in range(len(inputs)):
    pos3 += 5
    if pos3 >= 31:
      pos3 -= 31
    if inputs[x][pos3] == '#':
      c3 += 1

  c4 = 0
  pos4 = -7

  for x in range(len(inputs)):
    pos4 += 7
    if pos4 >= 31:
      pos4 -= 31
    if inputs[x][pos4] == '#':
      c4 += 1

  c5 = 0
  pos5 = -1

  for x in range(len(inputs)):
    if x == 0 or x % 2 == 0:
      pos5 += 1
      if pos5 >= 31:
        pos5 -= 31
      if inputs[x][pos5] == '#':
        c5 += 1
  
  return c1 * c2 * c3 * c4 * c5

print(part1())
print(part2())