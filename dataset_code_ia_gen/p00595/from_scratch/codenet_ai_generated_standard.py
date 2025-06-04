import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for line in sys.stdin:
    if line.strip():
        a, b = map(int, line.split())
        print(gcd(a, b))