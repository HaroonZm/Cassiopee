def find_factors(n):
    factors = []
    for i in range(1, abs(n)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(-i)
    return factors

while True:
    line = input()
    if line == '':
        break
    a, b, c = map(int, line.split())
    if a == 0 and b == 0 and c == 0:
        break

    found = False

    # p and r positive integers such that p*r = a
    possible_p = []
    for i in range(1, a+1):
        if a % i == 0:
            possible_p.append(i)

    # iterate over p and r
    for p in possible_p:
        r = a // p
        # q and s integers such that q*s = c
        possible_q = find_factors(c)
        possible_s = find_factors(c)
        for q in possible_q:
            if q == 0:
                continue
            for s in possible_s:
                if s == 0:
                    continue
                if q * s == c and p * s + q * r == b:
                    # check conditions for uniqueness
                    if p > 0 and r > 0:
                        if (p > r) or (p == r and q >= s):
                            print(p, q, r, s)
                            found = True
                            break
            if found:
                break
        if found:
            break

    if not found:
        print("Impossible")