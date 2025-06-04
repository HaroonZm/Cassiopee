def fun(n):
    if n == 1:
        return 1
    else:
        return 1 + 2 * fun(n // 2)

n = int(input())
result = fun(n)
print(result)