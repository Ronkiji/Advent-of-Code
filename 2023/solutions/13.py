inputs = [line.rstrip('\n') for line in open("inputs/13.txt")]
from collections import defaultdict
pz, c = defaultdict(list), 0
for line in inputs:
    if line:
        pz[c].append(line)
    else:
        c += 1

def find1(p):
    for i, line in enumerate(p):
        if i == 0:
            continue
        if line ==  p[i-1]:
            found = True
            l, r = i-1, i
            if l < 0 or r >= len(p):
                found = False
            while l >= 0 and r < len(p):
                if p[l] != p[r]:
                    found = False
                    break
                l -= 1
                r += 1
            if found:
                return i           
    return False

def find2(p):
    for i, line in enumerate(p):
        if i == 0:
            continue
        can_smudge = True
        if line == p[i-1] or sum(char1 != char2 for char1, char2 in zip(line, p[i-1])) == 1:
            found = True
            l, r = i-1, i
            while l >= 0 and r < len(p):
                if p[l] != p[r]:
                    if can_smudge and sum(char1 != char2 for char1, char2 in zip(p[l], p[r])) == 1:
                        can_smudge = False
                    else:
                        found = False
                        break
                l -= 1
                r += 1
            if found and not can_smudge:
                return i           
    return False

t1, t2 = 0, 0
for n, p in pz.items():
    pt = [''.join(row[i] for row in p) for i in range(len(p[0]))]
    s1 = find1(p)
    s2 = find2(p)
    t1 += s1 * 100 if s1 else find1(pt)
    t2 += s2 * 100 if s2 else find2(pt)

print(t1, t2)