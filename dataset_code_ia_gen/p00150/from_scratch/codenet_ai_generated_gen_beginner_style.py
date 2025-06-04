def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break

    max_twin = (0, 0)
    for i in range(2, n-1):
        if is_prime(i) and is_prime(i+2) and (i+2) <= n:
            if i+2 > max_twin[1]:
                max_twin = (i, i+2)
    print(max_twin[0], max_twin[1])