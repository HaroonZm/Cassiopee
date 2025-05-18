import math

N=int(input())

def ff(x):
    L=int(math.sqrt(x))

    FACT=dict()

    for i in range(2,L+2):
        while x%i==0:
            FACT[i]=FACT.get(i,0)+1
            x=x//i

    if x!=1:
        FACT[x]=FACT.get(x,0)+1

    return FACT

# 拡張ユークリッドの互除法.ax+by=gcd(a,b)となる(x,y)を一つ求め、(x,y)とgcd(x,y)を返す.
def Ext_Euc(a,b,axy=(1,0),bxy=(0,1)): # axy=a*1+b*0,bxy=a*0+b*1なので,a,bに対応する係数の初期値は(1,0),(0,1)
    # print(a,b,axy,bxy)
    q,r=divmod(a,b)

    if r==0:
        return bxy,b # a*bxy[0]+b*bxy[1]=b
   
    rxy=(axy[0]-bxy[0]*q,axy[1]-bxy[1]*q) # rに対応する係数を求める.
    return Ext_Euc(b,r,bxy,rxy)

FACT=ff(N*2)
LIST=[]
for f in FACT:
    LIST.append(f**FACT[f])
    
L=len(LIST)

LANS=2*N-1

for i in range(1<<L):
    A=1
    B=1
    for j in range(L):
        if i & (1<<j)!=0:
            A*=LIST[j]
        else:
            B*=LIST[j]
    if A==1 or B==1:
        continue

    x,_=Ext_Euc(A,-B)
    x,y=x[0],x[1]

    if x<0:
        x+=(1+abs(x)//B)*B

    LANS=min(LANS,x*A)

print(LANS)