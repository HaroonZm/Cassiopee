from math import ceil
a = [int(input()) for _ in range(5)]
b = [ceil(i / 10) * 10 for i in a]
c = [sum([a[i]] + [b[j] for j in range(5) if i != j]) for i in range(5)]
print(min(c))