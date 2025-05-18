import copy
n = int(input())
a = list(map(int, input().split()))
b = copy.deepcopy(a)
b.sort()
loop = []
minp = min(a)
t = [0 for i in range(n)]
while True:
    i = t.index(0)
    j = len(loop)
    loop.append([a[i]])
    t[i] = 1
    while True:
        i = b.index(a[i])
        if t[i] == 1:
            break
        t[i] = 1
        loop[j].append(a[i])
    if sum(t) == n:
        break
    j += 1
cost = 0
for i in loop:
    if len(i) == 1:
        continue
    ps = sum(i)
    pl = len(i)
    pm = min(i)
    p1 = ps + (pl - 2) * pm
    p2 = ps + pm + (pl + 1) * minp
    cost += min(p1, p2)
print(cost)