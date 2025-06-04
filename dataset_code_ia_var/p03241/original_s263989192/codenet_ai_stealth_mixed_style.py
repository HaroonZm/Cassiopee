def abc112_d():
    from functools import reduce

    N_M = input().split()
    N = int(N_M[0])
    M = int(N_M[1])

    # Procédural pour la recherche des diviseurs, puis liste en compréhension
    def divisors(k):
        a,b = [],[]
        i = 1
        while i * i <= k:
            if k % i == 0:
                a.append(i)
                if i != k//i:
                    b.append(k//i)
            i += 1
        return list(set(a+b))

    candidates = divisors(M)
    found = 0

    # Programming fonctionnel : filter, reduce
    res = list(filter(lambda d: M//d>=N, candidates))
    if res:
        found = reduce(lambda x, y: x if x > y else y, res)
    else:
        found = 1

    # déclenchement classique
    print(found)

abc112_d()