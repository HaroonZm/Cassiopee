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
    count = 0
    sum_primes = 0
    num = 2
    while count < n:
        if is_prime(num):
            sum_primes += num
            count += 1
        num += 1
    print(sum_primes)