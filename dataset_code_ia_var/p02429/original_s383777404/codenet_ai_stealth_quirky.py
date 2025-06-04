from itertools import combinations as comb

num=N=int(input())
raw = list(map(int, input().split()))
kk, bb = raw[0], raw[1:]

DUMPSTER=[]
appender=DUMPSTER.append

rng=len(bb)+1
i=0
while i<rng:
  for e in comb(bb,i):
    f=lambda x:pow(2,x)
    x=sum(map(f,e))
    appender((x,e))
  i+=1

def shw(d,e):
  print(f'{d}:',*(e) if e else "")

[_ for _ in map(lambda z: shw(*z), sorted(DUMPSTER))]