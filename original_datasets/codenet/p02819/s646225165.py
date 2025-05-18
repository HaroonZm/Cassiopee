def isprime(n):
    a = 2
    while a * a < n:
        if x % a == 0:
            return False
        a += 1
    return True

x = int(input())
while True:
    if isprime(x):
        print(x)
        break
    x += 1