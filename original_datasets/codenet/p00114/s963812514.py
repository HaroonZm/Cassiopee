from fractions import gcd
def lcm(a,b):
    return a*b/gcd(a,b)
def ge(a,m):
    for aa,mm in zip(a, m): 
        i, b = 1, aa%mm
        while b!=1:
            b = (aa*b)%mm
            i += 1
        yield i
while True:
    tmp = map(int, raw_input().split(" "))
    if all(t==0 for t in tmp):
        break
    print reduce(lcm,ge(tmp[::2],tmp[1::2]))