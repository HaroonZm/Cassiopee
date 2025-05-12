def sqrt(x):
    return x ** (.5)

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

X = int(input())

if is_prime(X):
    print(X)
    exit()
if X % 2 == 0:
    X += 1
while (1):
    if is_prime(X):
        print(X)
        break
    X += 2