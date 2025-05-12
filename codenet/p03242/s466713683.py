N=input()
ans=[]
for i in range(len(N)):
  if N[i]=="1":
    ans.append(9)
  else:
    ans.append(1)
print(*ans,sep="")