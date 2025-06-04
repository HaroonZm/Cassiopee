def f(n):
    a = ""
    while n > 0:
        a += str(n % 4)
        n //= 4
    return a[::-1]

while True:
    n = input()
    if n == "-1":
        break
    n = int(n)
    print(f(n) if n > 0 else 0)