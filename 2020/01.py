inputs = [int(line.rstrip('\n')) for line in open("inputs/day01.txt")]
for a in inputs:
  for b in inputs:
    for c in inputs:
      if a + b + c == 2020:
        print(a * b * c)