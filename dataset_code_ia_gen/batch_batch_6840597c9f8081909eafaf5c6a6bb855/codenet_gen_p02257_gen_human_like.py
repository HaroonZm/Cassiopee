def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

N = int(input())
count = 0
for _ in range(N):
    num = int(input())
    if is_prime(num):
        count += 1

print(count)