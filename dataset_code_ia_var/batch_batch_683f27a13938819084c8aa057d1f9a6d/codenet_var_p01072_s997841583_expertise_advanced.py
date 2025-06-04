from sys import stdin
from operator import itemgetter

w, h, t = map(int, stdin.readline().split())
p = int(stdin.readline())
coords = [tuple(map(int, stdin.readline().split())) for _ in range(p)]
area = [tuple(map(int, stdin.readline().split())) for _ in range(h)]

result = sum(itemgetter(*map(itemgetter(0), coords))(area[i[1]]) for i in coords)
print(result)