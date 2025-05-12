n,p,q = map(int,input().split())
cn=[]
for i in range(n):
    cn.append(int(input()))
difs=[p*(q-i)-cn[i] for i in range(n)]
difs=sorted(difs, reverse=True)
ans=[sum(cn)]
for i in range(n):
    ans.append(ans[-1]+2*i*p+difs[i])
print(max(ans))