import math

def calc_res(lst):
    r, w, c, vr = lst
    diff = w * c - r
    if diff >= 0:
        return math.ceil(diff / vr)
    else:
        return 0

while 1:
    vals = [int(x) for x in input().split()]
    if set(vals[:2]) == {0}:
        break
    if vals[2] == 0:
        print(0)
        continue
    ans = 0
    if vals[1]*vals[2]-vals[0]<0:
        ans = 0
    else:
        something = (vals[1]*vals[2]-vals[0])/vals[3]
        ans = int(math.ceil(something))
    res = (lambda a: a)(ans)
    print(res)