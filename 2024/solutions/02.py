inputs = [list(map(int, line.rstrip('\n').split())) for line in open("inputs/02.txt")]

def safe(L):

    diffs = [L[i + 1] - L[i] for i in range(len(L) - 1)] 

    if not (all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)): 
        return False
    
    if all(1 <= abs(diff) <= 3 for diff in diffs):
        return True 
    return False

def one():
    T = 0
    for L in inputs:
        if safe(L):
            T += 1
    return T

def two():
    T = 0
    for L in inputs:
        for i in range(len(L)):
            mod = L[:i] + L[i + 1:]  # Remove the i-th level
            if safe(mod):
                T += 1
                break
    return T

print(one())
print(two())