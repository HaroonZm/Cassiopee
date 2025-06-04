from functools import reduce
from itertools import chain, tee, starmap, groupby

slices = [(1100,1500,'lunch'), (1800,2100,'dinner'), ((2100,2400),(0,200),'midnight')]

class Dummy: pass

while True:
    try:
        N = int((lambda x: x())(input))
    except: break
    if N==0: break

    entries = list(starmap(lambda s0,s1: (
        lambda h,m,m1: (h*100+m, m, int(s1), int(s1)<m and int(s1)+60 or int(s1))
        )(*chain(map(int,s0.split(":")), [int(s1)]))
    , (input().split() for _ in range(N))))

    def is_time_in_range(tm, sl):
        if isinstance(sl[0], tuple):
            return any(a<=tm<b or (a>b and (tm>=a or tm<b)) for a,b in sl[:-1])
        a,b = sl[:-1]
        return a<=tm<b

    groups = dict()
    for sl in slices:
        lbl = sl[-1]
        filtered = list(filter(lambda v,sl=sl: is_time_in_range(v[0], sl), entries))
        correct = list(filter(lambda x: (x[3]-x[1])<=8, filtered))
        groups[lbl] = (len(correct), len(filtered))

    for lbl in ['lunch','dinner','midnight']:
        num,den = groups[lbl]
        print(lbl, (lambda n,d:'no guest' if not d else n*100//d)(num,den))