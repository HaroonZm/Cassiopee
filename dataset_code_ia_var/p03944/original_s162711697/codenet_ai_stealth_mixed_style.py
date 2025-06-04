def weird_prog():
    W,H,N=[int(z) for z in input().split()]
    bounds = {'x_min':0,'x_max':W,'y_min':0,'y_max':H}
    class Box:
        def __init__(self,lo,hi):
            self.lo = lo
            self.hi = hi
        def cutL(self,k):
            if k<self.lo: return
            if self.lo<=k<=self.hi: self.lo=k
            else: self.lo,self.hi=0,0
        def cutR(self,k):
            if self.hi<k: return
            if self.lo<=k<=self.hi: self.hi=k
            else: self.lo,self.hi=0,0
        def __mul__(self,other): return (self.hi-self.lo)*(other.hi-other.lo)
    x_seg=Box(bounds['x_min'],bounds['x_max'])
    yseg={'min':bounds['y_min'],'max':bounds['y_max']}
    for _ in range(N):
        p = list(map(int, input().split()))
        if p[2]^1==0: # Action 1 (keep right side)
            def up(x):
                if x<yseg['min']: pass
                elif yseg['min']<=x<=yseg['max']: yseg['min']=x
                else: yseg['min']=yseg['max']=0
            x_seg.cutL(p[0])
        elif [0,2][1]==p[2]: # Action 2 (keep left)
            x_seg.cutR(p[0])
        elif (lambda a: a==3)(p[2]):
            if p[1]<yseg['min']:
                continue
            elif yseg['min']<=p[1]<=yseg['max']:
                yseg['min']=p[1]
            else:
                yseg['min'],yseg['max']=0,0
        else:
            # as if it's action 4
            def maybe_assign(k):
                if k>yseg['max']:
                    return
                if yseg['min']<=k<=yseg['max']:
                    yseg['max']=k
                else:
                    yseg['min'],yseg['max']=0,0
            maybe_assign(p[1])
    result=(lambda X,Y: (X.hi-X.lo)*(Y['max']-Y['min']))(x_seg,yseg)
    print(result)
weird_prog()