from sys import stdin
t = sum(map(int, (next(stdin) for _ in range(4))))
print(divmod(t, 60)[0])
print(divmod(t, 60)[1])