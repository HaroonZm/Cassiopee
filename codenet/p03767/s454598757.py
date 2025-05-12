n = int(input())
a = list(map(int, input().split()))
a.sort()
s = 0
for i in range(n):
    s += a[i * 2 + n]
print(s)