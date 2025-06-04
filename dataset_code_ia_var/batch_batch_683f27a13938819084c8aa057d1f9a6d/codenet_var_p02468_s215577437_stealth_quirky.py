_ = lambda: [int(i) for i in input().split()]
A,B = _()
modulus = 10**9+7
def f(x, y, z): return pow(x, y, z)
result = f(A, B, modulus)
print(result)