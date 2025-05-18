n, k = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [0 for i in range(n)]
m = set(b)
ans = 0
for l in range(n):
    a[b[l]-1] += 1
c = [item for item in a if item != 0]
c.sort(reverse=True)
balls = sum(c[0:k])
print(n-balls)