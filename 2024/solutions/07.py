inputs = [line.rstrip('\n') for line in open("inputs/07.txt")]
from itertools import product

def evaluate(A, N, Q=1):
    ops = ['+', '*', '||'] if Q == 2 else ['+', '*']
    gaps = len(N) - 1
    
    for ops in product(ops, repeat=gaps):
        ans = N[0]
        for num, op in zip(N[1:], ops):
            if op == '+':
                ans += num
            elif op == '*':
                ans *= num
            elif op == '||':
                ans = int(str(ans) + str(num))

        if ans == A:
            return True
    return False

T1 = 0
T2 = 0
for line in inputs:
    A, N = line.split(":")
    A = int(A)
    N = [int(x) for x in N.strip().split()]

    if evaluate(A, N):
        T1 += A
    if evaluate(A, N, Q=2):
        T2 += A

print(T1)
print(T2)