# Définition de la fonction a1 qui prend en argument une liste 'li'
def a1(li):
    # Vérifie si la valeur 100 est présente dans la liste 'li'
    # L'opérateur 'in' vérifie la présence d'un élément dans une collection (ici, list)
    if 100 in li:
        # Si 100 est présent dans la liste, retourne 1 (ce qui signifie Vrai dans ce contexte)
        return 1
    else:
        # Si 100 n'est pas présent, retourne 0 (ce qui signifie Faux)
        return 0

# Définition de la fonction a2 qui prend une liste 'li' en argument
def a2(li):
    # Calcule la moyenne des deux premiers éléments de la liste 'li'
    # li[0] fait référence au premier élément, li[1] au second
    # L'opérateur + additionne les deux éléments
    # L'expression (li[0]+li[1])/2 calcule leur moyenne arithmétique
    if (li[0] + li[1]) / 2 >= 90:
        # Si la moyenne est supérieure ou égale à 90, retourne 1
        return 1
    else:
        # Sinon, retourne 0
        return 0

# Définition de la fonction a3 qui prend une liste 'li' en argument
def a3(li):
    # Calcule la somme de tous les éléments de la liste grâce à la fonction intégrée sum()
    # Cette somme est divisée par 3 pour obtenir la moyenne (sachant que li contient 3 éléments)
    if sum(li) / 3 >= 80:
        # Si la moyenne est supérieure ou égale à 80, retourne 1
        return 1
    else:
        # Sinon, retourne 0
        return 0

# Définition de la fonction isA qui décide si la liste satisfait l'une des conditions a1, a2, ou a3
def isA(li):
    # Appelle successivement les fonctions a1, a2 et a3 en leur passant la liste 'li'
    # L'opérateur 'or' renvoie True si au moins une des fonctions retourne 1 (True)
    if a1(li) or a2(li) or a3(li):
        # Si l'une des trois fonctions retourne 1, retourne 1
        return 1
    else:
        # Sinon, retourne 0
        return 0

# Définition de la fonction b1 qui évalue une autre condition sur la liste 'li'
def b1(li):
    # Calcule la moyenne des 3 éléments de la liste
    if sum(li) / 3 >= 70:
        # Si la moyenne est supérieure ou égale à 70, retourne 1
        return 1
    else:
        # Sinon, retourne 0
        return 0

# Définition de la fonction b2 qui vérifie plusieurs conditions sur la liste
def b2(li):
    # 'sum(li)/3 >= 50' vérifie que la moyenne des trois éléments est au moins 50
    # '(li[0] >= 80 or li[1] >= 80)' vérifie que le premier ou le deuxième élément est au moins 80
    if sum(li) / 3 >= 50 and (li[0] >= 80 or li[1] >= 80):
        # Si les deux conditions sont vraies, retourne 1
        return 1
    else:
        # Sinon, retourne 0
        return 0

# Définition de la fonction isB qui décide si la liste satisfait les conditions de b1 ou b2
def isB(li):
    # Vérifie si b1(li) ou b2(li) retourne 1
    if b1(li) or b2(li):
        # Si au moins une des deux fonctions retourne 1, retourne 1
        return 1
    else:
        # Sinon, retourne 0
        return 0

# Définition de la fonction isX qui classe la liste selon les fonctions précédentes
def isX(li):
    # Si la fonction isA retourne 1, cela signifie que la liste est dans la catégorie 'A'
    if isA(li):
        return 'A'
    # Sinon, si la fonction isB retourne 1, cela signifie que la liste est dans la catégorie 'B'
    elif isB(li):
        return 'B'
    else:
        # Si aucune des conditions n'est remplie, retourne 'C'
        return 'C'

# Boucle infinie pour accepter plusieurs ensembles d'entrées utilisateur
while True:
    # Demande à l'utilisateur d'entrer un nombre, le convertit en entier avec int()
    N = int(input())
    # Si N est égal à 0, la condition est vraie et on sort de la boucle grâce au mot-clé break
    if N == 0:
        break
    # Sinon, on exécute la boucle suivante N fois (pour chaque cas de test)
    for _ in range(N):
        # Demande à l'utilisateur d'entrer une ligne d'entiers séparés par des espaces
        # input() lit une ligne, split() sépare à chaque espace, map(int, ...) convertit chaque portion en entier
        # list(...) transforme le résultat en une liste d'entiers
        l = list(map(int, input().split()))
        # Appelle la fonction isX avec la liste l et affiche (imprime) le résultat correspondant ('A', 'B', ou 'C')
        print(isX(l))