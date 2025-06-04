n = int(input())
def f(x):
    y = 1
    c = 0
    while True:
        if x < y*2:
            return y
        y <<= 1
        c += 1

print((lambda a: f(a))(n))