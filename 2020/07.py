
inputs = {}
for line in open("inputs/day07.txt"):
  line = line.rstrip('.\n')
  large, small = line.split(' bags contain ')
  current = {}
  if 'no other bags' in small:
    small = ''
  elif ', ' in small:
    small = small.split(', ')
    for x in small:
      x = x.replace(' bags', '')
      x = x.replace(' bag', '')
      val = x[0:1]
      color = x[2:]
      current[color] = int(val)
  else:
    small = small.replace(' bag', '')
    val = small[0:1]
    color = small[2:]
    current[color] = int(val)
  inputs[large] = current

print(inputs)