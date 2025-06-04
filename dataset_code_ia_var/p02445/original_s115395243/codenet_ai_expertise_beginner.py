n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    b, e, t = map(int, input().split())
    if t > b:
        temp1 = a[b:e]
        temp2 = a[e:t]
        a = a[:b] + a[t:e+(t-b)] + temp2 + temp1 + a[e+(t-b):]
    else:
        temp1 = a[t:b]
        temp2 = a[b:e]
        a = a[:t] + temp2 + temp1 + a[e:]
print(*a)