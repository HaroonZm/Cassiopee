w, h, c = input().split()
w = int(w)
h = int(h)
c = int(c)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

g = gcd(w, h)
result = (w // g) * (h // g) * c
print(result)