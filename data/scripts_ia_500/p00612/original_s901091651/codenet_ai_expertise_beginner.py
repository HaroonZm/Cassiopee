def f(n):
    result = 1 + 2 * n
    i = 1
    while i * i <= n:
        result = result + 1 + ((n - i * i) // i) * 2
        i = i + 1
    return result

while True:
    n = int(input())
    if n == 0:
        break
    value = f((n // 2) - 1)
    output = 8 * value + 8 * n
    print(output)