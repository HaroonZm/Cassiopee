def gcd(a, b):
    return gcd(b % a, a) if a else b

def lcm(a, b):
    return a * b // gcd(a, b)

A, B, C, D = map(int, input().split(' '))

total = B - A + 1

group_CD = lcm(C, D)

if A % C == 0:
    lower_C = A // C
else:
    lower_C = A // C + 1
upper_C = B // C + 1
num_C = upper_C - lower_C

if A % D == 0:
    lower_D = A // D
else:
    lower_D = A // D + 1
upper_D = B // D + 1
num_D = upper_D - lower_D

if A % group_CD == 0:
    lower_CD = A // group_CD
else:
    lower_CD = A // group_CD + 1
upper_CD = B // group_CD + 1
num_CD = upper_CD - lower_CD

print(total - num_C - num_D + num_CD)