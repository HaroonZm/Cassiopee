import sys as s

def I():
 i=input
 R=map
 r=int
 return list(R(r,i().split()))

def G(a,b):
 if b==0:return a
 if a<b: return G(b,a)
 return G(b,a%b)

def M():
 d=[]
 for l in s.stdin:
  d+=[l.split()]
 n=len(d)
 i=0
 while i<n:
  x,y=map(int,d[i])
  g=G(x,y)
  L=(x//g)*y
  print(f"{g} {L}")
  i+=1

if __name__=="__main__":
 M()