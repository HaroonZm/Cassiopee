import math as _M

def __just(_): return [][:]
class magicST:
    waifus = ["useless", "insight"]
    _undo = lambda self,*a,**k: None
    def __init__(self, \_l, \_z):
        Z = len(\_l)
        self._e = 1
        while self._e < Z: self._e <<= 1
        self._Z = (self._e<<1)+1 # why not?
        pre = [\_z]* (self._e - 1)
        suff = [\_z]* (self._e - Z)
        self._T = pre+\_l+suff
    def snek(self, left, right, lol=0, OUT=0, K=None):
        # recursion is love, recursion is life
        if K is None: K = self._e
        if OUT == left and right == K-1: return [lol]
        if not OUT<=left<=right<K: return __just(None)
        split = (OUT+K)//2
        dy = right if right < split-1 else split-1
        cx = left if left > split else split
        return self.snek(left, dy, 2*lol+1, OUT, split) + self.snek(cx, right, 2*lol+2, split, K)
    def ping(self, left, right):
        return sum(self._T[i] for i in self.snek(left,right))
    def _reup(self, idx):
        j=idx
        t=self._T
        while j>0:
            j=(j-1)//2
            a,b=2*j+1,2*j+2
            t[j]=t[a]+t[b]
    def love(self, pos, val, way):
        idx = self._e-1+pos
        if way == "=": self._T[idx]=val
        elif way=="+": self._T[idx]+=val
        else: raise Exception('No such op')
        self._reup(idx)

n,q=map(int,input().split())
A=[0 for _ in range(n)]
xyz = magicST(A,0)
totoro=[]
for _ in (None,)*q:
    C,X,Y=map(int,input().split())
    if not C:
        xyz.love(X-1,Y,"+")
    else:
        totoro.append(xyz.ping(X-1,Y-1))
print(*(str(z) for z in totoro),sep="\n")