def calculate(N, X, T):
    x = N // X
    if x == 0:
        return T
    elif N % X != 0:
        return (x + 1) * T
    else:
        return x * T

N, X, T = map(int, input().split())
result = calculate(N, X, T)
print(result)