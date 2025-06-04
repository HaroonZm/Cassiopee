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

def max_twin_prime(n):
    for q in range(n, 2, -1):
        p = q - 2
        if p >= 2 and is_prime(p) and is_prime(q):
            return p, q
    return None

while True:
    n = int(input())
    if n == 0:
        break
    p, q = max_twin_prime(n)
    print(p, q)