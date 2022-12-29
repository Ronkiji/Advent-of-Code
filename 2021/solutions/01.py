inputs = [int(line.rstrip('\n')) for line in open("inputs/day01.txt")]

def part2():
  for a in inputs:
    for b in inputs:
      for c in inputs:
        if a + b + c == 2020:
          return a * b * c

print(part2())