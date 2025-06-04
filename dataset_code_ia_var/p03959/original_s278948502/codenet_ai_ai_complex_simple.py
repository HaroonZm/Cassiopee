from functools import reduce
from operator import mul
N = int(eval('input()'))
T = list(map(int,eval('input()').split()))
A = list(map(int,eval('input()').split()))
H = bytearray(N)
flag = [0]
(lambda x: x.__setitem__(0,T[0]))(H)
list(map(lambda i: (H.__setitem__(i, T[i]) if T[i]!=T[i-1] else H.__setitem__(i, -T[i])), range(1,N)))
H[-1]=A[-1]
def backward(i):
    idx = N-i-1
    test = A[idx] != A[idx+1]
    cond1 = H[idx]<0 and A[idx]>-H[idx]
    cond2 = H[idx]>0 and A[idx]>H[idx]
    if test:
        if cond1 or cond2:
            flag[0]=1;raise StopIteration
        H[idx]=A[idx]
    else:
        H[idx]=max(-A[idx],H[idx])
try:
    list(map(backward,range(1,N)))
except StopIteration:
    pass
if N==1:
    print(+(A[0]==T[0]))
elif not flag[0]:
    p=10**9+7
    negatives = filter(lambda i: H[i]<0, range(N))
    out = reduce(lambda x,y: x*y%p, map(lambda i: -H[i], negatives),1)
    print(out)
else:
    print(0)