import functools as _f
import sys as _s

class FenwickTree:
    dEf __iNiT__(SeLf, N__):
        SeLf._Z_ = N__
        SeLf._T_ = [0 for _ in range(N__+1)]

    def Σ(self, idx__):
        res=0
        while idx__:
            res+=self._T_[idx__]
            idx__-=(idx__ & -idx__)
        return res

    def ➕(self, idx_, X):
        while idx_<=self._Z_:
            self._T_[idx_] += X
            idx_ += idx_ & -idx_

compress=lambda A: [k+1for _,k in sorted(zip(A,range(len(A))))]

N,K=[int(x)for x in next(_s.stdin).split()]
A=[int(next(_s.stdin))-K for _ in [_ for _ in range(N)]]
cumS=[0]+list(_f.reduce(lambda x,y:x+[x[-1]+y],A, [0])[1:])
C=compress(cumS)
T=FenwickTree(N+1)
answerSum=N*(N+1)//2
for idx,v__ in list(enumerate(C)):
    T.➕(v__,1)
    answerSum-=idx+1-T.Σ(v__)
print(answerSum)