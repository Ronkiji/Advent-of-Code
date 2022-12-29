# inputs = [line.rstrip('\n') for line in open("inputs/17.txt")]
# inputs = inputs[0]

# from itertools import cycle
# rc = 0

# print(list(inputs))
# push = cycle(inputs)
# rocks = [   [(0, 2), (0, 3), (0,4), (0, 5)],
#             [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)],
#             [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)],
#             [(0, 2), (1, 2), (2, 2), (3, 2)],
#             [(0, 2), (0, 3), (1, 2), (1, 3)]    ]
# rock = cycle(rocks)

# maxheight = 0
# height = 0
# row = 3
# visited = set()
# pi = -1
# pn = 0

# index = {}

# for rn, r in enumerate(rock):  
    
#     if rn == 2022:
#         break
    
#     ri = rn % len(rocks)
#     shape = [(row + c[0], c[1]) for c in r]
    
#     while all(s not in visited for s in shape):
        
#         p = next(push)
#         pn += 1
#         pi = pn % len(inputs)
        
#         if p == '>':
#             s_temp = [(s[0], s[1] + 1) for s in shape]
#         elif p == '<':
#             s_temp = [(s[0], s[1] - 1) for s in shape]
#         if all(0 <= s[1] < 7 for s in s_temp) and all(s not in visited for s in s_temp):
#             shape = s_temp
#         s_temp = [(s[0] - 1, s[1]) for s in shape]
#         if all(s[0] >= 0 for s in s_temp) and all(s not in visited for s in s_temp):
#             shape = s_temp
#         else:
#             for s in shape:
#                 visited.add(s)
#             # print(visited)
#             height = max([v[0] for v in visited])
#             row = height + 4
# print(height + 1)
    
    
print(hash('[(1, 2), (1, 5, 10)]'))
print(hash('[(1, 2), (1, 5, 10)]'))
        
        
#     rc = ri % len(rocks)
#     shape = [(row + coord[0], coord[1]) for coord in r]
#     while all(s not in visited for s in shape): 
#         p = next(push)
#         pi += 1
#         pc = pi % len(inputs)
#         if p == '>':
#             s_temp = [(s[0], s[1] + 1) for s in shape]
#             if all(s[1] < 7 for s in s_temp) and all(s not in visited for s in s_temp):
#                 shape = s_temp
#         elif p == '<':
#             s_temp = [(s[0], s[1] - 1) for s in shape]
#             if all(s[1] >= 0 for s in s_temp) and all(s not in visited for s in s_temp):
#                 shape = s_temp
#         s_temp = [(s[0] - 1, s[1]) for s in shape]
#         if all(s[0] >= 0 for s in s_temp) and all(s not in visited for s in s_temp):
#             shape = s_temp
#         else:
#             for s in shape:
#                 visited.add(s)
                
#             if visited in index.values():
#                 print(rc, pc)
#                 exit(0)
#             if (rc, pc) not in index:
#                 index[(rc, pc)] = []
#             index[(rc, pc)].append(visited)
#             height = max([v[0] for v in visited])
#             row = height + 4
# print(height + 1)
            
            