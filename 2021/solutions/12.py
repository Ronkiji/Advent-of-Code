# Part 2
inputs = []
for line in open("inputs/day12.txt"):
  line = line.rstrip('\n')
  act = line[0 : 1]
  if act == 'E':
    act = 0
  elif act == 'S':
    act = 1
  elif act == 'W':
    act = 2
  elif act == 'N':
    act = 3
  val = int(line[1 :])
  inputs.append([act, val])

wp = [10, 1]
current = 0;
ship = [0, 0]
# map East to 0, South to 1, West to 2, North to 3
# current = pos % 4

ver = 0
hor = 0

def new(act, val):
  global ship
  global wp
  global current
  if isinstance(act, int):
    if act == 0:
      wp = [wp[0] + val, wp[1]]
    elif act == 1:
      wp = [wp[0], wp[1] - val]
    elif act == 2:
      wp = [wp[0] - val, wp[1]]
    elif act == 3:
      wp = [wp[0], wp[1] + val]
  elif act == 'F':
    ship = [ship[0] + val * wp[0], ship[1] + val * wp[1]]
  elif act == 'L':
    if val/90 == 1:
      wp = [-wp[1], wp[0]]
    elif val/90 == 2:
      wp = [-wp[0], -wp[1]]
    elif val/90 == 3:
      wp = [wp[1], -wp[0]]
    elif val/90 == 4:
      wp = [wp[0], wp[1]]
  elif act == 'R':
    if val/90 == 1:
      wp = [wp[1], -wp[0]]
    elif val/90 == 2:
      wp = [-wp[0], -wp[1]]
    elif val/90 == 3:
      wp = [-wp[1], wp[0]]
    elif val/90 == 4:
      wp = [wp[0], wp[1]]

# Part 1
# inputs = []
# for line in open("inputs/day12.txt"):
#   line = line.rstrip('\n')
#   act = line[0 : 1]
#   if act == 'E':
#     act = 0
#   elif act == 'S':
#     act = 1
#   elif act == 'W':
#     act = 2
#   elif act == 'N':
#     act = 3
#   val = int(line[1 :])
#   inputs.append([act, val])

# current = 0;
# # map East to 0, South to 1, West to 2, North to 3
# # current = pos % 4

# ver = 0
# hor = 0

# def new(act, val):
#   # print(val)
#   global current
#   if isinstance(act, int):
#     calc(act, val)
#   elif act == 'F':
#     calc(current, val)
#   elif act == 'L':
#     current = (current - (val/90)) % 4
#   elif act == 'R':
#     current = (current + (val/90)) % 4

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

# print(abs(ver) + abs(hor))