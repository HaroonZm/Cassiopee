from collections import Counter

N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]
A, B, C = zip(*data)

cntA, cntB, cntC = map(Counter, (A, B, C))

for a, b, c in data:
    ans = (a if cntA[a] == 1 else 0) + (b if cntB[b] == 1 else 0) + (c if cntC[c] == 1 else 0)
    print(ans)