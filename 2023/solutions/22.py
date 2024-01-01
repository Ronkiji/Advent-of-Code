inputs = [line.rstrip('\n') for line in open("inputs/22.txt")]
B = []
for brick in inputs:
    l, r = brick.split("~")
    B.append([int(c) for c in l.split(",")] + [int(c) for c in r.split(",")])

D = set()

for i, b1 in enumerate(B):
    for j in range(i, len(B)):
        b2 = B[j]
        if max(b1[2], b1[5]) + 1 == min(b2[2], b2[5]): #b1 under b2
            checkx1 = (b1[0] <= b2[0] <= b1[3] and b1[0] <= b2[3] <= b1[3])
            checky1 = (b1[1] <= b2[1] <= b1[4] and b1[1] <= b2[4] <= b1[4])
            checkx2 = (b2[0] <= b1[0] <= b2[3] and b2[0] <= b1[3] <= b2[3])
            checky2 = (b2[1] <= b1[1] <= b2[4] and b2[1] <= b1[4] <= b2[4])
            print("i", i, j, b1, b2, checkx1, checkx2, checky1, checky2)
            if (checkx1 or checkx2) and (checky1 or checky2):
                D.add(i)
        elif max(b2[2], b2[5]) + 1 == min(b1[2], b1[5]): #b2 under b1
            checkx1 = (b1[0] <= b2[0] <= b1[3] and b1[0] <= b2[3] <= b1[3])
            checky1 = (b1[1] <= b2[1] <= b1[4] and b1[1] <= b2[4] <= b1[4])
            checkx2 = (b2[0] <= b1[0] <= b2[3] and b2[0] <= b1[3] <= b2[3])
            checky2 = (b2[1] <= b1[1] <= b2[4] and b2[1] <= b1[4] <= b2[4])
            print("j", i, j, b1, b2, checkx1, checkx2, checky1, checky2)
            if (checkx1 or checkx2) and (checky1 or checky2):
                D.add(j)

print(D)