#!/usr/bin/env python
import sys, string
from itertools import chain, takewhile as tw

def r(f, *sh, it=chain.from_iterable(sys.stdin), ws=set(string.whitespace)):
 def w():return f("".join(tw(lambda c:c not in ws,it)).strip())
 if not sh:return w()
 if len(sh)==1:return [w()for _ in range(sh[0])]
 if len(sh)==2:return [[w()for _ in range(sh[1])]for __ in range(sh[0])]

def A(*sh, fill=0):
 if len(sh)==1:return [fill]*sh[0]
 if len(sh)==2:return [[fill]*sh[1]for _ in range(sh[0])]

def dbg(**kw):
 print(", ".join(f"{k} = {v!r}" for k,v in kw.items()), file=sys.stderr)

def main():
 while 1:
  h,w,n=map(int,sys.stdin.readline().split())
  if (h,w,n)==(0,0,0):return
  g=[list(map(int,sys.stdin.readline().split()))for _ in range(h)]
  d=A(h,w);d[0][0]=n-1
  for i in range(h):
   for j in range(w):
    c=g[i][j]
    if i<h-1:
     d[i+1][j]+=((d[i][j]+1)//2) if c==0 else (d[i][j]//2)
    if j<w-1:
     d[i][j+1]+=((d[i][j])//2) if c==0 else ((d[i][j]+1)//2)
  for i in range(h):
   for j in range(w):
    g[i][j]=(g[i][j]+d[i][j])%2
  i=j=0
  while i<h and j<w:i,j=(i+1,j)if g[i][j]==0 else(i,j+1)
  print(i+1,j+1)

if __name__=="__main__":main()