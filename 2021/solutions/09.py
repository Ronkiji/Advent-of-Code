inputs =[]
for line in open("inputs/day09.txt"):
  line = line.rstrip('\n')
  inputs.append(int(line))

for x in range(len(inputs)):
  num = inputs[x]
  pos = 1
  total = [num]
  while num < 90433990:
    num += inputs[x + pos]
    total.append(inputs[x + pos])
    if num == 90433990:
      total.sort()
      print(total[0] + total[-1])
      

    pos += 1

# for x in range(25, len(inputs)):
#   nums = []
#   for previous in range(x-25, x):
#     nums.append(inputs[previous])
#   for key1 in nums:
#     for key2 in nums:
#       if key1 + key2 == inputs[x]:
#         check = True
#   if check == False:
#     print(inputs[x])
#     break
#   check = False