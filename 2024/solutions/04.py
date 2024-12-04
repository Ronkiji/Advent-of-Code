I = [line.rstrip('\n') for line in open("inputs/04.txt")]
N = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0), (0, -1)]
R, C = len(I), len(I[0])
W = "XMAS"

def one():

    def search(y, x, n1, n2):
        for i in range(4):
            yy = y + (n1 * i)
            xx = x + (n2 * i)
            if not( 0 <= yy < R and 0 <= xx < C) or  I[yy][xx] != W[i]:
                return 0
        return 1

    T = 0
    for y in range(R):
        for x in range(C):
            for n1, n2 in N:
                T += search(y, x, n1, n2)
    return T

def two():

    def search(y, x):
        if y + 3 > R or x + 3 > C:
            return 0
        
        P = [
            (["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]), 
            (["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]),
            (["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]),
            (["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]),
        ]

        for i, j, k in P:
            if ( 
                I[y][x] == i[0] and
                I[y][x + 2] == i[2] and
                I[y + 1][x + 1] == j[1] and
                I[y + 2][x] == k[0] and
                I[y + 2][x + 2] == k[2]
            ):
                return 1
        return 0

    T = 0
    for y in range(R):
        for x in range(C):
            T += search(y, x)
    return T


print(one())
print(two())