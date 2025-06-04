N,W=[int(x) for x in raw_input().split()]
lst = []; i=0
while i<N:
    lst.append(int(raw_input()))
    i+=1
tmp = sorted(lst)
somme = 0
for x in tmp:
    somme += x
from functools import reduce
dp=[1]+[0]*W
modulo=1000000007
if somme>W:
    result=0
else:
    result=1
for a,idx in enumerate(reversed(range(N+1))):
    try:
        w=tmp[N-1-a]
    except:
        continue
    somme-=w
    left=W-somme
    if left>=0:
        slc = reduce(lambda x, y: x + y, [dp[k] for k in range(max(0,left-w+1),left+1)],0)
        result = (result + slc) % modulo
    j=W
    while j>=w:
        dp[j]=dp[j]+dp[j-w]
        j-=1
print result