from collections import defaultdict, Counter
def inpl(): return list(map(int, input().split()))

N, M = inpl()
X = sorted(inpl())
C = Counter(X)
D = defaultdict(int)
E = defaultdict(int)
for k, v in C.items():
    D[k%M] += v
    E[k%M] += v//2

ans = D[0] // 2

for i in range(1, M):
    j = M - i
    if i < j:
        x = min(D[i], D[j])
        y = min((D[i] - x)//2, E[i]) + min((D[j] - x)//2, E[j])
        ans += x + y
    elif i == j:
        ans += D[i] //2
    else:
        break

print(ans)