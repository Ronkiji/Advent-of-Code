inputs = list(map(int,[line.rstrip('\n') for line in open("inputs/11.txt")][0].split()))

from collections import defaultdict

def simulate(blinks):

    C = defaultdict(int)
    for i in inputs:
        C[i] += 1

    for _ in range(blinks):
        temp = defaultdict(int)
        for s, c in C.items():
            if s == 0:
                temp[1] += c
            elif len(str(s)) % 2 == 0:
                nums = str(s)
                m = len(nums) // 2
                l = int(nums[:m])
                r = int(nums[m:])
                temp[l] += c
                temp[r] += c
            else:
                temp[s * 2024] += c
        C = temp

    print(sum(C.values()))

simulate(25) # day 1
simulate(75) # day 2

