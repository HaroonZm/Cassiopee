import math as _m
parse = lambda: list(map(int, input().split()))
a, b, c, d = parse()
delta = [c-a, d-b]
length = _m.sqrt(sum(j*j for j in delta))
n = int(input())

[*map(lambda p: print(*(a+delta[0]*p, b+delta[1]*p)), [((e-a)*delta[0] + (f-b)*delta[1])/(length**2) for e,f in (parse() for _ in [None]*n)])]