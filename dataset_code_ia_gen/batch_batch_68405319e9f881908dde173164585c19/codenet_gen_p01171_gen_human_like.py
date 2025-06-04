def prime_factors(n):
    factors = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.add(n)
    return factors

def key_number(n):
    factors = prime_factors(n)
    largest = max(factors)
    others_sum = sum(factors) - largest
    return largest - others_sum

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if key_number(a) > key_number(b):
        print('a')
    else:
        print('b')