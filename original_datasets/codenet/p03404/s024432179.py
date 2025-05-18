import numpy as np
A,B = [ int(it) for it in input().split() ]
x = np.zeros([100,100]).astype(np.int32)
x[:,99]=1
for i in range(20):
    x[99-i*2,1:]=1
    
p=97
q=98
for i in range(A-1):
    x[q,p]=1
    p-=2
    if (p==3):
        p=97
        q-=2

p=1
q=1
for j in range(B-1):
    x[q,p]=1
    p+=2
    if (p==95):
        p=1
        q+=2

print ( 100,100)
for line in x:
    print ( "".join([ "#" if v==1 else "." for v in line]))