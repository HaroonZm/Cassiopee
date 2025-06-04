P = list(map(lambda x: list(map(int, input().split())), [None]*5))

def f_decomp(a):
    L = []
    for idx in [0,1,2]:
        L.append(P[a][idx] - P[0][idx])
    return L

A = []
for _ in range(9):
    A.append(0)

V = f_decomp(1)
for cnt in range(3):
    val = f_decomp(cnt+2)
    for j, k in enumerate([cnt, cnt+3, cnt+6]):
        A[k] = val[j]

def det(lst):
    u,v,w,x,y,z,s,t,r = lst
    m = u*y*r + x*t*w + s*v*z - u*t*z - x*v*r - y*s*w
    return m

def F(a):
    tmp = []
    for z in A:
        tmp.append(z)
    for idx, pos in enumerate(range(a,9,3)):
        tmp[pos] = V[idx]
    res = det(tmp)/float(D0)
    return res

hit = False
D0 = det(A)
if D0!=0:
    res1 = F(0)
    res2 = F(1)
    res3 = F(2)
    check = (lambda x,y,z: x>=0 and y>=0 and z>=0 and (x+y+z)>=1)
    if check(res1,res2,res3):
        hit = True

print(["HIT","MISS"][not hit])