a, b = input().split()
a = int(a)
b = int(b)

def gcd(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x

print(gcd(a, b))