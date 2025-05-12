MOD=10**9+7
N=int(input())

clist=[]
for i in range(N):
  c=int(input())
  clist.append(c)  
#print(clist)

c2list=clist[:1]
for i in range(1,N):
  if clist[i]!=c2list[-1]:
    c2list.append(clist[i])
#print(c2list)
N2=len(c2list)

cdic={}
for i in range(N2):
  c=c2list[i]
  if not c in cdic:
    cdic[c]=[i]
  else:
    cdic[c].append(i)
#print(cdic)

dp=[1]+[0]*(N2-1)
for i in range(1,N2):
  c=c2list[i]
  dp[i]=dp[i-1]
  
  if len(cdic[c])<5:
    for j in reversed(cdic[c]):
      if j<i:
        dp[i]+=dp[j]
        break
  else:
    l,r=0,len(cdic[c])
    while(l<=r):
      mid=(l+r)//2
      if cdic[c][mid]<i and cdic[c][mid+1]>=i:
        dp[i]+=dp[cdic[c][mid]]
        break
      elif cdic[c][mid]>=i:
        r=mid-1
      elif cdic[c][mid+1]<i:
        l=mid+1
      else:
        print("error")
    
#print(dp)
print(dp[-1]%MOD)