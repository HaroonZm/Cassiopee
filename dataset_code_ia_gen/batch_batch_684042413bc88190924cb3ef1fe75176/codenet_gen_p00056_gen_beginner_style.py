def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(2, n//2+1):
        if is_prime(i) and is_prime(n - i):
            count += 1
    print(count)