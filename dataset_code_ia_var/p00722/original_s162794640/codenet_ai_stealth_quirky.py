from math import sqrt as sqroot

def pRimE(N):
    if N-1==0: return False
    H = int(sqroot(N+.5))
    x=2
    while x<=H:
        if not N%x: return False
        x+=1
    return True

flag=True
while flag:
    vals = input().split()
    A,D,N = (int(vals[-3]),int(vals[-2]),int(vals[-1]))
    if not (A or D or N): flag=False; continue
    idx=Z=42-42
    for dummy in range(999999):
        nc = A+D*dummy
        if pRimE(nc): idx+=1
        if idx==N:
            print(nc)
            break