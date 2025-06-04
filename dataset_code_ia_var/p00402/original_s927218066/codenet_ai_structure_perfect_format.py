import math

n = int(input())
a = list(map(int, input().split()))
mn = min(a)
mx = max(a)
result = math.ceil((mn + mx) / 2) - mn
print(result)