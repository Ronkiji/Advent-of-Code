info = []

for x in range(int(input())):
  info.append([int(x) for x in input().split(" ")])


mn = min(info)[0]

records = 0

for x in range(mn, max(info)[0]):
  seconds = 0
  for i in range(len(info)):
    pos = info[i][0]
    sec = info[i][1]
    dis = info[i][2]

    diff = abs(x - pos)

    if diff >= dis:
      seconds += (diff - dis)*sec
    
  if x == mn:
    record = seconds
    
  if seconds < record:
    record = seconds

print(record)
  




# M = int(input())
# K = int(input())

# table = []

# for x in range(M):
#   table.append([False for i in range(K)])

# key = []
# val = []

# for x in range(int(input())):
#   k, v = input().split(" ")
#   key.append(k)
#   val.append(int(v))



# for x in range(len(key)): 
#   if key[x] == "R":
#     for num in range(len(table[val[x] - 1])):
#       if table[val[x] - 1][num] == False:
#         table[val[x] - 1][num] = True
#       else:
#         table[val[x] - 1][num] = False
#   else:
#     for num in range(len(table)):
#       if table[num][val[x]-1] == False:
#         table[num][val[x]-1] = True
#       else:
#         table[num][val[x]-1] = False

# total = 0

# for x in range(M):
#   for y in range(K):
#     if table[x][y] == True:
#       total += 1

# print(total)





# num = int(input())

# h = [int(x) for x in input().split(" ")]

# w = [int(x) for x in input().split(" ")]

# area = 0

# for x in range(num):
#   area += (h[x] + h[x+1]) * w[x] / 2.0 

# print(area)





























# inputs = []

# for x in range(5):
#   inputs.append(input())

# print(inputs)

# with open("inputs/day19.txt") as fp:
#     rules, messages = fp.read().split('\n\n')
#     rules = rules.splitlines()
#     messages = messages.splitlines()

# print(rules)
# print(messages)
# def get(num):
#   inputs = {0: [0], 13: [1], 1: [2], 8: [3], 6: [4], 15: [5]}
#   curr = 15
#   pos = 6
#   while pos < num:

#     if inputs[curr][0] == pos - 1:
#       inputs[0].append(pos)
#       curr = 0
#     else:
#       diff = inputs[curr][-1] - inputs[curr][-2]
#       if diff in inputs:
#         inputs[diff].append(pos)
#       else:
#         inputs[diff] = [pos]
#       curr = diff

#     pos += 1

#   return curr

# print(get(2020))
# print(get(30000000))
# if curr in inputs:
#   # if inputs[15] = [5]
#   index = len(copy) - 1 - copy[::-1].index(curr)
#   inputs.append(pos - index)
# else:
#   inputs.append(0)
# pos += 1

# if pos == 2019:
#   print('# at 2020: ' + str(inputs[pos]))
#   break
# dif1 = 0
# dif3 = 1

# for x in range(len(inputs)):
#   if x == 0:
#     dif = inputs[x]
#   else:
#     dif = inputs[x] - inputs[x-1]

#   if dif == 1:
#     dif1 += 1
#   elif dif == 3:
#     dif3 += 1

# print(dif1 * dif3)
# sol = {0:1}
# for line in sorted(inputs):
#     sol[line] = 0
#     print(sol)
#     if line - 1 in sol:
#         sol[line]+=sol[line-1]
#     if line - 2 in sol:
#         sol[line]+=sol[line-2]
#     if line - 3 in sol:
#         sol[line]+=sol[line-3]

# print(sol[max(inputs)])
# import re

# class Solver(int):
#     def __mul__(self, inp):
#         return Solver(int(self) + inp)
#     def __add__(self, inp):
#         return Solver(int(self) + inp)
#     def __sub__(self, inp):
#         return Solver(int(self) * inp)

# def evaluate1(expression):
#     expression = re.sub(r"(\d+)", r"Solver(\1)", expression)
#     expression = expression.replace("*", "-")
#     return eval(expression, {}, {"Solver": Solver})

# def evaluate2(expr):
#     expr = re.sub(r"(\d+)", r"Solver(\1)", expr)
#     expr = expr.replace("*", "-")
#     expr = expr.replace("+", "*")
#     return eval(expr, {}, {"Solver": Solver})

