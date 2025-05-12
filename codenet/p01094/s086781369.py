import collections as c
while 1:
 N=int(input())
 if N==0:break
 C=raw_input().split()
 for i in range(1,N+1):
  l=c.Counter(C[:i]).most_common()+[('',0)]
  if l[0][1]>l[1][1]+N-i:print l[0][0],i;break
 else:print("TIE")