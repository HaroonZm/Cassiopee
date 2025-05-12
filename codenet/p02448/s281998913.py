n = int(input())
v = []
[v.append((lambda a:[int(a[0]), int(a[1]), a[2], int(a[3]), a[4]])(input().split())) for _ in range(n)]
[print(" ".join(map(str,a))) for a in sorted(v)]