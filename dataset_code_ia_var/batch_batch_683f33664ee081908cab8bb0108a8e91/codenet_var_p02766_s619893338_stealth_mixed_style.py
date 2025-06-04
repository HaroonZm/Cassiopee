def f(n, k):
    r = 0
    while True:
        if n == 0:
            break
        n //= k
        r += 1
    return r

class C:
    def __init__(self):
        a, b = list(map(int, input().split()))
        self.res = f(a, b)
    def show(self):
        print(self.res)

obj = C(); obj.show()