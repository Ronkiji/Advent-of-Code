parse = [(line.rstrip('\n')) for line in open("inputs/01.txt")]
left = [int(key) for key, val in (line.split() for line in parse)]
right = [int(val) for key, val in (line.split() for line in parse)]

left, right = sorted(left), sorted(right)

def one():
    return sum(abs(x-y) for x, y in zip(left, right))

def two():
    from collections import Counter
    d = Counter(right)
    return sum(y * d[y] for y in left if y in d)

print(one())
print(two())