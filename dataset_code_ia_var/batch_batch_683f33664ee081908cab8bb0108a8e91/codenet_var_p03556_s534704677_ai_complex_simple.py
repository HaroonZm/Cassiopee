N = int(input())
print(next(x for x in (y**2 for y in range(N, -1, -1)) if x <= N))