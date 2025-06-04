N=int(input())
s=input()
t=input()

def y(a,b):
 ans=2*a
 for i in range(a):
  if ''.join([s[-1-i+j] for j in range(i+1)]) == ''.join([t[j] for j in range(i+1)]):
    ans=2*a-i-1
 return ans

class X:
 def __init__(self,v):self.v=v
 def out(self):print(self.v)

result=y(N,t)
X(result).out()