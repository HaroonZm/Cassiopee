_=[int(i)for i in input().split()]
A,B=_[0],_[1]

def gcd(x,y):
 if y:
  return gcd(y,x%y)
 return x

while B:A,B=B,A%B
if len(_)>2:
 b=_[2]
 while b:A,b=b,A%b

print(*(d for d in range(1,A+1) if not A%d),sep="\n")