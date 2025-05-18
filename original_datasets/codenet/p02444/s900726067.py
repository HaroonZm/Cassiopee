n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    b, m, e = map(int, input().split())
    tmp = a[b:e]
    a = a[:b] + tmp[m-b:] + tmp[:m-b] + a[e:]
print(*a)