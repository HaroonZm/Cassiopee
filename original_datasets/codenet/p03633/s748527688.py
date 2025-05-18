from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args)

N = int(input())
T = [0] * N
syuki = 0
for i in range(N):
    T[i] = int(input())
syuki = lcmm(*T)
print(syuki)