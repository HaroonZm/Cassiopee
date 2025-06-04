while True:
    N = int(input())
    if N == 0:
        break

    recettes = []
    for i in range(N):
        recettes.append(input())

    PQR = input().split()
    P = int(PQR[0])
    Q = int(PQR[1])
    R = int(PQR[2])
    C = int(PQR[3])

    trouve = False
    for i in range(N):
        valeurs = recettes[i].split()
        s = int(valeurs[0])
        p = int(valeurs[1])
        q = int(valeurs[2])
        r = int(valeurs[3])

        if p <= P and q <= Q and r <= R:
            if 4*p + 9*q + 4*r <= C:
                print(s)
                trouve = True

    if trouve == False:
        print("NA")