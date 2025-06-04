import sys
input=sys.stdin.readline

class RollingHash:
    def __init__(self,s,base=1007,mod=10**9+7):
        self.n=len(s)
        self.mod=mod
        self.base=base
        self.pow=[1]*(self.n+1)
        self.hash=[0]*(self.n+1)
        for i,c in enumerate(s):
            self.hash[i+1]=(self.hash[i]*base+ord(c))%mod
            self.pow[i+1]=(self.pow[i]*base)%mod
    def get(self,l,r):
        return (self.hash[r]-self.hash[l]*self.pow[r-l])%self.mod

S=input().rstrip()
Q=int(input())
rh1=RollingHash(S,1007,10**9+7)
rh2=RollingHash(S,2009,10**9+9)

def check(l,r,t):
    length=r-l+1
    if t==length:
        return True
    # vérifier si substring de longueur length-t égale à substring décalée de t
    h1_1 = rh1.get(l-1,r-t)
    h1_2 = rh1.get(l-1+t,r)
    h2_1 = rh2.get(l-1,r-t)
    h2_2 = rh2.get(l-1+t,r)
    if h1_1==h1_2 and h2_1==h2_2:
        return True

    diff=0
    for i in range(l-1,r-t):
        if S[i]!=S[i+t]:
            diff+=1
            if diff>1:
                return False
    return True

for _ in range(Q):
    l,r,t=map(int,input().split())
    print("Yes" if check(l,r,t) else "No")