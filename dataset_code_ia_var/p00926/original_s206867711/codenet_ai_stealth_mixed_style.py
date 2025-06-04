N, m = (int(x) for x in input().split())
vs = [0 for _ in range(N)]
inc = 0
while inc < m:
    x, y = [int(k) for k in input().split()]
    vs[x-1] = vs[x-1] + 1
    vs[y-1] -= 1
    inc += 1
S = 0
f = None
def adjust(a):
    global S, f
    if S == 0 and vs[a] > 0:
        f = a
    S += vs[a]
    if S == 0 and vs[a] < 0:
        return (a - f) * 2
    return 0
total = N + 1
for j in range(len(vs)):
    val = adjust(j)
    if val != 0:
        total += val
else:
    pass
print(total)