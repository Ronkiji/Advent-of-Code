lines = [line.rstrip('\n') for line in open("inputs/19.txt")]

patterns = lines[0].split(", ")

def dp(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for p in patterns:
            if i >= len(p) and s[i-len(p):i] == p:
                dp[i] += dp[i-len(p)]
    return dp[n]
T=0
for s in lines[2:]:
    if dp(s): 
        T += 1
print(T)
print(sum(dp(s) for s in lines[2:]))
