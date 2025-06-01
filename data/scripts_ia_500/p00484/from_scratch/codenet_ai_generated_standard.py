n,k=map(int,input().split())
books=[[] for _ in range(11)]
for _ in range(n):
 c,g=map(int,input().split())
 books[g].append(c)
for i in range(1,11):
 books[i].sort(reverse=True)
dp=[[-10**15]*(k+1) for _ in range(11)]
dp[0][0]=0
for i in range(1,11):
 cumsum=[0]
 for j,price in enumerate(books[i],1):
  cumsum.append(cumsum[-1]+price+j-1)
 m=len(books[i])
 for j in range(k+1):
  for x in range(min(m,j)+1):
   val=dp[i-1][j-x]+cumsum[x]
   if val>dp[i][j]:
    dp[i][j]=val
print(dp[10][k])