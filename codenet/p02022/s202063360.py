N, M = [int(x) for x in input().split()]

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

cntA = [0] * 1001
cntB = [0] * 1001

for a in A:
    cntA[a] = cntA[a] + 1

for b in B:
    cntB[b] = cntB[b] + 1

ans = 0
for a in range(1001):
    for b in range(1001):
        ans = ans + (a * b * cntA[a] * cntB[b])

print(ans)