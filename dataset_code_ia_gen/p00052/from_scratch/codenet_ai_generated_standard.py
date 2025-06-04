def trailing_zeros_factorial(n):
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    return count

while True:
    n = int(input())
    if n == 0:
        break
    print(trailing_zeros_factorial(n))