class LazySegmentTree(object):
    __slots__ = 'n', 'log', 'data', 'lazy', 'me', 'oe', 'fmm', 'fmo', 'foo', 'original_size'

    def __init__(s, in_data, m_id, o_id, fmm, fmo, foo):
        s.fmm = fmm
        s.fmo = fmo
        s.foo = foo
        s.me = m_id
        s.oe = o_id
        s.original_size = len(in_data)
        n = 1
        while n < s.original_size:
            n <<= 1
        s.n = n
        s.log = n.bit_length() - 1
        s.data = [s.me]*(n) + list(in_data) + [s.me]*(n-s.original_size)
        for k in range(n-1,0,-1):
            s.data[k] = s.fmm(s.data[k*2],s.data[k*2+1])
        s.lazy = [s.oe]*(2*n)
    
    def replace(self, idx, val):
        k = idx + self.n
        # push
        for d in range(self.log,0,-1):
            p = k >> d
            x=self.lazy[p]
            self.lazy[p<<1]   = self.foo(self.lazy[p<<1],   x)
            self.lazy[p<<1|1] = self.foo(self.lazy[p<<1|1], x)
            self.data[p]      = self.fmo(self.data[p], x)
            self.lazy[p]      = self.oe
        # set
        self.data[k] = val
        self.lazy[k] = self.oe
        # pull
        while k > 1:
            k >>= 1
            L,R=self.data[k*2],self.data[k*2+1]
            lz,rz=self.lazy[k*2],self.lazy[k*2+1]
            self.data[k]=self.fmm(self.fmo(L,lz),self.fmo(R,rz))
            self.lazy[k]=self.oe

    def effect(self, l, r, op):
        n=self.n
        l+=n;r+=n
        ind=[]
        L=l>>1;R=r>>1
        fl=lambda x:0 if x%2 else (x&-x).bit_length()
        for i in range(self.log):
            if fl(r)%2 or i>=fl(r): ind.append(R)
            if L<R and (fl(l)%2 or i>=fl(l)): ind.append(L)
            L//=2;R//=2
        for j in reversed(ind):
            a=self.lazy[j]
            self.lazy[2*j]=self.foo(self.lazy[2*j], a)
            self.lazy[2*j+1]=self.foo(self.lazy[2*j+1], a)
            self.data[j]=self.fmo(self.data[j], a)
            self.lazy[j]=self.oe
        ll, rr = l, r
        while ll < rr:
            if ll&1:
                self.lazy[ll]=self.foo(self.lazy[ll],op)
                ll+=1
            if rr&1:
                rr-=1
                self.lazy[rr]=self.foo(self.lazy[rr],op)
            ll//=2;rr//=2
        for j in ind:
            a=self.lazy[j]
            l=r=0
            l, r = self.data[j*2], self.data[j*2+1]
            lz, rz = self.lazy[j*2], self.lazy[j*2+1]
            self.data[j]=self.fmm(self.fmo(l,lz),self.fmo(r,rz))
            self.lazy[j]=self.oe

    def folded(self, l, r):
        n = self.n
        l += n
        r += n
        I=[]; L, R = l>>1, r>>1
        fl = lambda x:0 if x%2 else (x&-x).bit_length()
        for i in range(self.log):
            if fl(r)%2 or i>=fl(r): I.append(R)
            if L<R and (fl(l)%2 or i>=fl(l)): I.append(L)
            L//=2; R//=2
        for j in reversed(I):
            x = self.lazy[j]
            self.lazy[2*j]   = self.foo(self.lazy[2*j], x)
            self.lazy[2*j+1] = self.foo(self.lazy[2*j+1], x)
            self.data[j]     = self.fmo(self.data[j], x)
            self.lazy[j]     = self.oe
        x=self.me;y=self.me
        while l<r:
            if l&1:
                x=self.fmm(x,self.fmo(self.data[l],self.lazy[l]))
                l+=1
            if r&1:
                r-=1
                y=self.fmm(self.fmo(self.data[r],self.lazy[r]),y)
            l//=2;r//=2
        return self.fmm(x,y)

def atc2():
    import sys
    input = sys.stdin.buffer.readline
    N,Q = map(int,input().split())
    LL = list(input().split())
    mdata = [(0,1,0) if e==b'1' else (1,0,0) for e in LL]
    fmm = lambda a,b:(a[0]+b[0],a[1]+b[1],a[2]+b[2]+a[1]*b[0])
    def fmo(x,o): return (x[1],x[0],x[0]*x[1]-x[2]) if o else x
    foo=lambda o1,o2:o1^o2
    lst = LazySegmentTree(mdata,(0,0,0),0,fmm,fmo,foo)
    o = []
    for _ in range(Q):
        d = input()
        if not d: break
        x = d.split()
        if x[0]==b'1':
            lst.effect(int(x[1])-1,int(x[2]),1)
        else:
            o.append(lst.folded(int(x[1])-1,int(x[2]))[2])
    print('\n'.join(map(str,o)))

if __name__=='__main__':
    atc2()