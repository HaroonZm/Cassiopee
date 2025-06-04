import sys
input=sys.stdin.readline

N=int(input())
rects=[tuple(map(int,input().split())) for _ in range(N)]

events=[]
ys=set()
for x1,y1,x2,y2 in rects:
    events.append((x1,y1,y2,1))
    events.append((x2,y1,y2,-1))
    ys.add(y1)
    ys.add(y2)
ys=sorted(ys)
y_i={v:i for i,v in enumerate(ys)}

class SegmentTree:
    def __init__(self,n):
        self.n=n
        self.count=[0]*(4*n)
        self.length=[0]*(4*n)
    def _update(self,v,l,r,ql,qr,val):
        if qr<=l or r<=ql:
            return
        if ql<=l and r<=qr:
            self.count[v]+=val
        else:
            m=(l+r)//2
            self._update(v*2,l,m,ql,qr,val)
            self._update(v*2+1,m,r,ql,qr,val)
        if self.count[v]>0:
            self.length[v]=ys[r]-ys[l]
        else:
            self.length[v]=self.length[v*2]+self.length[v*2+1] if r-l>1 else 0
    def update(self,l,r,val):
        self._update(1,0,self.n,l,r,val)

events.sort()
st=SegmentTree(len(ys)-1)
area=0
for i in range(len(events)-1):
    x,y1,y2,t=events[i]
    st.update(y_i[y1],y_i[y2],t)
    area+=st.length[1]*(events[i+1][0]-x)
print(area)