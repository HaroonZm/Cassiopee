a = sorted(list(map(int, input().split())))
k = int(input())
a[-1] = 2**k*a[-1]
print(sum(a))