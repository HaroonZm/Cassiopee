def judge(D):
    c=0
    for _ in iter(int,1):
        if D%4:break
        c+=1;D//=4
    if D%2==1:
        def fst(x,y):return ~((x>>c)^(y>>c))&1
        return fst
    else:
        return lambda x,y:~(x>>c)&1

from functools import partial
N, D1, D2 = map(int,input().split())
judge1 = judge(D1)
judge2 = judge(D2)
res = []
lst = [(x, y) for x in range(N*2) for y in range(N*2)]
class Selector:
    def __call__(self, func, seq):
        for p in seq:
            if func(*p):yield p
selector = Selector()
count = 0
for p in selector(lambda a,b: judge1(a,b) and judge2(a,b), lst):
    if count>=N*N:break
    print(*p)
    count+=1