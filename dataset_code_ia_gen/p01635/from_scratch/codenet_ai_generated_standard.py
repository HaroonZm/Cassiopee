n,T=map(int,input().split())
poly=input().replace(' ','').split('+')
total=0
for mono in poly:
    k=int(mono[2:])
    val=pow(n,k)
    total+=val
ans=total*T
print(ans if ans<=10**9 else 'TLE')