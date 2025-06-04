import math

def build_tree(vals, init, f):
    size = len(vals)
    n = 2 ** math.ceil(math.log2(size))
    arr = [init] * (n*2)
    j = n
    for v in vals:
        arr[j] = v
        j += 1
    for k in range(j, n*2): arr[k] = init
    h = n-1
    while h > 0:
        arr[h] = f(arr[h<<1], arr[(h<<1)+1])
        h -= 1
    return arr, n

class SegMentT:
    def __init__(self, init_list, default_value, func):
        self.func=func
        self._arr, self._offset = build_tree(init_list, default_value, func)
        self.defv=default_value
    def __call__(self, l,r):
        s, t, res = l+self._offset, r+self._offset, self.defv
        while s < t:
            if s&1: res = self.func(res, self._arr[s]); s += 1
            if t&1: t -= 1; res = self.func(res, self._arr[t])
            s >>= 1; t >>= 1
        return res
    def assign(self, idx, v):
        ind = idx + self._offset
        self._arr[ind] = v
        while ind > 1:
            ind >>= 1
            self._arr[ind]=self.func(self._arr[ind*2], self._arr[ind*2+1])

def get():
    return list(map(int, input().split()))
def _min(x, y): return min(x, y)
def _max(x, y): return max(x, y)
n=int(input())
lst=[]
for z in input().split():
    lst.append(int(z))
q=int(input())
qL=[]
for K in range(q):
    l,r,d = map(int,input().split())
    qL.append((l,r,d,K))
QSO=sorted(qL, key=lambda X:X[2])
l2=sorted(enumerate(lst), key=lambda z_:z_[1])
tree1=SegMentT([-int(1e9)]*n, -int(1e9), _max)
tree2=SegMentT(lst, int(1e9), _min)
idx=0
ans=[0]*q
for l,r,d,qi in QSO:
    while idx<n and l2[idx][1]<=d:
        tree1.assign(l2[idx][0], l2[idx][1])
        tree2.assign(l2[idx][0], int(1e9))
        idx+=1
    v1=abs(tree1(l,r+1)-d)
    v2=abs(tree2(l,r+1)-d)
    ans[qi]=v1 if v1<v2 else v2
print('\n'.join(map(str,ans)))