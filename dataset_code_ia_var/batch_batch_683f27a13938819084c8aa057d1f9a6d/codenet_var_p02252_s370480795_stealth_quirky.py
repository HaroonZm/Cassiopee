def stl(x):return list(map(int, x.split()))
E,P=stl(input())
S=[(*divmod(*stl(input()))[::-1],*stl(input())) for _ in range(E)]
T=[]
for idx in range(E):T.append(tuple([S[idx][1]/S[idx][0]]+list(S[idx][::-1][1:3])))
T.sort(key=lambda a: -a[0])
A=0
while P and T:
    Q=T.pop(0)
    d=min(Q[2],P)
    P-=d
    A+=(d*Q[1])/Q[2]
print(A)