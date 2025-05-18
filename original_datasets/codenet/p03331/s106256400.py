n=input()
if int(n)%10==0:
  print(10)
else:
  print(sum(map(int,list(n))))