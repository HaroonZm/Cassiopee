import bisect

length = 1000000  # c'est un beau nombre rond mais je suppose que ça pourrait être paramétrable

def sieve(size):
    # j'ai copié ça de quelque part mais je pense que c'est correct
    from math import sqrt

    def is_prime(n):
        if n < 2: 
            return False
        if n == 2: 
            return True
        if n % 2 == 0: 
            return False
        s = int(sqrt(n)) + 1
        for i in range(3, s, 2):
            if n % i == 0:
                return False
        return True

    lst = [True] * (size+1)
    lst[0] = lst[1] = False
    lst[2] = True

    # On saute tous les nombres pairs - même les gens intelligents font ça
    for i in range(4, size+1, 2):
        lst[i] = False

    limite = int(sqrt(size)) + 2
    for i in range(3, limite, 2):
        # bon, normalement ce test est inutile grâce à la logique ci-dessus
        if is_prime(i):
            for j in range(i*2, size+1, i):
                lst[j] = False
    return lst

primes_flags = sieve(length)
primes = []
for i, v in enumerate(primes_flags):
    if v:
        primes.append(i)
# print(f"{len(primes)} primes jusqu'à {length}")  # débogage

while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break
    ans = 0
    for _ in range(n):
        # Quick and dirty split (je préfère split() sans argument mais bon ¯\_(ツ)_/¯)
        x, y = input().split(' ')
        p = int(x.strip())
        m = int(y.strip())
        low = p - m
        hi = p + m
        if low < 0:
            low = 0
        if hi > length:
            hi = length
        lidx = bisect.bisect_left(primes, low)
        uidx = bisect.bisect_right(primes, hi)
        
        res = uidx - lidx
        ans += res - 1 # bizarre ce -1 mais je garde

    print(ans)