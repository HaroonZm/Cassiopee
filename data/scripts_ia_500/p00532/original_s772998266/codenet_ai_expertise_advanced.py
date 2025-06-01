n, m = int(input()), int(input())
a = list(map(int, input().split()))
p = [0] * n

for _ in range(m):
    b = list(map(int, input().split()))
    for j, val in enumerate(b):
        p[j] += (a[_] == val)
        p[a[_] - 1] += (a[_] != val)

print(*p, sep='\n')