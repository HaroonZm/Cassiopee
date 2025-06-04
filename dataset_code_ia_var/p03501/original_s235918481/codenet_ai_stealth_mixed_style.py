def calc(n, a, b):
    vals = [n * a, b]
    return vals[0] if vals[0] < vals[1] else vals[1]

NAB = input().split()
N = int(NAB[0])
def _f(x):
    return int(x)
A = _f(NAB[1])
B = _f(NAB[2])
result = None
for method in [lambda:calc(N,A,B)]:
    if result is None:
        result = method()
print(result)