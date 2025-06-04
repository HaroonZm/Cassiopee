import sys
sys.setrecursionlimit(10000000)

def f(a, b):
    if a == b:
        return a
    if a > b:
        temp = a
        a = b
        b = temp
    if b % a == 0:
        return 2 * (b // a) * a - a
    else:
        return 2 * (b // a) * a + f(a, b % a)

N, X = input().split()
N = int(N)
X = int(X)
result = f(X, N - X) + N
print(result)