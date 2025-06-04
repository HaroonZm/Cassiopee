def lire_nombre():
    return int(input())

def lire_liste():
    return list(map(int, input().split()))

def trouver_min(liste):
    return min(liste)

def trouver_max(liste):
    return max(liste)

def somme(a, b):
    return a + b

def diviser_entiere(a, b):
    return a // b

def calculer_x(a):
    minimum = trouver_min(a)
    maximum = trouver_max(a)
    somme_min_max = somme(minimum, maximum)
    resultat = diviser_entiere(somme_min_max, 2)
    return resultat

def valeur_absolue(x):
    return abs(x)

def difference_absolue(x, y):
    return valeur_absolue(x - y)

def construire_liste_diff_abs(x, a, N):
    resultat = []
    for i in range(N):
        diff = difference_absolue(x, a[i])
        resultat.append(diff)
    return resultat

def trouver_max_liste(liste):
    return max(liste)

def formater_nombre(nombre):
    return "{:.0f}".format(nombre)

def afficher(texte):
    print(texte)

def programme_principal():
    N = lire_nombre()
    a = lire_liste()
    x = calculer_x(a)
    b = construire_liste_diff_abs(x, a, N)
    resultat = trouver_max_liste(b)
    texte = formater_nombre(resultat)
    afficher(texte)

programme_principal()