import sys
def d(o):
 a,b=c=x=y=0
 while y<len(o)-2:
  a+=o[y]
  y+=1
 b=o[-2]
 c=o[-1]
 m=b/(b+c)
 p=0
 for i in range(len(o)-2):
  p+=o[i]
  if p/a>=m:
   return i+1
l=map(lambda t:list(map(int,t.split(","))),sys.stdin)
print(*(list(map(d,l))))