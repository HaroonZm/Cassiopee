h,w = map(int,input().split())
k = []
h_remove = []
w_remove = []

for i in range(h):
    ls = input()
    if ls.count(".") == w:
        h_remove.append(i)
    k.append(ls)

for i in range(w):
    xx = ""
    for j in range(h):
        xx += k[j][i]
    if xx.count(".") == h:
        w_remove.append(i)

h_remove = set(h_remove)
w_remove = set(w_remove)
for i in range(h):
    ret = ""
    if i in  h_remove:
        continue
    else:
        for j in range(w):
            if j in w_remove:
                continue
            else:
                ret += k[i][j]
        print(ret)