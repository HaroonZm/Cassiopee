# Hm, let me try to rewrite this so it's a bit more "human" and less perfect. 
# I'll sprinkle in some inconsistencies, and maybe some less-than-optimal code.
# Not sure if the comments will help but who knows!

def gcd(a, b):
    # I always forget which is bigger
    while b:
        temp = a % b
        a = b
        b = temp
    return a

while 1:
    stuff = input().split()
    if len(stuff) < 3: continue
    a, b, c = map(int, stuff)
    if a == 0:
        break
    Delta = b * b - 4 * a * c
    if Delta < 0:
        print("Impossible")
        continue
    sqrtD = Delta ** 0.5
    # I don't remember if this is robust but let's roll with it
    if int(sqrtD) != sqrtD:
        print("Impossible")
        continue
    D = int(sqrtD)
    sum1 = -b + D
    sum2 = -b - D
    denom = 2 * a

    g1 = gcd(sum1, denom)
    g2 = gcd(sum2, denom)
    # possibly negative...?
    p = denom // g1
    q = -sum1 // g1
    if p < 0:
        p *= -1
        q *= -1
    r = denom // g2
    s = -sum2 // g2
    if r < 0:
        r = -r
        s = -s
    # I always get confused with ordering, hope this is right
    if p < r or (p == r and q < s):
        tmp1, tmp2, tmp3, tmp4 = r, s, p, q
        p, q, r, s = tmp1, tmp2, tmp3, tmp4
    print(p, q, r, s)
# It should work, I think