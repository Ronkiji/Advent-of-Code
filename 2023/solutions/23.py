

import sys
sys.setrecursionlimit(20000)
G = [line.rstrip('\n') for line in open("inputs/23.txt")]
ysize, xsize = len(G), len(G[0])
D = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
S = (0, G[0].find("."))
E = (xsize-1, G[-1].find("."))

dist = []

def dfs(v, n):
    if n == E:
        dist.append(len(v))
        return
    if n in v: 
        return
    c = G[n[0]][n[1]]
    if c == "#": 
        return
    v.add(n)
    if c in D:
        new = (n[0] + D[c][0], n[1] + D[c][1])
        dfs(v.copy(), new)
        return
    for x, y in [[-1,0],[0,1],[1,0],[0,-1]]:
        new = (n[0] + x, n[1] + y)
        if 0 <= new[0] < ysize and 0 <= new[1] < xsize:
            dfs(v.copy(), new)
    return 

dfs(set(), S)
print(max(dist)) # only p1


# from collections import defaultdict
# import sys
# G = [line.rstrip('\n') for line in open("inputs/23.txt")]
# ysize = len(G)
# xsize = len(G[0])
# D = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}

# nodes = set()
# S = (0, G[0].find("."))
# E = (xsize-1, G[-1].find("."))
# for y in range(len(G)):
#     for x in range(len(G[0])):
#         if G[y][x] != "#":
#             nodes.add((y, x))
# print(len(nodes))

# # pruning graph
# res = {}
# for n in nodes:
#     adj = dict()
#     for x, y in [[-1,0],[0,1],[1,0],[0,-1]]:
#         new = (n[0] + x, n[1] + y)
#         adj[new] = 1
#     res[n] = adj  
#     allkeys = list(res.keys())
#     for key in allkeys:
#         neighbors = res[key]
#         if len(neighbors) == 2:
#             left_neighbor, right_neighbor = neighbors.keys()
#             del res[left_neighbor][key]
#             del res[right_neighbor][key]
#             res[left_neighbor][right_neighbor] = max(res[left_neighbor].get(right_neighbor, 0),  neighbors[left_neighbor] + neighbors[right_neighbor])
#             res[right_neighbor][left_neighbor] = res[left_neighbor][right_neighbor]
#             del res[key]

# print(res.values())
# nodes = res.keys()
# print(len(res.keys()))
# dist = []

# occ = set()

# def dfs(v, n):
    
#     if n == E:
#         print(len(v))
#         dist.append(len(v))
#         return True
#     if n not in nodes:
#         return False
#     if n in v:
#         return False
#     v.add(n)
#     # if c in D:
#     #     new = (n[0] + D[c][0], n[1] + D[c][1])
#     #     dfs(newv, new)
#     #     return
#     for x, y in [[-1,0],[0,1],[1,0],[0,-1]]:
#         new = (n[0] + x, n[1] + y)
#         if 0 <= new[0] < ysize and 0 <= new[1] < xsize:
#             dfs(v.copy(), new)

#     return 

# sys.setrecursionlimit(20000)

# dfs(set(), S)

# print(max(dist))


    




    


