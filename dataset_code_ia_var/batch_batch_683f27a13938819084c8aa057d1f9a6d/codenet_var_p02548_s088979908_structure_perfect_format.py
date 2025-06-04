N = int(input())

ans = 0

for a in range(1, N):
    maxb = N // a
    if N % a == 0:
        maxb -= 1
    if maxb > 0:
        ans += maxb

print(ans)