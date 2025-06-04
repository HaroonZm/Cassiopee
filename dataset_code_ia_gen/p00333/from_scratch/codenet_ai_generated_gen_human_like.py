W, H, C = map(int, input().split())
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
g = gcd(W, H)
num_sections = (W // g) * (H // g)
print(num_sections * C)