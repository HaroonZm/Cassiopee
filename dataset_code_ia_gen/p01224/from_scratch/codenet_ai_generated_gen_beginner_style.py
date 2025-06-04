def sum_proper_divisors(n):
    if n == 1:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total

while True:
    N = int(input())
    if N == 0:
        break
    S = sum_proper_divisors(N)
    if N == S:
        print("perfect number")
    elif N > S:
        print("deficient number")
    else:
        print("abundant number")