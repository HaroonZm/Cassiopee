import math

N=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))

p=0
q=0

for i in range(N):
  n = P[i]-1
  
  for j in range(i):
    if P[j]<P[i]:
      n -= 1
  
  p += n*math.factorial(N-(i+1))

for i in range(N):
  n = Q[i]-1
  
  for j in range(i):
    if Q[j]<Q[i]:
      n -= 1
  
  q += n*math.factorial(N-(i+1))

print(abs(p-q))