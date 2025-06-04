n = int(input())

def smallest_divisor(x):
    if x % 2 == 0:
        return 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return i
        i += 2
    return x  # x is prime

start = 2
while True:
    found = True
    divisors = []
    for num in range(start, start + n):
        d = smallest_divisor(num)
        if d == 1 or d == num:
            # number is prime or 1, no divisor other than 1 or itself
            found = False
            break
        divisors.append(d)
    if found:
        print(start)
        for d in divisors:
            print(d)
        break
    start += 1