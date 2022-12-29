inputs = [line.rstrip('\n') for line in open("inputs/07.txt")][1:]

curr = root = {}
d = []

for line in inputs:
    if line[0: 4] == "$ cd":
        dir = line[5:]
        if dir == "..":
            curr = d.pop()
        else:
            if dir not in curr:
                curr[dir] = {}
            d.append(curr)
            curr = curr[dir]
    elif line[0 : 4] != "$ ls":
        left, right = line.split()
        if left == "dir":
            if right not in curr:
                curr[right] = {}
        else:
            curr[right] = int(left)

def one():

    def find(d):
        if type(d) == int:
            return (d, 0)
        size = 0
        total = 0
        for subdir in d.values():
            s, t = find(subdir)
            size += s
            total += t
        if size <= 100000:
            total += size
        return (size, total)

    print(find(root)[1])

def two():
    
    dirsize = []
    
    def find(d):
        if type(d) == int:
            return (d)
        size = 0
        for subdir in d.values():
            s = find(subdir)
            if type(subdir) is dict:
                dirsize.append(s)
            size += s
        return (size)

    total = find(root)

    for size in dirsize:
        if total - size <= 40000000:
            print(size)
            break
        
one()
two()