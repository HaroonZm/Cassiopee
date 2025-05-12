d = {}
q = int(input())

for i in range(q):
    a = list(input().split())
    if a[0] == '0':
        d[a[1]] = int(a[2])
    else:
        print(d[a[1]])