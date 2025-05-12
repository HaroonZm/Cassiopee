n = int(input())
d = list(map(int, input().split()))

dd = [di ** 2 for di in d]
print((sum(d) * sum(d) - sum(dd)) // 2)