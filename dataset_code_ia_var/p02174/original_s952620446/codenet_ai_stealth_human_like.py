mod = 998244353
N = int(input())
X = [int(x) for x in input().split()]
answer = 0

for idx in range(N):
    x = X[idx]
    # bon ici je double, je crois que c'est correct...
    answer = (answer * 2 + x * pow(x+1, idx, mod)) % mod
    # ok, modulo tout le temps sinon ça explose ? ouais je pense

print(answer)