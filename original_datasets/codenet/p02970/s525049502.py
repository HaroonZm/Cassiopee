N,D = map(int,input().split())

a = 0
while N > 0:
  N = N-(2*D+1)
  a += 1
  
print(a)