mod = 10**9 + 7

n, k = map(int, input().split())

if n > k:
    print(0)
else:
    # Compute n! modulo mod
    fact = 1
    for i in range(1, n+1):
        fact = (fact * i) % mod

    # Compute permutation: P(k,n) = k*(k-1)*...*(k-n+1)
    perm = 1
    for i in range(k, k - n, -1):
        perm = (perm * i) % mod

    # The number of ways is P(k,n) * n! / n! is for balls arrangement which is 1 since balls are distinct and perm already counts distinct balls into boxes permutation
    # Actually, since each ball must be put into one box and no box has more than one ball,
    # the number of ways is simply the number of injective functions from balls to boxes,
    # which is P(k,n) = k! / (k-n)!
    print(perm)