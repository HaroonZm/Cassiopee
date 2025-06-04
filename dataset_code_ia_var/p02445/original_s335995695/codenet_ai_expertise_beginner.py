n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    b, e, t = map(int, input().split())
    s = t + e - b
    if t > b:
        first = a[:b]
        second = a[t:s]
        third = a[e:t]
        fourth = a[b:e]
        fifth = a[s:]
        a = first + second + third + fourth + fifth
    else:
        first = a[:t]
        second = a[b:e]
        third = a[s:b]
        fourth = a[t:s]
        fifth = a[e:]
        a = first + second + third + fourth + fifth
print(*a)