# with open("inputs/day18.txt") as fp:
#     lines = [line.split("\n")[0] for line in fp.readlines()]
# print("Part 1:", sum(evaluate1(l) for l in lines))
# print("Part 2:", sum(evaluate2(l) for l in lines))
# inputs = []
# for line in open("inputs/day18.txt"):
#   line = '(' + line.rstrip('\n').replace(' ', '') + ')'
#   inputs.append(line)
# sums = []

# def evaluate(line, pos):
#   val = 0
#   cur = '+'
#   lim1 = 0
#   lim2 = 0
#   for x in range(pos + 1, len(line)):
#     if (lim1 < x <= lim2) == False:
#       if line[x].isnumeric():
#         val = eval('val' + cur + 'int(line[x])')
#       elif line[x] == '*' or line[x] == '+':
#         cur = line[x]
#       elif line[x] == ')':
#         return val, x
#       else:
#         value, lim2 = evaluate(line, x)
#         lim1 = x
#         val = eval('val' + cur + 'value')
#     elif x >= len(line):
#       return val, x
#   return None

# for line in inputs:
#   value, limit = evaluate(line, 0)
#   sums.append(value)

# print(sum(sums))

# for line in inputs:
#   for char in line:
#     print(char)

# memory = []
# mask = ''

# def find(a, m):
#   # address and mask
#   a = bin(int(a))
#   a = a.replace('b', '0' * (37 - len(a)))
#   lm = list(m)
#   la = list(a)
#   for i in range(len(lm)):
#     if lm[i] != '0':
#       la[i] = lm[i]

#   # number of binary numbers
#   a = ''.join(la)
#   bn = a.count('X')

#   mx = ''
#   for x in range(bn):
#     mx += '1'

#   mx = int(mx, 2)

#   # all bi possibilities
#   ab = []
#   for i in range(mx + 1):
#     bi = bin(int(i))[2:].zfill(bn)
#     bi = list(bi)
#     ab.append(bi)

#   # all addresses
#   aa = []
#   for q in ab:
#     ind = 0
#     dup = list(a)
#     a = list(a)
#     for x in range(len(a)):
#       if a[x] == 'X':
#         dup[x] = q[ind]
#         ind += 1
#     aa.append(int((''.join(dup)), 2))
#   return aa

# for line in open("inputs/day14.txt"):
#   line = line.rstrip('\n')
#   key, val = line.split(' = ')
#   if key == 'mask':
#     mask = val
#     print(mask)
#   else:
#     mem = key[4 : -1]
#     add = find(mem, mask)
#     dup = False
#     loop = 0
#     for x in memory:
#       if x[0] in add:
#         index = add.index(x[0])
#         del add[index]
#         memory[loop][1] = val
#       loop += 1
#     for x in add:
#       memory.append([x, val])

# sums = 0
# for x in memory:
#   sums += int(x[1])

# print(sums)

#   mem = 0
#   num = 0
#   line = line.rstrip('\n')
#   if line[0 : 4] == 'mask':
#     loc = []
#     mask = line[7 :]
#     print('MASK IS ' + mask)
#     loop = 0
#     for x in mask:
#       if x != 'X':
#         loc.append([loop, x])
#       loop += 1
#     # print(loc)
#   else:
#     mem, num = line.split('] = ')
#     mem = mem[-1]
#     find(mem, num)

# val = 0
# for x in memory:
#   val += int(x[1], 2)

# print(val)

# with open("inputs/day14.txt", 'r') as fp:
#     lines = [line.rstrip() for line in fp.readlines()]

# memory = {}
# masks = []
# curr_mask = None
# curr_value = None
# curr_address = None

# for line in lines:
#     k, v = line.split(" = ")
#     if k == "mask":
#         masks.append(v)
#         curr_mask = v
#     else:
#         # get address
#         curr_address = int(k[4:-1])
#         curr_value = int(v)

#         bin_value = list(bin(curr_value)[2:].zfill(36))
#         new_value = [0] * 36

#         for i, (mask, value) in enumerate(zip(curr_mask, bin_value)):
#             # do nothing if X
#             if mask == "X":
#                 new_value[i] = value
#             else:
#                 # change value to mask else
#                 new_value[i] = mask

#         memory[curr_address] = int("".join(new_value), 2)
# print(f"Part one solution: {sum(memory.values())}")

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

# append all values to an array and check if any values repeat x amount of times
# value = int(inputs[0])
# nums = []

