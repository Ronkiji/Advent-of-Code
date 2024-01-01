from itertools import product
import re

inputs = [line.rstrip('\n') for line in open("inputs/12.txt")]
total = 0
for line in inputs:
    string, nums = line.split(" ")
    nums = [int(i) for i in nums.split(",")]
    # nums *= 5
    # string = "?".join(string for _ in range(5))

    options = ['#', '.']
    positions = [i for i, char in enumerate(string) if char == '?']
    combos = product(options, repeat=len(positions))

    results = []
    for combo in combos:
        temp = list(string)
        for pos, o in zip(positions, combo):
            temp[pos] = o
        results.append(''.join(temp))

    pattern = "^\.*"
    for n in nums:
        pattern += "#" * n + r'\.+'
    pattern = pattern[:-3] + "\.*$"
    
    for r in results:
        if re.search(pattern, r):
            total += 1

print(total)
