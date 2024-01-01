G = [line.rstrip('\n') for line in open("inputs/18.txt")]

def _area_(coords):
    t=0
    for count in range(len(coords)-1):
        y = coords[count+1][1] + coords[count][1]
        x = coords[count+1][0] - coords[count][0]
        z = y * x
        t += z
    return abs(t/2.0)


DT = {"D": (1, 0), # down
        "U": (-1, 0), # up
        "R": (0, 1), # right
        "L": (0, -1), # left
        "1": (1, 0), # down
        "3": (-1, 0), # up
        "0": (0, 1), # right
        "2": (0, -1)}

P = (0,0)
S = []
for L in G:
    D, N, _ = L.split()
    dir = DT[D]
    for n in range(int(N)):
        P = (P[0] + dir[0], P[1] + dir[1])
        S.append(P)

print(_area_(S) + 1 + len(S)//2)

P = (0, 0)
S = []
for L in G:
    _, _, H = L.split()
    dir = DT[H[-2]]
    N = int(H[2:-2], 16)
    for n in range(int(N)):
        P = (P[0] + dir[0], P[1] + dir[1])
        S.append(P)

print(_area_(S) + 1 + len(S)//2)