# inputs[1] = inputs[1].split(',')

# for x in inputs[1]:
#   if x != 'x':
#     nums.append(int(x))

# print(nums)

# def find(val):
#   global value
#   curr = 0
#   while True:
#     curr += val
#     if(curr >= value):
#       break
#   return curr, val

# new = []

# for x in nums:
#   new.append(find(x))

# new.sort(key=lambda x: x[0])

# print((new[0][0] - value) * new[0][1])

# wp = [10, 1]
# current = 0;
# ship = [0, 0]
# # map East to 0, South to 1, West to 2, North to 3
# # current = pos % 4

# ver = 0
# hor = 0

# def new(act, val):
#   # print(val)
#   global ship
#   global wp
#   global current
#   if isinstance(act, int):
#     if act == 0:
#       wp = [wp[0] + val, wp[1]]
#     elif act == 1:
#       wp = [wp[0], wp[1] - val]
#     elif act == 2:
#       wp = [wp[0] - val, wp[1]]
#     elif act == 3:
#       wp = [wp[0], wp[1] + val]
#   elif act == 'F':
#     ship = [ship[0] + val * wp[0], ship[1] + val * wp[1]]
#   elif act == 'L':
#     if val/90 == 1:
#       wp = [-wp[1], wp[0]]
#     elif val/90 == 2:
#       wp = [-wp[0], -wp[1]]
#     elif val/90 == 3:
#       wp = [wp[1], -wp[0]]
#     elif val/90 == 4:
#       wp = [wp[0], wp[1]]
#   elif act == 'R':
#     if val/90 == 1:
#       wp = [wp[1], -wp[0]]
#     elif val/90 == 2:
#       wp = [-wp[0], -wp[1]]
#     elif val/90 == 3:
#       wp = [-wp[1], wp[0]]
#     elif val/90 == 4:
#       wp = [wp[0], wp[1]]

# def calc(d, v):
#   global ver
#   global hor
#   if d == 0:
#     hor += v
#   elif d == 1:
#     ver -= v
#   elif d == 2:
#     hor -= v
#   elif d == 3:
#     ver += v

# for line in inputs:
#   new(line[0], line[1])
#   print(wp)
#   print(ship)
#   print()

# print(abs(ship[0]) + abs(ship[1]))

# accum = 0
# visited = []

# def new(pos, op, arg):
#   visited.append(pos)
#   if op == 'acc':
#     global accum
#     accum += eval(arg)
#     return pos + 1
#   elif op == 'jmp':
#     return pos + eval(arg)
#   else:
#     return pos + 1

# # print(inputs[1])

# pos = 0

# while True:
#   if pos == len(inputs):
#     break
#   upd = new(pos, inputs[pos][0], inputs[pos][1])
#   if upd in visited:
#     break
#   else:
#     pos = upd

# print('Accumulator = ' + str(accum))

# def new(inputs, x, y):
#   # print(inputs)
#   around = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x + 1, y], [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]
#   # print(inputs[x][y] + ' ' + str(x) + ' ' + str(y))
#   # print(inputs[91][0])
#   if inputs[x][y] == 'L':
#     for e in around:
#       if 0 <= e[0] < len(inputs) and 0 <= e[1] < len(inputs[0]):
#         if inputs[e[0]][e[1]] == '#':
#           return 'L'
#     return '#'

#   elif inputs[x][y] == '#':
#     count = 0
#     for e in around:
#       if 0 <= e[0] < len(inputs) and 0 <= e[1] < len(inputs[0]):
#         # if x == 0 and y == 2:
#         #   print(inputs[e[0]][e[1]] + '  ' + str(e[0])  + '  ' + str(e[1]))
#         if inputs[e[0]][e[1]] == '#':
#           count += 1
#     # if x == 0 and y == 2:
#     #     print(count)
#     if count >= 4:
#       return 'L'
#     else:
#       return '#'

#   else:
#     return '.'

# dup = []
# loop = 0

# while True:
#   string = ''
#   # print('Length: ' + str(len(inputs[0])))
#   # print(inputs[91][1])

#   for x in range(len(inputs)):
#     for y in range(len(inputs[0])):
#       # print(str(x) + ' ' + str(y))
#       string += new(inputs, x, y)
#     # print(string + '  ' + str(x) + ' ' + str(y))
#     dup.append(string)
#     string = ''

