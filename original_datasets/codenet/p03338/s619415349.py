from collections import Counter

N = int(input())
S = input()

R = Counter(list(S))
L = Counter()

ans = 0
for s in S:
    L[s] += 1
    R[s] -= 1
    ans = max(ans, len((L & R).keys()))

print(ans)