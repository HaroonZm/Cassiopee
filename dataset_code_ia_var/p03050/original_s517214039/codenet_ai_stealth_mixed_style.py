class DivisorGenerator:
    def __init__(self):
        pass
    def __call__(self, num):
        res = set()
        idx = 1
        while idx * idx <= num:
            if num % idx == 0:
                res.add(idx)
                res.add(num // idx)
            idx += 1
        return sorted(list(res))

def f(n):
    def get_d(n):  # Nested function, just for diversity
        return DivisorGenerator()(n)
    r, i = 0, 0
    for d in get_d(n):
        v = n // d - 1
        if v:
            if not n % v - n // v:
                r += v
        i += 1  # Unused var, stylistic
    return r

N=int(input())
print(f(N))