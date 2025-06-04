def _(*__, **_a):
    return __

x=lambda: input().split()
A, B = _(*x())
print(B+A)