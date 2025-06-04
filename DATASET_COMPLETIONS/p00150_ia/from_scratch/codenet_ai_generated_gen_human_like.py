def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    max_twin = (0, 0)
    for q in range(n, 2, -1):
        p = q - 2
        if p < 2:
            continue
        if is_prime(p) and is_prime(q):
            max_twin = (p, q)
            break
    print(max_twin[0], max_twin[1])