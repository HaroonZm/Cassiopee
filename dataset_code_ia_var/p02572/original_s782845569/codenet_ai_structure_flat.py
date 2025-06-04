n = int(input())
a = list(map(int, input().split()))
ans = 0
keisu = [0] * n
t = 0

i = 0
while i < n:
    keisu[i] += t
    t += a[i]
    i += 1

i = 0
while i < n:
    ans += a[i] * keisu[i]
    i += 1

print(ans % (1000000000 + 7))