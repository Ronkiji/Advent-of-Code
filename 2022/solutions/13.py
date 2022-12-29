def compare(left, right):
    if type(left) == type(right) == int:
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1 
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    
    short_length = len(left) if len(left) < len(right) else len(right)
    
    for i in range(short_length):
        state = compare(left[i], right[i])
        if state != 0:
            return state

    if len(left) < len(right):
        return 1
    else:
        return -1
    
import ast
from functools import cmp_to_key

def one():
    inputs = open("inputs/13.txt").read().rstrip().split("\n\n")

    pairs = []

    for i, pair in enumerate(inputs):
        duple = pair.split("\n")
        pairs.append((ast.literal_eval(duple[0]), ast.literal_eval(duple[1])))
        
    counter = 0
    for x in range(len(pairs)):
        p = pairs[x]
        left, right = p[0], p[1]
        counter += x + 1 if compare(left, right) == 1 else 0
    print(counter)

def two():
    inputs = [line.rstrip('\n') for line in open("inputs/13.txt")]

    lists = []
    for line in inputs:
        if line != "":
            lists.append(ast.literal_eval(line))
    lists.append([[2]])
    lists.append([[6]])
    
    lists.sort(key=cmp_to_key(compare), reverse=True)

    print((lists.index([[2]]) + 1) * (lists.index([[6]]) + 1))
    
one()
two()