r, c = map(int, input().split())
s = []
T = []
t = 0
for k in range(r):
    x = list(map(int, input().split()))
    y = 0
    for val in x:
        y += val
    x.append(y)
    s.append(x)
i = 0
while i < c + 1:
    t = 0
    j = 0
    while j < r:
        t += s[j][i]
        j += 1
    T.append(t)
    i += 1
s.append(T)
p = 0
while p < r + 1:
    q = 0
    while q < len(s[p]):
        print(s[p][q], end=' ' if q < len(s[p])-1 else '\n')
        q += 1
    p += 1