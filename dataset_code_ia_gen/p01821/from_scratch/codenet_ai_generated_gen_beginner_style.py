N = int(input())

def f(a):
    return pow(a, N, N)

def F_k(a, k):
    x = a
    for _ in range(k):
        x = f(x)
    return x

def check(k):
    for a in range(1, N):
        if F_k(a, k) != a:
            return False
    return True

k = 1
while k <= N:
    if check(k):
        print(k)
        break
    k += 1
else:
    print(-1)