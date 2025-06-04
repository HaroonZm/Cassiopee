def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i = i + 1
    return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x = x + 1