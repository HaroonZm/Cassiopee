from functools import reduce

t = sum(int(input()) for _ in range(4))
g, remainder = divmod(t, 60)
print(g)
print(remainder)