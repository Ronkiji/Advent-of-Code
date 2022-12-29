def part2():
  inputs = []
  for line in open("inputs/day02.txt"):
    line = line.rstrip('\n')
    r, l, st = line.split(' ')
    r1, r2 = r.split('-')
    l = l.strip(':')
    inputs.append([int(r1), int(r2), l, st])
  count = 0
  for x in inputs:
    if (x[3][x[0]-1] == x[2]) ^ (x[3][x[1]-1] == x[2]):
      count += 1
  return count

print(part2())