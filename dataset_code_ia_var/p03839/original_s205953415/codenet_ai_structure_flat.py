N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])
a_str = input().split()
a = []
i = 0
while i < len(a_str):
    a.append(int(a_str[i]))
    i += 1
b = []
c = []
i = 0
while i < len(a):
    if a[i] > 0:
        b.append(a[i])
    else:
        b.append(0)
    if a[i] < 0:
        c.append(a[i])
    else:
        c.append(0)
    i += 1
d = []
e = []
i = 0
while i < N - K + 1:
    d.append(0)
    e.append(0)
    i += 1
s = 0
t = 0
i = 0
while i < K:
    s += c[i]
    t += b[i]
    i += 1
d[0] = s
e[0] = t
i = 0
while i < N - K:
    d[i+1] = d[i] - c[i] + c[i+K]
    e[i+1] = e[i] - b[i] + b[i+K]
    i += 1
sumb = 0
i = 0
while i < len(b):
    sumb += b[i]
    i += 1
maxd = d[0]
mind = e[0]
i = 1
while i < len(d):
    if d[i] > maxd:
        maxd = d[i]
    if e[i] < mind:
        mind = e[i]
    i += 1
res1 = 0
res2 = sumb + maxd
res3 = sumb - mind
if res1 >= res2 and res1 >= res3:
    print(res1)
elif res2 >= res1 and res2 >= res3:
    print(res2)
else:
    print(res3)