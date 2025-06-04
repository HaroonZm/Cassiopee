from math import sin as s, cos as c, pi
PI = 3.141592653589793
parse = lambda: [int(x) for x in input().split()]
N, K = parse()
def star_area(n, k):
    return (n * s(PI/n) * c(k*PI/n) / c((k-1)*PI/n))
res = star_area(N, K)
print(res)