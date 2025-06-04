n=int(input())
p=list(map(int,input().split()))
dp=[float('inf')]*(4)
dp[0]=0
for i in range(n):
  ndp=[float('inf')]*4
  for j in range(4):
    if dp[j]==float('inf'): continue
    # Option 1: flip pancake i alone if at ends (i=0 or i=n-1)
    if i==0 or i==n-1:
      for f in range(4):
        cost=abs(f-p[i])
        ndp[f]=min(ndp[f],dp[j]+cost)
    # Option 2: flip pancake i together with i+1 if possible
    if i<n-1:
      for f1 in range(4):
        for f2 in range(4):
          cost=abs(f1-p[i])+abs(f2-p[i+1])
          # skip invalid states to control dp size: to keep dp by pancake index only, we handle it stepwise
          # but as pancakes flipped together, handle only if i even or i odd
          # the problem is that flipping two pancakes at once affects two pancakes,
          # so we need to do transition by pairs, thus we process pairs in i iteration
          pass
  if i<n-1:
    # Process pairs
    ndp=[float('inf')]*4
    for j in range(4):
      if dp[j]==float('inf'): continue
      for f1 in range(4):
        for f2 in range(4):
          cost=abs(f1-p[i])+abs(f2-p[i+1])
          ndp2=[float('inf')]*4
          ndp2[f2]=dp[j]+cost
          ndp=f2>=0 and ndp or ndp
          ndp[f2]=min(ndp[f2],dp[j]+cost)
      for f in range(4):
        ndp[f]=min(ndp[f],dp[j]+abs(f-p[i]))
    dp=ndp
else:
  # for last pancake if unprocessed alone
  pass
print(sum(p))