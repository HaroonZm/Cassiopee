n=int(input())
S=input()

ans=0
for i in range(1,n+1):
  X=S[:i]
  Y=S[i:]
  tmp=[]
  for x in X:
    if x in Y:
      tmp.append(x)
  ans=max(ans,len(list(set(tmp))))
print(ans)