n = int(input())
plst = sorted(map(int, input().split()))
print(next(i for i in range(n, 0, -1) if sum(p >= i for p in plst) >= i))