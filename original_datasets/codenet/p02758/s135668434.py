import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

n=int(readline())
segSize=n+1
def init_max(init_max_val):
    for i in range(segSize):
        seg_max[i+num_max-1]=init_max_val[i]
    for i in range(num_max-2,-1,-1) :
        seg_max[i]=max(seg_max[2*i+1],seg_max[2*i+2]) 
    
def update_max(k,x):
    k += num_max-1
    seg_max[k] = x
    while k:
        k = (k-1)//2
        seg_max[k] = max(seg_max[k*2+1],seg_max[k*2+2])
    
def query_max(p,q):
    if q<=p:
        return ide_ele_max
    p += num_max-1
    q += num_max-2
    res=ide_ele_max
    while q-p>1:
        if p&1 == 0:
            res = max(res,seg_max[p])
        if q&1 == 1:
            res = max(res,seg_max[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res,seg_max[p])
    else:
        res = max(max(res,seg_max[p]),seg_max[q])
    return res
ide_ele_max = 0
num_max =2**(segSize-1).bit_length()
seg_max=[ide_ele_max]*2*num_max
mod=998244353

m = map(int,read().split())
XD = sorted(zip(m,m))
X=[x for x,d in XD]

from bisect import bisect_right
X=[bisect_right(X,x+d-1)for x,d in XD]

init_max(list(range(segSize)))
update_max(n,n)
combs=[1]*(n+1)
t=0
for x,d in reversed(XD):
    idx=n-1-t
    t+=1
    p=X[idx]
    p=query_max(idx,p)
    update_max(idx,p)
    combs[idx]=(combs[p+1]+combs[idx+1])%mod
print(combs[0])