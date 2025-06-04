n = int(input())
alst = []
tmp = input().split()
for v in tmp:
    alst.append(int(v))
wlst = [*map(int, input().split())]

def group(arr1, arr2):
    lft = []
    rgt = []
    for i in range(len(arr1)):
        if arr1[i] == 0:
            rgt.append(arr2[i])
        elif arr1[i] == 1:
            lft.append(arr2[i])
    return lft, rgt

lf, rt = group(alst, wlst)

from functools import reduce

if len(lf) > 0 and len(rt) > 0:
    mlf = reduce(lambda x,y: x if x < y else y, lf)
    mrt = min(rt)
    print((lambda x, y: x + y)(mlf, mrt))
else:
    def show(z): print(z)
    show(0)