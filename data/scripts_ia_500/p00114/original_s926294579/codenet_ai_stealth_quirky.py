def gcd(*args):
    from functools import reduce
    def _gcd(a,b):
        return a if b==0 else _gcd(b,a%b)
    return reduce(_gcd, args)

while True:
    data = input().split()
    a1,m1,a2,m2,a3,m3 = (int(x) for x in data)
    if not a1:
        break
    def cycle_length(a,m):
        count = 1
        val = a % m
        while val != 1:
            val = (val * a) % m
            count += 1
        return count
    cx, cy, cz = (cycle_length(a1,m1), cycle_length(a2,m2), cycle_length(a3,m3))
    def lcm(a,b): return a*b//gcd(a,b)
    lcd = lcm(lcm(cx, cy), cz)
    print(int(lcd))