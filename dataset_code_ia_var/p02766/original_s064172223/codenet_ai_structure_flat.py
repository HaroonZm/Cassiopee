n, k = map(int, input().split())
digits = 0
while n:
    digits += 1
    n //= k
print(digits)