import collections
from math import *
s=input()
a=collections.Counter(s)
o=0
for x in a:
    if a[x]&1:
        o+=1
        if o>1:print(0);break
        a[x]-=1
else:
    b=factorial(len(s)//2)
    for x in a.values():
        b//=factorial(x//2)
    print(b)