from functools import reduce
import operator

W, H, x, y = map(int, input().split())

area = reduce(lambda f, g: f(g), [lambda t: t[0]*t[1]/2, lambda v: (v[0], v[1])], (W, H))

count = ((lambda a, b, c, d: all(map(operator.eq, [a*2, b*2],[c, d]))))(x, y, W, H).__int__()

print(area, count)