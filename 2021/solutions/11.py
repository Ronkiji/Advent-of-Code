inputs = []
for line in open("inputs/day11.txt"):
  line = line.rstrip('\n')
  inputs.append(line)

def new(inputs, x, y):

  around = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x + 1, y], [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]

  if inputs[x][y] == 'L':
    for e in around:
      if 0 <= e[0] < len(inputs) and 0 <= e[1] < len(inputs[0]):
        if inputs[e[0]][e[1]] == '#':
          return 'L'
    return '#'
  
  elif inputs[x][y] == '#':
    count = 0
    for e in around:
      if 0 <= e[0] < len(inputs) and 0 <= e[1] < len(inputs[0]):
        if inputs[e[0]][e[1]] == '#':
          count += 1
    if count >= 4:
      return 'L'
    else: 
      return '#'
  
  else:
    return '.'

dup = []
loop = 0

while True:
  string = ''
  
  for x in range(len(inputs)):
    for y in range(len(inputs[0])):
      string += new(inputs, x, y)
    dup.append(string)
    string = ''
  
  loop += 1
  
  if inputs == dup:
    break
  
  inputs = dup
  dup = []
  
occ = 0
for row in inputs:
  occ += row.count('#')

print(occ)