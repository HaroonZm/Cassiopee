H,W=map(int,input().split())
S=[input() for _ in range(H)]
ans=0
for j1 in range(W):
 for j2 in range(j1+1,W):
  c=0
  for i in range(H):
   if S[i][j1]=='J' and S[i][j2]=='O': c+=1
   elif S[i][j1]=='I' and c>0:
    ans+=c
print(ans)