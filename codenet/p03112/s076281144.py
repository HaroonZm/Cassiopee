#abc119d
import bisect

a,b,q=map(int,raw_input().split())
inf=2<<60
s=[-inf]+[int(raw_input()) for i in xrange(a)]+[inf]
t=[-inf]+[int(raw_input()) for i in xrange(b)]+[inf]
s.sort()
t.sort()
for i in xrange(q):
 x=int(raw_input())
 b=bisect.bisect(s,x)
 d=bisect.bisect(t,x)
 res=inf
 for ss in [s[b-1],s[b]]:
  for tt in [t[d-1],t[d]]:
   d1=abs(ss-x)+abs(tt-ss)
   d2=abs(tt-x)+abs(ss-tt)
   res=min(res,d1,d2)
 print res