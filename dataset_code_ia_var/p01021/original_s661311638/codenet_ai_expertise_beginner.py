def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    n, m = map(int, input().split())
    alst = list(map(int, input().split()))
    blst = list(map(int, input().split()))

    g1 = alst[0]
    for i in range(1, n):
        g1 = pgcd(g1, alst[i])

    l2 = blst[0]
    for i in range(1, m):
        # Calculer le PPCM à la main
        g2 = pgcd(l2, blst[i])
        l2 = l2 * blst[i] // g2

    if g1 % l2 != 0:
        print(0)
    else:
        x = g1 // l2
        ans = 1
        for i in range(2, 10000000):
            if i > x:
                break
            cnt = 1
            while x % i == 0:
                cnt += 1
                x //= i
            ans *= cnt
        print(ans)

main()