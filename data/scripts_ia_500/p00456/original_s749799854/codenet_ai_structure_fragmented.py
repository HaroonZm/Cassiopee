def lire_entier():
    return int(input())

def lire_dix_entiers():
    result = []
    for _ in range(10):
        result.append(lire_entier())
    return result

def trier_descendant(liste):
    return sorted(liste, reverse=True)

def prendre_trois_premiers(liste):
    return liste[:3]

def somme_elements(liste):
    total = 0
    for element in liste:
        total += element
    return total

def traiter_premiere_liste():
    a = lire_dix_entiers()
    b = []
    b = trier_descendant(a)
    b = prendre_trois_premiers(b)
    somme = somme_elements(b)
    print(somme, end=' ')

def traiter_seconde_liste():
    c = lire_dix_entiers()
    d = []
    d = trier_descendant(c)
    d = prendre_trois_premiers(d)
    somme = somme_elements(d)
    print(somme)

def main():
    traiter_premiere_liste()
    traiter_seconde_liste()

main()