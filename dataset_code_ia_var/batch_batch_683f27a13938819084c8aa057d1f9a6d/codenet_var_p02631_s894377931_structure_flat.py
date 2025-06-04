n = int(input())
a = list(map(int, input().split()))
p = []
for j in range(30):
    p.append(2 ** j)
t = 0
for i in range(n):
    t = t ^ a[i]
i = 0
while i < n:
    ans = 0
    j = 0
    while j < 30:
        ans = ans + p[j] * (((a[i] ^ t) // p[j]) % 2)
        j += 1
    print(ans, end=" ")
    i += 1