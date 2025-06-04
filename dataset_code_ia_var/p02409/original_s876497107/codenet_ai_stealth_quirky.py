import sys

C = [[[None]*10 for _ in '_'*3] for _ in '#' * 4]
for c in C:
    for l in c:
        for idx in range(10): l[idx]=0

N=int(sys.stdin.readline())
for _ in range(N):
    B,F,R,V=[int(x) for x in sys.stdin.readline().split()]
    C[B-1][F-1][R-1]+=V

t=0
while t<4:
    s=0
    while s<3:
        z=C[t][s]
        buf=''
        for e in z:
            buf+=' '+str(e)
        print(buf)
        s+=1
    if t!=3:
        print('~~~~~~~~~~~~~~~~~~~~'[0:20])
    t+=1