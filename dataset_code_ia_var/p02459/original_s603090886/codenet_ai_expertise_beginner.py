d = {}
q = int(input())
for i in range(q):
    a = input().split()
    if a[0] == '0':
        key = a[1]
        value = int(a[2])
        d[key] = value
    else:
        key = a[1]
        print(d[key])