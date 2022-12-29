def get(num):
  inputs = {0: [0], 13: [1], 1: [2], 8: [3], 6: [4], 15: [5]}
  curr = 15
  pos = 6 
  while pos < num:

    if inputs[curr][0] == pos - 1:
      inputs[0].append(pos)
      curr = 0
    else:
      diff = inputs[curr][-1] - inputs[curr][-2]
      if diff in inputs:
        inputs[diff].append(pos)
      else:
        inputs[diff] = [pos]
      curr = diff

    pos += 1

  return curr

print(get(2020))
print(get(30000000))