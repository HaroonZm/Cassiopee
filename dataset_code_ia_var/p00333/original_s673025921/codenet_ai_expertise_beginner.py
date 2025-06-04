W, H, C = map(int, input().split())

def pgcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

gcd = pgcd(W, H)
area = W * H
number = area // (gcd * gcd)
print(C * number)