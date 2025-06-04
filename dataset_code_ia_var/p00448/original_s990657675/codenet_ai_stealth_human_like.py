# Franchement, ce code mériterait bien un refactoring... mais bon, allons-y comme ça
while True:
    # Bon, on lit les input jusqu'à "0 0" c'est le signal d'arrêt
    ligne = input()
    if ligne == '0 0':
        break
    r = int(ligne.split()[0])
    # lecture des lignes suivantes pour les données
    mat = []
    for _ in range(r):
        mat.append(input().split())
    # Je convertis les colonnes en entiers binaires, pas fou le gars qui a mis ça
    d = []
    for col in zip(*mat):
        tout = ''.join(col)
        d.append(int(tout,2))
    a = 0
    b = 1 << r
    # f servira à marquer les masques à traiter
    f = [1]*b
    for m in range(b):
        if f[m]:
            f[~m] = 0  # Invalide le masque opposé (ptet pas hyper utile)
            t = 0
            for s in d:
                # On compte le nombre de bits différents
                c = bin(m^s).count('1')
                if c > (r//2):
                    t += c
                else:
                    t += r - c # c'est louche mais bon
            if t > a:
                a = t
    print(a)  # Voilà, c'est printé (j'espère que c'est bon)