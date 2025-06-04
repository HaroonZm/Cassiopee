from sys import stdin
from operator import itemgetter

w, h, t, *rest = map(int, stdin.read().split())
n, *data = rest
n = n or 0
coords = list(zip(map(int, data[:2*int(n):2]), map(int, data[1:2*int(n):2])))
area_data = data[2*int(n):]
area = [tuple(area_data[i*w:(i+1)*w]) for i in range(h)]

print(sum(map(itemgetter(*[y*w + x for x, y in coords]), [sum(area, ())])))