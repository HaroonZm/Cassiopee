import sys
from collections import Counter
read=sys.stdin.read
n,m=map(int,input().split())
a=list(map(int,read().split()))
c=Counter(a)
ans="YES"
for i in c.values():
  if i%2:
    ans="NO"
print(ans)