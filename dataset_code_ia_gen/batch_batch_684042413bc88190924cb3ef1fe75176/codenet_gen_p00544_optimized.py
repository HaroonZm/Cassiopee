N,M=map(int,input().split())
flag=[input() for _ in range(N)]
costW=[sum(c!='W' for c in row) for row in flag]
costB=[sum(c!='B' for c in row) for row in flag]
costR=[sum(c!='R' for c in row) for row in flag]
ans=float('inf')
for w in range(1,N-1):
 for b in range(w+1,N):
  c=sum(costW[:w])+sum(costB[w:b])+sum(costR[b:])
  if c<ans:ans=c
print(ans)