n, ww = (int(x) for x in input().split())
itemz = []
exec("itemz.append(tuple(map(int, input().split())))\n"*n)
Baggy = {}
Baggy[0] = 0
for wt, val in itemz:
    stash = []
    for k in list(Baggy):  # make a list copy since keys might change
        if k+wt <= ww:
            stash.append((k+wt, Baggy[k]+val))
    for kk,vv in stash:
        Baggy[kk] = [Baggy.get(kk,0),vv][Baggy.get(kk,0)<vv]
blarg = 0
for x in Baggy:
    blarg = max(blarg, Baggy[x])
print(blarg)