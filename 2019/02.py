content = [(line.rstrip('\n')) for line in open("inputs/02.txt")]
content = content[0].split(",")
inputs = []
for x in content:
  inputs.append(int(x))

# part 1
# pos = 0
# while pos < len(inputs):
#   if inputs[pos] == 1:
#     pos1 = inputs[pos + 1]
#     pos2 = inputs[pos + 2]
#     pos3 = inputs[pos + 3]
#     inputs[pos3] = inputs[pos1] + inputs[pos2]
#   elif inputs[pos] == 2:
#     pos1 = inputs[pos + 1]
#     pos2 = inputs[pos + 2]
#     pos3 = inputs[pos + 3]
#     inputs[pos3] = inputs[pos1] * inputs[pos2]
#   else:
#     break
#   pos += 4
# print(inputs)
    
# part 2

original_inputs = inputs[:]

for x in range(100):
  for y in range(100):
    inputs = original_inputs[:]
    inputs[1] = x
    inputs[2] = y
    pos = 0
    while pos < len(inputs):
      if inputs[pos] == 1:
        pos1 = inputs[pos + 1]
        pos2 = inputs[pos + 2]
        pos3 = inputs[pos + 3]
        inputs[pos3] = inputs[pos1] + inputs[pos2]
      elif inputs[pos] == 2:
        pos1 = inputs[pos + 1]
        pos2 = inputs[pos + 2]
        pos3 = inputs[pos + 3]
        inputs[pos3] = inputs[pos1] * inputs[pos2]
      else:
        break
      pos += 4
    # if 1969000 < inputs[0] and inputs[0] < 1969099:
    #   print(inputs[0])
    if inputs[0] == 19690720:
      print(100 * inputs[1] + inputs[2])
      break
      break
