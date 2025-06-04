W, H, C = map(int, input().split())
def gcd(a,b):
    while b:
        a,b = b, a % b
    return a
g = gcd(W, H)
n = (W//g) * (H//g)
print(n * C)