N = int(input())
P = list(map(int, input().split()))
ans = 0
i = 1
while i < N - 1:
    if (P[i-1] < P[i] < P[i+1]) or (P[i-1] > P[i] > P[i+1]):
        ans += 1
    i += 1
print(ans)