#   loop += 1
#   # print(loop)
#   # print(inputs)
#   # print(dup)

#   if inputs == dup:
#     break

#   inputs = dup
#   dup = []
#   # print('loop done')
#   # print()

# occ = 0
# for row in inputs:
#   occ += row.count('#')

# print(occ)

#     #.#L.L#.##
#     #LLL#LL.L#
#     L.#.L..#..
#     #L##.##.L#
#     #.#L.LL.LL
#     #.#L#L#.##
#     ..L.L.....
#     #L#L##L#L#
#     #.LLLLLL.L
#     #.#L#L#.##

# for x in range(len(inputs)):
#   num = inputs[x]
#   pos = 1
#   total = [num]
#   while num < 90433990:
#     num += inputs[x + pos]
#     total.append(inputs[x + pos])
#     if num == 90433990:
#       total.sort()
#       print(total[0] + total[-1])

#     pos += 1

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

# inputs = {}
# for line in open("inputs/day7.txt"):
#   line = line.rstrip('.\n')
#   large, small = line.split(' bags contain ')
#   current = {}
#   if 'no other bags' in small:
#     small = ''
#   elif ', ' in small:
#     small = small.split(', ')
#     for x in small:
#       x = x.replace(' bags', '')
#       x = x.replace(' bag', '')
#       val = x[0:1]
#       color = x[2:]
#       current[color] = int(val)
#   else:
#     small = small.replace(' bag', '')
#     val = small[0:1]
#     color = small[2:]
#     current[color] = int(val)
#   inputs[large] = current

# print(inputs)

# inputs = []
# for line in open("inputs/day7.txt"):
#   line = line.rstrip('\n')
#   large, small = line.split(' bags contain ')
#   current = []
#   if 'no other bags.' in small:
#     small = ''
#   elif ', ' in small:
#     small = small.split(', ')
#     small[-1] = small[-1].replace('.', '')
#     for x in small:
#       x = x.replace(' bags', '')
#       x = x.replace(' bag', '')
#       color = x[0:1]
#       val = x[2:]
#       current.append([val, color])
#   else:
#     small.replace('.', '')
#     color = x[0:1]
#     val = x[2:]
#     current.append([val, color])
#   inputs.append([large, current])

# print(inputs[1][1][1][1])

# inputs = []
# current = ''
# numPpl = 0
# for line in open("inputs/day6.txt"):
#   line = line.rstrip('\n')
#   if line != '':
#     current += line
#     numPpl += 1
#   elif line == '':
#     current = current.rstrip('\n')
#     inputs.append([current, numPpl])
#     current = ''
#     numPpl = 0
# if current != '': inputs.append([current, numPpl])

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# sumCount = []

# for line in inputs:
#   count = 0
#   for char in alphabet:
#     if line[0].count(char) == line[1]:
#       count += 1
#   sumCount.append(count)

# print(sum(sumCount))

# inputs = []
# mapping = [['F', '0'], ['B', '1'], ['L', '0'], ['R', '1']]

# for line in open("inputs/day5.txt"):
#   line = line.rstrip('\n')
#   # y = line[0 : 7]
#   # x = line[7 :]
#   inputs.append(line)

# binInputs = []

# for line in inputs:
#   binary = ''
#   for char in line:
#     if char == 'F' or char == 'L':
#       binary += '0'
#     elif char == 'B' or char == 'R':
#       binary += '1'

#   binInputs.append(binary)

# seatId = []

# for line in binInputs:
#   y = int(line[0 : 7], 2)
#   x = int(line[7 :], 2)
#   seatId.append(y * 8 + x)

# seatId.sort()
# print(seatId[-1])

# for x in range(len(seatId)):
#   if x != len(seatId) - 1:
#     if seatId[x] - seatId[x+1] == -2:
#       print(seatId[x] + 1)

# inputs = []
# current = ''
# for line in open("inputs/day4.txt"):
#   line = line.rstrip('\n')
#   if line != '':
#     current += line + ' '
#   elif line == '':
#     current = current.rstrip('\n')
#     inputs.append(current)
#     current = ''
# if current != '': inputs.append(current)

# elements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# count = 0
# results = []

# valids = []

# for line in inputs:
#   for substrings in elements:
#     results.append(substrings in line)
#   if all(results):
#     valids.append(line)
#     count += 1
#   results = []
# print(count)

