from heapq import heappush, heappop

H,W,T,Q = map(int,input().split())

pint = [[0]*(W+1) for _ in range(H+1)]

class Bit2D:
    def __init__(self,H,W):
        self.bit = [[0]*(W+1) for _ in range(H+1)]
    def add(self,a,b,Z):
        x = a
        while x<=H:
            y = b
            yl = self.bit[x]
            while y<=W:
                yl[y]+=Z
                y+=y&-y
            x+=x&-x
    def s_sum(self,a,b):
        ret = 0
        x = a
        while x>0:
            y = b
            yl = self.bit[x]
            while y>0:
                ret+=yl[y]
                y-=y&-y
            x-=x&-x
        return ret

    def ssum(self,x1,y1,x2,y2):
        return self.s_sum(x2,y2) - self.s_sum(x1-1,y2) - self.s_sum(x2,y1-1) + self.s_sum(x1-1,y1-1)
    
    def pprint(self):
        for i in self.bit:
            print(i)
    
    def psum(self,x1,y1,x2,y2):
        return [self.s_sum(x2,y2) , self.s_sum(x1-1,y2) , self.s_sum(x2,y1-1) , self.s_sum(x1-1,y1-1)]

q = []
Yet = Bit2D(H,W)
Fin = Bit2D(H,W)
for i in range(Q):
    t,c,*pos=map(int,input().split())
    while q and q[0][0] <= t:
        _,x,y= heappop(q)
        Yet.add(x,y,-1)
        Fin.add(x,y,1)
        pint[x][y] = 2
    
    if c == 0:
        h,w = pos
        pint[h][w] = 1
        Yet.add(h,w,1)
        heappush(q,(t+T,h,w))
    elif c == 1:
        h,w = pos
        if pint[h][w] == 2:
            Fin.add(h,w,-1)
            pint[h][w] = 0
    else:
        h1,w1,h2,w2 = pos

        print(Fin.ssum(h1,w1,h2,w2),Yet.ssum(h1,w1,h2,w2))