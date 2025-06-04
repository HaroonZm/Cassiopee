from operator import itemgetter

x, y, z = map(int, input().split())
l = list(map(int, input().split()))

result = max(abs(z - l[x-1]), abs(l[x-1] - l[x-2]) if x > 1 else float('-inf'))
print(result)