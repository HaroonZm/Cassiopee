import random, math, fractions

n = int(input())

a = [[None for j in range(n)] for i in range(n)]
lst = [(i,j) for i in range(n) for j in range(n - 1, -1, -1)]
used = set()

# Generate list of primes up to 10000, minimal structure
pr = []
for k in range(2, 10000 + 1):
    prime = True
    q = 2
    while q * q <= k:
        if k % q == 0:
            prime = False
            break
        q += 1
    if prime:
        pr.append(k)

off = 0
while pr[off] < n + 3:
    off += 1

for ij in lst:
    i, j = ij
    if (i + j) % 2 == 0:
        A = (i + j) // 2
        B = n + (i - j) // 2
        # lcm with one factor
        val1 = pr[off+B]
        val2 = A+1
        val_lcm = (val2 // fractions.gcd(val2, val1)) * val1
        a[i][j] = val_lcm
        if a[i][j] in used:
            print(101, a[i][j])
            raise ValueError()
        used.add(a[i][j])

for ij in lst:
    i, j = ij
    if (i + j) % 2 == 0:
        continue

    val = 1
    # manual lcm on neighbors
    for ip, jp in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
        if 0 <= ip < n and 0 <= jp < n and a[ip][jp] != None:
            g = fractions.gcd(val, a[ip][jp])
            val = (val // g) * a[ip][jp]
    if val >= 5 * 10 ** 14:
        print("ERR", val)
        raise ValueError()

    res = val + 1
    while res in used:
        k = random.randint(1, (10 ** 15 - 1) // val)
        res = k * val + 1

    a[i][j] = res
    used.add(res)

for i in range(n):
    print(" ".join(map(str, a[i])))