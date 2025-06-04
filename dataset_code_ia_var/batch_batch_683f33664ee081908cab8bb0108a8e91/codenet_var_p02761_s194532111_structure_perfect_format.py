n, m = map(int, input().split())
defs = [tuple(map(int, input().split())) for _ in range(m)]

is_empty = False
jouken = {}

for i in range(n):
    dd = list(set([d[1] for d in defs if d[0] - 1 == i]))
    if len(dd) > 1:
        is_empty = True
        break
    elif len(dd) == 1:
        jouken[i] = dd[0]

num = [0] * n

if n == 1:
    if 0 in jouken:
        num[0] = jouken[0]
    else:
        num[0] = 0
else:
    if 0 in jouken:
        if jouken[0] == 0:
            is_empty = True
        else:
            num[0] = jouken[0]
    else:
        num[0] = 1
    for i in range(1, n):
        if i in jouken:
            num[i] = jouken[i]
        else:
            num[i] = 0

num = [str(i) for i in num]

if is_empty:
    print(-1)
else:
    print(''.join(num))