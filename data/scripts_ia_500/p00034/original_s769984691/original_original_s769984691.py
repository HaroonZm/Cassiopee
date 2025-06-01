import sys
def d(o):
 m=o[-2]/sum(o[-2:])
 l=sum(o[:-2])
 p=lambda x:(sum(o[:x])/l)
 for i in range(1,len(o[:-2])+1):
  if p(i)>=m:return i

l=[list(map(int,t.split(","))) for t in sys.stdin]
[print(i) for i in [d(o) for o in l]]