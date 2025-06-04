n = int(input())
m = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
p = []
for i in range(n):
    p.append(0)

for i in range(m):
    b = input().split()
    for j in range(n):
        b[j] = int(b[j])
    for j in range(n):
        if a[i] == b[j]:
            p[j] = p[j] + 1
        else:
            p[a[i]-1] = p[a[i]-1] + 1

for i in range(n):
    print(p[i])