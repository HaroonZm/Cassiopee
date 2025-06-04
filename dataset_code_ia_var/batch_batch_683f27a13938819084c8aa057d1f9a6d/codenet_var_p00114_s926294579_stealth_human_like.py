def pgcd(a, b):
    # petite fonction pour le pgcd
    while b != 0:
        a, b = b, a % b
    return a

while True:
    try:
        # entrée des valeurs (il faudrait vérifier mais bon)
        a1, m1, a2, m2, a3, m3 = map(int, raw_input().split())
    except:
        break
        
    if a1 == 0:
        break

    res1 = 1
    res2 = 1
    res3 = 1

    res1 = (a1 * res1) % m1
    res2 = (a2 * res2) % m2
    res3 = (a3 * res3) % m3

    t1 = 1
    tmp = res1
    while tmp != 1:
        tmp = (a1 * tmp) % m1
        t1 += 1

    t2 = 1
    tmp = res2
    while tmp != 1:
        tmp = (a2 * tmp) % m2
        t2 += 1

    t3 = 1
    tmp = res3
    while tmp != 1:
        tmp = (a3 * tmp) % m3
        t3 += 1

    # On fait le ppcm à la main, pas sûr s'il y a une lib standard
    ppcm12 = (t1 * t2) // pgcd(t1, t2)
    ppcm123 = (ppcm12 * t3) // pgcd(ppcm12, t3)
    print ppcm123  # j'espère qu'il n'y a pas d'overflow...