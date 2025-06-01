W, H, C = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

g = gcd(W, H)
num_parts = (W // g) * (H // g)
cost = num_parts * C

print(cost)