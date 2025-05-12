def calc_gcd(x, y):
    
    if x < y:
        x, y = y, x

    while y > 0:
        x, y = y, x % y

    return x

a, b = map(int, input().split())

gcd = calc_gcd(a, b)

x1 = 1
y1 = 0
z1 = a_prime = a / gcd

x2 = 0
y2 = 1
z2 = b_prime = b / gcd

while z2 != 1:
    q = (z1 - (z1 % z2)) / z2

    (x1, y1, z1), (x2, y2, z2) = (x2, y2, z2), (x1 - (q * x2), y1 - (q * y2), z1 - (q * z2))

t = 0
x = x2 + b_prime * t
y = y2 + a_prime * t

print(int(x), int(y))