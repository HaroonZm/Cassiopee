a = []
l = [2]

while True:
    try:
        val = input()
        a.append(int(val))
    except Exception:
        break

def primes(n):
    import math
    sieve = [True]*(n+1)
    sieve[0], sieve[1] = False, False
    for num in range(2, int(math.sqrt(n)) + 1):
        if sieve[num]:
            for multiple in range(num*num, n+1, num):
                sieve[multiple] = False
    return list(filter(lambda x: sieve[x], range(n+1)))

z = primes(max(a))

def count_primes_up_to(k):
    count = 0
    for prime in z:
        if prime <= k:
            count +=1
    return count

for k in a:
    print(count_primes_up_to(k))