import math

A, B = map(int,input().split())

result = (A * B) // math.gcd(A, B)

print(result)