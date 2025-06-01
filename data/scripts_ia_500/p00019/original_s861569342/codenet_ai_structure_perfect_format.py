def f(x):
    if x == 1:
        return x
    else:
        return x * f(x - 1)

n = int(input())
print(f(n))