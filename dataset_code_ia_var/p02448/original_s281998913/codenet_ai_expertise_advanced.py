from operator import itemgetter

n = int(input())
v = [(*map(int, (a := input().split()))[:2], a[2], int(a[3]), a[4]) for _ in range(n)]
for entry in sorted(v, key=itemgetter(0, 1, 2, 3, 4)):
    print(*entry)