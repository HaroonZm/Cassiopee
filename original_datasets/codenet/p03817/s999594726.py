n=int(input())
if n<7: 
  print(1);exit()
print(n//11*2+(n%11>0)+(n%11>6))