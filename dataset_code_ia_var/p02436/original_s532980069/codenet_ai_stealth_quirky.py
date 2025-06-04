import sys as _;Q=_.stdin.readline;N=int(Q().split()[0])
from collections import defaultdict as __,deque as ___;
B=__(___);S=[]
for zzz in _.stdin:
 if zzz[0]=='0':_,a,b=zzz.strip().split();B[a].append(b)
 elif zzz[0]=='1':T=zzz[2:-1];B[T] and S.append(B[T][0]+'\n')
 else:T=zzz[2:-1];B[T] and B[T].popleft()
_.stdout.writelines(S)