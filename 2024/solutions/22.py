inputs = [int(line.rstrip('\n')) for line in open("inputs/22.txt")]

def compute(secret):
    # 1: multiply by 64, XOR, and prune
    secret ^= (secret * 64) % 16777216
    
    # 2: divide by 32 (integer division), XOR, and prune
    secret ^= (secret // 32) % 16777216

    # 3: multiply by 2048, XOR, and prune
    secret ^= (secret * 2048) % 16777216

    # 4: prune
    secret %= 16777216
    return secret

T = 0
prices = []
delta = []
for S in inputs:
    secret = S
    price_list = [S%10]
    for _ in range(2000):
        secret = compute(secret)
        price_list.append(secret % 10)
    T += secret
    prices.append(price_list)
    delta.append([price_list[i] - price_list[i - 1] for i in range(1, len(price_list))])

print(T)

from collections import defaultdict
hashes = defaultdict(int)
visited = defaultdict(set)

for user in range(len(inputs)):
    D = delta[user]
    P = prices[user]
    for i in range(len(D)-3):
        if user not in visited[tuple(D[i:i+4])]:
            hashes[tuple(D[i:i+4])] += P[i+4]
            visited[tuple(D[i:i+4])].add(user)

print(max(hashes.values()))