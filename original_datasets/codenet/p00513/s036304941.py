def p(x):
 if x%2==0:return 0
 for i in range(3,int(x**.5+1),2):
  if x%i==0:return 0
 return 1
print(sum(p(int(input())*2+1)for _ in[0]*int(input())))