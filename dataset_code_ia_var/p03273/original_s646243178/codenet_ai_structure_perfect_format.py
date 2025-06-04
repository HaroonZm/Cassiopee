h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
c = []
ng_h = []
ng_w = []

for i in range(h):
    ok = True
    for j in range(w):
        if a[i][j] != ".":
            ok = False
            break
    if ok:
        ng_h.append(i)

for i in range(w):
    ok = True
    for j in range(h):
        if a[j][i] != ".":
            ok = False
            break
    if ok:
        ng_w.append(i)

for i in range(h):
    t = ""
    if i in ng_h:
        continue
    for j in range(w):
        if j in ng_w:
            continue
        t += a[i][j]
    if t != "":
        c.append(t)

print(*c, sep='\n')