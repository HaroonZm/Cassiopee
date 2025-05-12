# A Point in a Triangle
import math
def simul_eq(a,b,c,d,e,f):
    # A = [[a,b],[d,e]]
    C = [c,f]
    detA = a*e - b*d
    # if detA == 0: raise # det(A) == 0.
    At = [[e,-b],[-d,a]]
    x = sum(map((lambda x,y: x*y), At[0], C)) / detA
    y = sum(map((lambda x,y: x*y), At[1], C)) / detA
    return (x,y)
ss = input().split()
while 1:
    x1,y1,x2,y2,x3,y3,xp,yp = map(float,ss)
    s,t = simul_eq(x2-x1, x3-x1, xp-x1, y2-y1, y3-y1, yp-y1)
    if 0 < s < 1 and 0 < t < 1 and 0 < s + t < 1:
        print('YES')
    else:
        print('NO')
    try: ss = input().split()
    except EOFError: break