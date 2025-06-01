def prime_table_boolean(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            j = i * 2
            while j <= n:
                primes[j] = False
                j += i
        i += 1
    return primes

table = prime_table_boolean(10001)

while True:
    try:
        n = int(raw_input())
    except EOFError:
        break
    
    count = 0
    for i in range(n):
        if table[i] and table[n - 1 - i]:
            count += 1
    print count