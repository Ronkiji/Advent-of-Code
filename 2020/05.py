inputs = []
mapping = [['F', '0'], ['B', '1'], ['L', '0'], ['R', '1']]

for line in open("inputs/day05.txt"):
  line = line.rstrip('\n')
  # y = line[0 : 7]
  # x = line[7 :]
  inputs.append(line)

binInputs = []

for line in inputs:
  binary = ''
  for char in line:
    if char == 'F' or char == 'L':
      binary += '0'
    elif char == 'B' or char == 'R':
      binary += '1'
  
  binInputs.append(binary)

seatId = []

for line in binInputs:
  y = int(line[0 : 7], 2)
  x = int(line[7 :], 2)
  seatId.append(y * 8 + x)

seatId.sort()
print(seatId[-1])

for x in range(len(seatId)):
  if x != len(seatId) - 1:
    if seatId[x] - seatId[x+1] == -2:
      print(seatId[x] + 1)