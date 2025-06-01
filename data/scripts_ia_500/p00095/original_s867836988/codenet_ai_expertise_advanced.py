n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
a = sorted(((-y, x) for x, y in a))
print(a[0][1], -a[0][0])