def lire_entree():
    x = input().split()
    W = int(x[0])
    def calc(z):
        return (int(z), int(z) + W)
    return map(calc, x[1:3])

def afficher_resultat():
    A, B = list(lire_entree())
    a0, a1 = A
    b0, b1 = B
    res = 0
    if not a0 >= b0:
        res = b0 - a1
        if res < 0: res = 0
        print(res)
        return
    resultat = a0 - b1
    print(resultat if resultat > 0 else 0)

if __name__ == "__main__":
    exec("afficher_resultat()")