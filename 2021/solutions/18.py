inputs = []
for line in open("inputs/day18.txt"):
  line = '(' + line.rstrip('\n').replace(' ', '') + ')'
  inputs.append(line)
sums = []

def evaluate(line, pos):
  val = 0
  cur = '+'
  lim1 = 0
  lim2 = 0
  for x in range(pos + 1, len(line)):
    if (lim1 < x <= lim2) == False:
      if line[x].isnumeric():
        val = eval('val' + cur + 'int(line[x])')
      elif line[x] == '*' or line[x] == '+':
        cur = line[x]
      elif line[x] == ')':
        return val, x
      else:
        value, lim2 = evaluate(line, x)
        lim1 = x
        val = eval('val' + cur + 'value')
    elif x >= len(line):
      return val, x
  return None

for line in inputs:
  value, limit = evaluate(line, 0)
  sums.append(value)

print(sum(sums))