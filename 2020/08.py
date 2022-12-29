inputs = []
for line in open("inputs/day08.txt"):
  line = line.rstrip('\n')
  op, arg = line.split(' ')
  inputs.append([op, arg])
  
print(inputs)

accum = 0
visited = []


def new(pos, op, arg):
  visited.append(pos)
  if op == 'acc':
    global accum
    accum += eval(arg)
    return pos + 1
  elif op == 'jmp':
    return pos + eval(arg)
  else:
    return pos + 1

print(inputs[1])

pos = 0

while True:
  upd = new(pos, inputs[pos][0], inputs[pos][1])
  if upd in visited:
    break
  else:
    pos = upd

print('Accumulator = ' + str(accum))