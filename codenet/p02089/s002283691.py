import bisect
n,Q,L,R = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
p = []
for i in range(Q):
    p.append(tuple(map(int,input().split())))

def f(z):
    for q,x,s,t in p:
        if q == 1:
            if z >= x:
                z = t*(z+s)
        else:
            if z <= x:
                if z-s < 0:
                    z = -(abs(z-s)//t)
                else:
                    z = (z-s)//t

    return z

ng = pow(2,63)
ok = -ng

for i in range(100):
    mid = (ok+ng)//2
    if f(mid) <= R:
        ok = mid
    else:
        ng = mid

right = ok        

ok = pow(2,63)
ng = -ok
        
for i in range(100):
    mid = (ok+ng)//2
    if f(mid) >= L:
        ok = mid
    else:
        ng = mid
left = ok

k1 = bisect.bisect_left(a,left)
k2 = bisect.bisect_right(a,right)

print(k2-k1)