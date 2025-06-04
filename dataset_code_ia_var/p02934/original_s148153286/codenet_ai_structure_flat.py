n = int(input())
a = [int(x) for x in input().split()]
c = 0
i = 0
while i < n:
    c += 1 / a[i]
    i += 1
print(1 / c)