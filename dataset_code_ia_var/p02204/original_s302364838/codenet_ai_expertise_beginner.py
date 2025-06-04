m, n = map(int, input().split())
a = list(map(int, input().split()))

if m == 2:
    x = 0
    y = 0
    for i in range(n):
        # Première version du motif
        if i % 2 == 0:
            motif1 = 1
            motif2 = 2
        else:
            motif1 = 2
            motif2 = 1
        if a[i] != motif1:
            x += 1
        if a[i] != motif2:
            y += 1
    print(min(x, y))
else:
    x = 0
    for i in range(1, n):
        if a[i-1] == a[i]:
            a[i] = -1
            x += 1
    print(x)