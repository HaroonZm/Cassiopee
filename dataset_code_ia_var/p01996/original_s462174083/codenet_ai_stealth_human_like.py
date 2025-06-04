import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
# Je vais utiliser bisect mais pas sûr de l'avoir fait souvent...
idx = bisect.bisect_left(a, m+1)
# j'espère que c'est ce qu'il fallait, à voir...
print(m - idx)