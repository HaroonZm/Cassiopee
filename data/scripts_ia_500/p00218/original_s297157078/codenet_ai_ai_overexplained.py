def a1(li):
    # Cette fonction vérifie si la liste d'entiers 'li' contient la valeur 100.
    # 'in' est un opérateur qui retourne True si l'élément à gauche est présent dans l'objet à droite.
    if 100 in li:
        # Si 100 est trouvé dans la liste, la fonction retourne l'entier 1.
        return 1
    else:
        # Sinon, elle retourne l'entier 0.
        return 0

def a2(li):
    # Cette fonction calcule la moyenne des deux premiers éléments de la liste 'li'
    # puis compare cette moyenne à 90.
    # li[0] est le premier élément de la liste, li[1] le second.
    moyenne = (li[0] + li[1]) / 2
    # Comparaison pour vérifier si la moyenne est supérieure ou égale à 90.
    if moyenne >= 90:
        # Si oui, retourne 1.
        return 1
    else:
        # Sinon, retourne 0.
        return 0

def a3(li):
    # Cette fonction calcule la moyenne des trois éléments de la liste 'li'
    # en utilisant la fonction sum(), qui additionne tous les éléments de la liste.
    # Elle divise ensuite la somme par 3 pour obtenir la moyenne.
    moyenne = sum(li) / 3
    # Vérifie si la moyenne est supérieure ou égale à 80.
    if moyenne >= 80:
        # Retourne 1 si la condition est vraie.
        return 1
    else:
        # Retourne 0 si la condition est fausse.
        return 0

def isA(li):
    # Cette fonction détermine si la liste 'li' correspond à une catégorie 'A'.
    # Elle utilise les fonctions a1, a2 et a3 définies précédemment.
    # L'opérateur 'or' est un opérateur logique qui retourne True si au moins une condition est vraie.
    if a1(li) or a2(li) or a3(li):
        # Si une des fonctions retourne 1 (considérée comme True en contexte booléen),
        # la fonction retourne 1 pour indiquer que la catégorie 'A' est satisfaite.
        return 1
    else:
        # Sinon, retourne 0.
        return 0

def b1(li):
    # Fonction qui calcule la moyenne des éléments de 'li' et vérifie si elle est >= 70.
    moyenne = sum(li) / 3
    if moyenne >= 70:
        return 1
    else:
        return 0

def b2(li):
    # Fonction qui vérifie deux conditions simultanément:
    # 1) La moyenne des éléments de 'li' est supérieure ou égale à 50.
    # 2) Au moins l'un des deux premiers éléments est supérieur ou égal à 80.
    moyenne = sum(li) / 3
    condition_premier = li[0] >= 80
    condition_second = li[1] >= 80
    if moyenne >= 50 and (condition_premier or condition_second):
        # Si les deux conditions sont satisfaites, retourne 1.
        return 1
    else:
        # Sinon, retourne 0.
        return 0

def isB(li):
    # Cette fonction décide si 'li' rentre dans la catégorie 'B'.
    # Elle retourne 1 si b1 ou b2 est satisfait, sinon 0.
    if b1(li) or b2(li):
        return 1
    else:
        return 0

def isX(li):
    # Fonction principale qui détermine la catégorie ('A', 'B' ou 'C') pour la liste 'li'.
    # Elle teste d'abord la catégorie 'A', puis 'B', sinon 'C'.
    if isA(li):
        # Si 'li' est de catégorie 'A', retourne la chaîne de caractères 'A'.
        return 'A'
    elif isB(li):
        # Sinon, si 'li' est de catégorie 'B', retourne 'B'.
        return 'B'
    else:
        # Si aucune condition précédente n'est remplie, retourne 'C'.
        return 'C'

# Boucle infinie qui permet de traiter plusieurs cas d'entrée jusqu'à ce que l'utilisateur entre 0.
while True:
    # Lit une ligne d'entrée standard, convertit la chaîne en entier et stocke dans 'N'.
    N = int(input())
    # Si 'N' vaut 0, cela signifie qu'on doit sortir de la boucle et terminer le programme.
    if N == 0:
        break
    # Sinon, on entre dans une boucle qui va tourner 'N' fois.
    for _ in range(N):
        # Pour chaque itération, lit une ligne d'entrée qui contient plusieurs nombres séparés par des espaces.
        # La fonction map applique int à chaque élément lu pour obtenir une liste d'entiers.
        l = list(map(int, input().split()))
        # Affiche le résultat obtenu en appelant la fonction isX avec la liste 'l' comme paramètre.
        print(isX(l))