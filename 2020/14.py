memory = []
mask = ''

def find(a, m):
  # address and mask 
  a = bin(int(a))
  a = a.replace('b', '0' * (37 - len(a)))
  lm = list(m)
  la = list(a)
  for i in range(len(lm)):
    if lm[i] != '0':
      la[i] = lm[i]
  
  # number of binary numbers
  a = ''.join(la)
  bn = a.count('X')

  mx = ''
  for x in range(bn):
    mx += '1'
  
  mx = int(mx, 2)

  # all bi possibilities
  ab = []
  for i in range(mx + 1):
    bi = bin(int(i))[2:].zfill(bn)
    bi = list(bi)
    ab.append(bi)
  
  # all addresses
  aa = []
  for q in ab:
    ind = 0
    dup = list(a)
    a = list(a)
    for x in range(len(a)):
      if a[x] == 'X':
        dup[x] = q[ind]
        ind += 1
    aa.append(int((''.join(dup)), 2))
  return aa

for line in open("inputs/day14.txt"):
  line = line.rstrip('\n')
  key, val = line.split(' = ')
  if key == 'mask':
    mask = val
    print(mask)
  else:
    mem = key[4 : -1]
    add = find(mem, mask)
    dup = False
    loop = 0
    for x in memory:
      if x[0] in add:
        index = add.index(x[0])
        del add[index]
        memory[loop][1] = val
      loop += 1
    for x in add:
      memory.append([x, val])

sums = 0
for x in memory:
  sums += int(x[1])

print(sums)

# memory = []
# mask = ''

# for line in open("inputs/day14.txt"):
#   line = line.rstrip('\n')
#   key, val = line.split(' = ')
#   if key == 'mask':
#     mask = val
#   else:
#     val = bin(int(val))
#     val = val.replace('b', '0' * (37 - len(val)))
#     lm = list(mask)
#     lv = list(val)
#     for i in range(len(lm)):
#       if lm[i] != 'X':
#         lv[i] = lm[i]
#     mask = ''.join(lm)
#     val = ''.join(lv)
#     mem = key[4 : -1]
#     dup = False
#     loop = 0
#     for x in memory:
#       if x[0] == mem:
#         dup = True
#         memory[loop][1] = val
#       loop += 1
#     if dup == False:
#       memory.append([mem, val])

# sums = 0
# for x in memory:
#   sums += int(x[1], 2)
  
# print(sums)