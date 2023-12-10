inputs = [line.rstrip('\n') for line in open("inputs/07.txt")]

rank = []

from collections import Counter

order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 
              'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def eval(s, n):
    c = Counter(s)
    l = sorted(list(c.values()), reverse=True)
    items = sorted(c.items(), key=lambda x: (-x[1], order[x[0]]))
    print(items)
    if l == [5]:
        return (order[items[0][0]], 0, 0, 0, 0, 0, 0, 0, 0, 0, n)
    elif l == [4,1]:
        return (0, order[items[0][0]], 0, 0, 0, order[items[1][0]], 0, 0, 0, 0, n)
    elif l == [3,2]:
        return (0, 0, order[items[0][0]], order[items[1][0]], 0, 0, 0, 0, 0, 0, n)
    elif l == [3,1,1]:
        return (0, 0, order[items[0][0]], 0, 0, order[items[1][0]], order[items[2][0]], 0, 0, 0, n)   
    elif l == [2,2,1]:
        return (0, 0, 0, order[items[0][0]], order[items[1][0]], order[items[2][0]],0, 0, 0, 0, n)     
    elif l == [2,1,1,1]:
        return (0, 0, 0, order[items[0][0]], 0, order[items[1][0]],order[items[2][0]], order[items[3][0]], 0, 0, n)     
    elif l == [1,1,1,1,1]:
        return (0, 0, 0, 0, 0, order[items[0][0]], order[items[1][0]],order[items[2][0]], order[items[3][0]], order[items[4][0]], n)        
results = []       
for str in inputs:
    s, n = str.split(" ")
    results.append(eval(s, n))
sorted = sorted(results, key=lambda x: tuple(-i for i in x[:10]))
print(sorted)
total = 0
for i, x in enumerate(sorted):
    print(x)
    total += int(x[-1]) * i

print(total)
