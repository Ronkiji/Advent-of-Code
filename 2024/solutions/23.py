connections = [line.rstrip('\n') for line in open("inputs/23.txt")]
from itertools import combinations
from collections import defaultdict
from functools import cache

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

T = 0
triangles = set()
for k, v in graph.items():
    for a, b in combinations(v, 2):
        if a in graph[b]:
            if any(n.startswith('t') for n in [k, a, b]):
                triangles.add(tuple(sorted([k,a,b])))

print(len(triangles))

def bron_kerbosch(graph, R, P, X, cliques):
    if not P and not X:
        cliques.append(R)
        return
    for node in list(P):
        bron_kerbosch(
            graph,
            R.union({node}),
            P.intersection(graph[node]),
            X.intersection(graph[node]),
            cliques
        )
        P.remove(node)
        X.add(node)

nodes = set(graph.keys())
cliques = []
bron_kerbosch(graph, set(), nodes, set(), cliques)

print(",".join(sorted(max(cliques, key=len))))
