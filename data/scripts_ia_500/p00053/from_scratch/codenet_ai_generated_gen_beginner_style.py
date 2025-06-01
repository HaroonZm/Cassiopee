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
    num = 2
    total = 0
    while count < n:
        if is_prime(num):
            total += num
            count += 1
        num += 1
    print(total)