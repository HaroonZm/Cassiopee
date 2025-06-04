n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    b, e = map(int, input().split())
    a = a[:b] + a[b:e][::-1] + a[e:]
print(*a)