# keyval = []

# full = []

# for line in valids:
#   for field in line.split():
#     key, value = field.split(':')
#     keyval.append([key, value])
#   full.append(keyval)
#   keyval = []

# num = 0
# total = 0

# for line in full:
#   for x in line:

#     # for years
#     if x[0] == 'byr':
#       if 1920 <= int(x[1]) <= 2002:
#         num += 1
#     elif x[0] == 'iyr':
#       if 2010 <= int(x[1]) <= 2020:
#         num += 1
#     elif x[0] == 'eyr':
#       if 2020 <= int(x[1]) <= 2030:
#         num += 1

#     # for height
#     elif x[0] == 'hgt':
#       if x[1].find('cm') != -1:
#         hgtcm = int(x[1][0 : -2])
#         if 150 <= hgtcm <= 193:
#           num += 1
#       elif x[1].find('in') != -1:
#         hgtin = int(x[1][0 : -2])
#         if 59 <= hgtin <= 76:
#           num += 1

#     # for colors
#     elif x[0] == 'hcl':
#       hcl = x[1][1:]
#       if len(hcl) == 6:
#         charvalid = 0
#         for char in hcl:
#           if char.isnumeric() and 0 <= int(char) <= 9:
#             charvalid += 1
#           elif 'a' <= char <= 'f':
#             charvalid += 1
#         if charvalid == 6:
#           num += 1

#     elif x[0] == 'ecl':
#       if x[1] == 'amb' or x[1] == 'blu' or x[1] == 'brn' or x[1] == 'gry' or x[1] == 'grn' or x[1] == 'hzl' or x[1] == 'oth':
#         num += 1

#     # for ID
#     elif x[0] == 'pid':
#       if x[1].isnumeric() and len(x[1]) == 9:
#         num += 1

#   if num == 7:
#     total += 1
#   num = 0

# print(total)

# inputs1 = []

# for line in inputs:
#   for substrings in elements:
#     results.append(substrings in line)

#   if all(results):
#     inputs1.append(line)
#     print(line)
#     pos = line.find('byr:')
#     byr = int(line[pos + 4 : pos + 8])

#     if 1920 <= byr <= 2002:
#       print(byr)
#       pos = line.find('iyr:')
#       iyr = int(line[pos + 4 : pos + 8])

#       if 2010 <= iyr <= 2020:
#         print(iyr)
#         pos = line.find('eyr:')
#         eyr = int(line[pos + 4 : pos + 8])

#         if 2020 <= eyr <= 2030:
#           print(eyr)
#           pos = line.find('hgt:')

#           valid = False
#           hgt = 0
#           if line.find('cm ') != -1 and 1 < (line.find('cm ') - (pos + 4)) < 4:
#             hgtcm = int(line[pos + 4 : line.find('cm ')])
#             # print(str(hgtcm) + 'cm')
#             if 150 <= hgtcm <= 193:
#               valid = True
#               hgt = hgtcm
#           elif line.find('in ') and 1 < (line.find('in ') - (pos + 4)) < 4:
#             hgtin = int(line[pos + 4 : line.find('in ')])
#             # print(str(hgtin) + 'in')
#             if 59 <= hgtin <= 76:
#               valid = True
#               hgt = hgtin

#           if valid:
#             print(hgt)

# for substrings in elements:
#   print(line)
#   print(substrings)
#   print(line.find(substrings))
# count += 1
# results = []

# print(inputs1)

# c1 = 0
# pos1 = -1

# for x in range(len(inputs)):
#   pos1 += 1
#   if pos1 >= 31:
#     pos1 -= 31
#   if inputs[x][pos1] == '#':
#     c1 += 1

# inputs = []
# for line in open("inputs/day2.txt"):
#   line = line.rstrip('\n')
#   r, l, st = line.split(' ')
#   r1, r2 = r.split('-')
#   l = l.strip(':')
#   inputs.append([int(r1), int(r2), l, st])
# count = 0
# for x in inputs:
#   if (x[3][x[0]-1] == x[2]) ^ (x[3][x[1]-1] == x[2]):
#     count += 1

# print(count)

# inputs = [[int(line.rstrip('\n')) for line in open("inputs/day1.txt")]]
# for a in inputs:
#   for b in inputs:
#     for c in inputs:
#       if a + b + c == 2020:
#         print(a * b * c)
