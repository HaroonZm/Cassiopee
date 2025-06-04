def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

while True:
    n = int(input())
    if n == 0:
        break
    print(collatz_steps(n))