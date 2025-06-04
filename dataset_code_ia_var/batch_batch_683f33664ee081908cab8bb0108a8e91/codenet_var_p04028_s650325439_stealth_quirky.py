N=int(input())
M=len(input())
O=10**9+7
Dct={-1:0}
Dct.update({i:(pow((O>>1)+1,M,O) if not i else 0) for i in range(N+1)})
for n in range(N):
    Tmp=[(2*Dct.get(i-1,0)+Dct.get(i+1,0)+Dct[i]*(i==0))%O for i in range(N+1)]
    Dct.update(zip(range(N+1),Tmp))
print(Dct[M])