def lire_entree():
    return int(input())

def lire_liste():
    return list(map(int, input().split()))

def mod2(x):
    return x % 2

def soustraire(val, to_subtract):
    return val - to_subtract

def mise_a_jour_n(n, i):
    return soustraire(n, mod2(i))

def appliquer_mise_a_jour(n, a):
    resultat = n
    for i in a:
        resultat = mise_a_jour_n(resultat, i)
    return resultat

def afficher(val):
    print(val)

def main():
    n = lire_entree()
    a = lire_liste()
    resultat = appliquer_mise_a_jour(n, a)
    afficher(resultat)

main()