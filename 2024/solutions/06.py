G = [line.rstrip('\n') for line in open("inputs/06.txt")]
C, R = len(G), len(G[0])
B = set() # blocks
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
S = (0, 0)
for y in range(C):
    for x in range(R):
        if G[y][x] == "^":
            S = (y, x)
        elif G[y][x] == "#":
            B.add((y, x))

def search(B, S):
    V = set() # visited
    D = 0 # direction index
    while 0 <= S[0] < C and 0 <= S[1] < R:
        if (S, D) in V: # include direction for part two
            return False
        V.add((S, D))
        
        y, x = dirs[D]
        next = (S[0] + y, S[1] + x)

        if next in B:
            D = ( D + 1) % 4
        else: 
            S = next
    U = set() # get unique locations visited
    for (tup, dir) in V:
        U.add(tup)
    return len(U)

def two():
    T = 0
    for y in range(C):
        for x in range(R):
            if (y,x) not in B:
                B_copy = B.copy()
                B_copy.add((y,x))
                S_copy = S
                if not search(B_copy, S_copy):
                    T += 1
    return T

print(search(B, S)) # one
print(two())