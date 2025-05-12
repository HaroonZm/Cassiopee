h1, h2 = map(int, raw_input().split())
k1, k2 = map(int, raw_input().split())
a, b, c, d = map(int, raw_input().split())

calc = lambda p, q: p*a+p/10*c+q*b+q/20*d
v1 = calc(h1, h2); v2 = calc(k1, k2)
print["hiroshi", "even", "kenjiro"][(v1<v2)+(v1<=v2)]