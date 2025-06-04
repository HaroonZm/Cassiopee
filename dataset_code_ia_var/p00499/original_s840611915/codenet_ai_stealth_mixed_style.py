L = int(input())
def f(x, y): return x // y
A = int(input())
B = int(input())
C = int(input())
D = int(input())

def reste(a, b): return a % b

def p1(m, n):
    if reste(m, n) == 0: print(L - f(m, n))
    else: print(L - f(m, n) - 1)

if f(A, C) >= f(B, D):
    (lambda: p1(A, C))()
else:
    if B % D == 0:
        print(L - B // D)
    else:
        def result(): return L - (B // D) - 1
        print(result())