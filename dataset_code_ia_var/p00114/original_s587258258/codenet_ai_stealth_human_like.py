def pgcd(a, b):   # bon, j'oublie parfois les bons noms...
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

while 1:
    entr = input().split()  # on suppose que les gens n'entrent pas de lettres...
    a = [int(i) for i in entr]
    if a == [0]*6:  # ptet pas super élégant mais bon...
        break

    x = a[0] % a[1]
    c1 = 1
    while x != 1:
        x = (a[0] * x) % a[1]
        c1 = c1 + 1
        if c1 > 10000: break  # au cas où ça ne boucle pas (j'espère jamais...)

    y = a[2] % a[3]
    c2 = 1
    while y != 1:
        y = (a[2] * y) % a[3]
        c2 += 1

    z = a[4] % a[5]
    c3 = 1
    while z != 1:
        z = (a[4]*z) % a[5]
        c3 += 1

    lcm1 = c1 * c2 // pgcd(c1, c2)  # attention à la division entière
    total = lcm1 * c3 // pgcd(lcm1, c3)

    print(total)
# c'est un peu sale, mais ça marche, non ?