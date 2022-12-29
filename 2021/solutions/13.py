inputs = []
for line in open("inputs/day13.txt"):
  line = line.rstrip('\n')
  inputs.append(line)

value = int(inputs[0])
nums = []

inputs[1] = inputs[1].split(',')

for x in inputs[1]:
  if x != 'x':
    nums.append(int(x))

print(nums)

def find(val):
  global value
  curr = 0
  while True:
    curr += val
    if(curr >= value):
      break
  return curr, val

new = []

for x in nums:
  new.append(find(x))

new.sort(key=lambda x: x[0])

print((new[0][0] - value) * new[0][1])


# my part 2
# inputs = []
# for line in open("inputs/day13.txt"):
#   line = line.rstrip('\n')
#   inputs.append(line)

# inputs[1] = inputs[1].split(',')

# keys = []
# offset = 0

# for x in inputs[1]:
#   if x != 'x':
#     keys.append([int(x), offset])
#   offset += 1

# print(keys)

# loop = 1

# allNum = []
# boolean = True
# while boolean:
#   print(loop)
#   for sets in keys:
#     allNum.append((sets[0] * loop) - sets[1])

#   if loop % 100 == 0:
#     for elem in allNum:
      
#       if allNum.count(elem) == len(keys):
#         boolean = False
#         print(elem)
#         break

#   loop += 1










# Someone else's part two, I don't understand yet
# https://github.com/stevotvr/adventofcode2020/blob/main/aoc2020/src/day13/day13.java
# with open("inputs/day13.txt", "r") as fp:
#     lines = fp.readlines()
# timestamp = int(lines[0][:-1])
# bus_ids = [int(x) for x in lines[1].split(",") if x.isdigit()]

# import numpy as np
# timestamps = range(timestamp-50, timestamp+50)
# valid = np.inf
# diff = np.inf
# bus_id = np.inf

# for time in timestamps:
#     for bus in bus_ids:
#         if time%bus==0:
#             d = abs(time-timestamp)
#             if time>timestamp and d < diff:
#                 valid = time
#                 diff = d
#                 bus_id = bus

# # print(bus_id*(valid-timestamp))

# LINES=lines
# start = int(LINES[0])
# busses = ["x" if x == "x" else int(x) for x in LINES[1].split(",")]
# print(busses)

# def part2():
#     mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
#     print(mods)
#     vals = list(reversed(sorted(mods)))
#     val = mods[vals[0]]
#     r = vals[0]
#     for b in vals[1:]:
#         while val % b != mods[b]:
#             val += r
#         r *= b
#     return val
# print(part2())