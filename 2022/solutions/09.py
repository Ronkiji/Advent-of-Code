def one():
    parse = [line.rstrip('\n') for line in open("inputs/09.txt")]
    inputs = [(key, int(val)) for key, val in (line.split(" ") for line in parse)]
    visited = [(0,0)]
    td1 = [(0,1), (1, 0), (-1,0), (0,-1)]
    td2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    hd = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1,1)]
    head = (0, 0)
    tail = (0, 0)

    def update(h, t):
        for hn in hd:
            if t[0] == h[0] + hn[0] and t[1] == h[1] + hn[1]:
                return h, t
        possible = []
        for tn in td1: 
            for hn in hd:
                if (t[0] + tn[0] == h[0] + hn[0]) and (t[1] + tn[1] == h[1] + hn[1]):
                    possible.append((t[0] + tn[0], t[1] + tn[1]))
                    break
            else:
                continue
            break
        for tn in td2: 
            for hn in hd:
                if (t[0] + tn[0] == h[0] + hn[0]) and (t[1] + tn[1] == h[1] + hn[1]):
                    possible.append((t[0] + tn[0], t[1] + tn[1]))
                    break
            else:
                continue
            break
        if len(possible) == 1:
            if possible[0] not in visited:
                visited.append(possible[0])
            return h, possible[0]
        else:
            for p in possible:
                if p[0] == h[0] or p[1] == h[1]:
                    if p not in visited:
                        visited.append(p)
                    return h, p

    for i in inputs:
        if i[0] == "L":
            start = head[0]
            for x in range(1, i[1] + 1):
                head = (start - x, head[1])
                head, tail = update(head, tail)
        elif i[0] == "R":
            start = head[0]
            for x in range(1, i[1] + 1):
                head = (start + x, head[1])
                head, tail = update(head, tail)
        elif i[0] == "U":
            start = head[1]
            for x in range(1, i[1] + 1):
                head = (head[0], start + x)
                head, tail = update(head, tail)
        elif i[0] == "D":
            start = head[1]
            for x in range(1, i[1] + 1):
                head = (head[0], start - x)
                head, tail = update(head, tail)
                
    print(len(visited))

def two():
    parse = [line.rstrip('\n') for line in open("inputs/09.txt")]
    inputs = [(key, int(val)) for key, val in (line.split(" ") for line in parse)]
    visited = [(0,0)]
    td1 = [(0,1), (1, 0), (-1,0), (0,-1)]
    td2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    hd = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1,1)]
    head = (0, 0)
    tails = []
    for x in range(9):
        tails.append((0,0))

    def update(h, t, count=False):
        for hn in hd:
            if t[0] == h[0] + hn[0] and t[1] == h[1] + hn[1]:
                return h, t
        possible = []
        for tn in td1: 
            for hn in hd:
                if (t[0] + tn[0] == h[0] + hn[0]) and (t[1] + tn[1] == h[1] + hn[1]):
                    possible.append((t[0] + tn[0], t[1] + tn[1]))
                    break
            else:
                continue
            break
        for tn in td2: 
            for hn in hd:
                if (t[0] + tn[0] == h[0] + hn[0]) and (t[1] + tn[1] == h[1] + hn[1]):
                    possible.append((t[0] + tn[0], t[1] + tn[1]))
                    break
            else:
                continue
            break
        if len(possible) == 1:
            if count:
                if possible[0] not in visited:
                    visited.append(possible[0])
            return h, possible[0]
        else:
            for p in possible:
                if p[0] == h[0] or p[1] == h[1]:
                    if count:
                        if p not in visited:
                            visited.append(p)
                    return h, p

    for i in inputs:
        # print(i)
        if i[0] == "L":
            start = head[0]
            for x in range(1, i[1] + 1):
                head = (start - x, head[1])
                head, tails[0] = update(head, tails[0])
                for y in range(len(tails)-1):
                    tails[y], tails[y+1] = update(tails[y], tails[y+1], y+2 == len(tails))
        elif i[0] == "R":
            start = head[0]
            for x in range(1, i[1] + 1):
                head = (start + x, head[1])
                head, tails[0] = update(head, tails[0])
                for y in range(len(tails)-1):
                    tails[y], tails[y+1] = update(tails[y], tails[y+1], y+2 == len(tails))
        elif i[0] == "U":
            start = head[1]
            for x in range(1, i[1] + 1):
                head = (head[0], start + x)
                head, tails[0] = update(head, tails[0])
                for y in range(len(tails)-1):
                    tails[y], tails[y+1] = update(tails[y], tails[y+1], y+2 == len(tails))
        elif i[0] == "D":
            start = head[1]
            for x in range(1, i[1] + 1):
                head = (head[0], start - x)
                head, tails[0] = update(head, tails[0])
                for y in range(len(tails)-1):
                    tails[y], tails[y+1] = update(tails[y], tails[y+1], y+2 == len(tails))

    print(len(visited))

one()
two()