N = int(input())
d = [int(x) for x in input().split()]

d.sort()
h = N // 2
print(d[h] - d[h-1])