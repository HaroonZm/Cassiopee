n, k = map(int, input().split())
s = 0
i = 0
while n != 0:
    n = n // k
    i = i + 1
print(i)