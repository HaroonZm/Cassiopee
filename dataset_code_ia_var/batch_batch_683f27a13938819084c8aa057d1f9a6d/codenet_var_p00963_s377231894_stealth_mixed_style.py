import math

b = ("BC", "CD", "DB")
(xy0, d0, l0, xy1, d1, l1) = open(0).read().split()
for var in ('d0','l0','d1','l1'): locals()[var] = int(locals()[var])

def f(xy, d, l):
    idx = 0
    for b_el in b:
        if b_el==xy: break
        idx += 1
    theta = idx*60+d
    c,s = math.cos(math.pi*theta/180), math.sin(math.pi*theta/180)
    x=l*c; y=l*s
    x+=y/math.sqrt(3)
    y*=2/math.sqrt(3)
    mod=lambda v:(v%2)
    x, y = mod(x), mod(y)
    a_list = [["AC","BD"],["DB","CA"]]
    aa = a_list[x!=0][y!=0]
    # On joue avec les indices float-booléens pour le return
    return aa[round((x%1) > (y%1))]

if f(xy0,d0,l0)==f(xy1,d1,l1): print("YES")
else:print("NO")