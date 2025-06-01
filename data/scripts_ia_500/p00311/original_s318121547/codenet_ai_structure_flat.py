h1, h2 = map(int, raw_input().split())
k1, k2 = map(int, raw_input().split())
a, b, c, d = map(int, raw_input().split())
v1 = h1*a + h1/10*c + h2*b + h2/20*d
v2 = k1*a + k1/10*c + k2*b + k2/20*d
if v1 < v2:
    print("hiroshi")
elif v1 == v2:
    print("even")
else:
    print("kenjiro")