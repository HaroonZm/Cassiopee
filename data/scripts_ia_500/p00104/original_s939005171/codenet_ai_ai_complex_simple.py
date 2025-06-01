from functools import reduce
from operator import add
from sys import stdin
def f():
    def g():return next(stdin).split()
    h,w=map(int,g())
    while not(h==w==0):
        r=list(map(list,[next(stdin).rstrip('\n') for _ in range(h)]))
        pos=lambda x,y:(x,y)
        i=[0,0]
        def move(c):
            return {'>':(1,0),'<':(-1,0),'v':(0,1),'^':(0,-1),'.':(0,0)}.get(c,(0,0))
        def step():
            i[0],i[1]=i[0]+d[0],i[1]+d[1]
        visited=set()
        loop_detect=lambda p,pvs: p in pvs
        while True:
            p=tuple(i)
            if loop_detect(p,visited):
                print('LOOP')
                break
            visited.add(p)
            c=r[i[1]][i[0]]
            r[i[1]][i[0]]='*'
            if c=='.':
                print(i[0],i[1])
                break
            d=move(c)
            i[0]+=d[0];i[1]+=d[1]
        h,w=map(int,g())
if __name__=='__main__':
    f()