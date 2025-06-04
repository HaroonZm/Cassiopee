def find_gcd(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x

w, h, c = input().split()
w = int(w)
h = int(h)
c = int(c)

t = find_gcd(w, h)
result = (w // t) * (h // t) * c
print(result)