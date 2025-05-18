n=int(input())
l=[]
s=0
for i in range(n+2):
  l.append(s)
  s+=i+1
if n not in l:
  print('No')
else:
  k=l.index(n)+1
  ans=[[] for i in range(k)]
  c=0
  for i in range(k):
    for j in range(i+1,k):
      ans[i].append(c+1)
      ans[j].append(c+1)
      c+=1
  print('Yes')
  print(k)
  for i in range(k):
    print(k-1,*ans[i])