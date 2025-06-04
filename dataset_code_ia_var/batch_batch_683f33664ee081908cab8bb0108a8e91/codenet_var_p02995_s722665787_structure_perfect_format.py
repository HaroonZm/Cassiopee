A, B, C, D = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

E = C * D // gcd(C, D)

dif = B - A + 1
rc = B // C + (-A // C) + 1
rd = B // D + (-A // D) + 1
re = B // E + (-A // E) + 1
x = dif - rc - rd + re

print(x)