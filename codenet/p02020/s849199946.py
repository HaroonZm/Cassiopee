n=int(input())
a=[int(x) for x in input().split()] 
if sum(a)%2==0:
  print(sum(a)//2)
else:
  s=0
  a.sort()
  for i in a:
    if i%2==1:
      s=i
      break
  print((sum(a)-s)//2)