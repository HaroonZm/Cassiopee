import sys,bisect,math
A,B = map(int,sys.stdin.readline().split())
res = A//B
if res < 0 and A%B!=0:
  print(res+1)
  exit()
print(res)