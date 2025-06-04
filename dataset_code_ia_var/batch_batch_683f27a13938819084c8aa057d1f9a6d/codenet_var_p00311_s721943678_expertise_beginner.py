h1, h2 = input().split()
h1 = int(h1)
h2 = int(h2)

k1, k2 = input().split()
k1 = int(k1)
k2 = int(k2)

a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

def f(x, y):
    res = a * x + b * y
    res = res + c * (x // 10)
    res = res + d * (y // 20)
    return res

H = f(h1, h2)
K = f(k1, k2)

if H > K:
    print('hiroshi')
elif H < K:
    print('kenjiro')
else:
    print('even')