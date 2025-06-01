def primes(n):
    sieve = list(map(lambda _: True, range(n + 1)))
    sieve[0], sieve[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] is False:
            continue
        for j in range(i * i, n + 1, i):
            sieve[j] = False
    return list(filter(lambda x: sieve[x], range(n + 1)))

a = (lambda f=[]: (lambda g: [g() for _ in iter(int, 1)])(lambda: f.append(int(input()))) or f)() 

z = primes(max(a))

_ = [print(len(list(filter(lambda x: x <= k, z)))) for k in a]