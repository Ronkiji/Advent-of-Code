# part 2

inputs = []
current = ''
numPpl = 0
for line in open("inputs/day06.txt"):
  line = line.rstrip('\n')
  if line != '':
    current += line
    numPpl += 1
  elif line == '':
    current = current.rstrip('\n')
    inputs.append([current, numPpl])
    current = ''
    numPpl = 0
if current != '': inputs.append([current, numPpl])

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sumCount = []

for line in inputs:
  count = 0
  for char in alphabet:
    if line[0].count(char) == line[1]:
      count += 1
  sumCount.append(count)

print(sum(sumCount))

# part 1
# inputs = []
# current = ''
# for line in open("inputs/day6.txt"):
#   line = line.rstrip('\n')
#   if line != '':
#     current += line
#   elif line == '':
#     current = current.rstrip('\n')
#     inputs.append(current)
#     current = ''
# if current != '': inputs.append(current)

# print(inputs)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# sumCount = []

# for line in inputs:
#   count = 0
#   for char in alphabet:
#     if char in line:
#       count += 1
#   sumCount.append(count)

# print(sum(sumCount))