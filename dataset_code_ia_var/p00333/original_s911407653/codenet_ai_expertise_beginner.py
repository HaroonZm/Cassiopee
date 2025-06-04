W, H, C = input().split()
W = int(W)
H = int(H)
C = int(C)

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

g = gcd(W, H)
result = (W // g) * (H // g) * C
print(result)