import math

n = int(input())
capacity = [int(input()) for i in range(5)]

neck = min(capacity)
result = math.ceil(n / neck) + 5 - 1

print(result)