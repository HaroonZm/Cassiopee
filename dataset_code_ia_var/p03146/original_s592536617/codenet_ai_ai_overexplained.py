# Définition d'une fonction appelée 'p' qui prend un argument 'a'
# Cette fonction utilise la fonction intégrée 'print' de Python pour afficher la valeur de 'a' dans la console
def p(a):
    print(a)

# Utilisation de la fonction input() pour demander à l'utilisateur de saisir une valeur
# input() renvoie toujours une chaîne de caractères (str)
# int() convertit cette chaîne de caractères en un nombre entier (int)
s = int(input())

# Création d'une liste contenant un seul élément : la valeur de 's'
# Les listes sont des structures de données qui peuvent stocker plusieurs éléments
list = [s]

# Utilisation d'une boucle infinie 'while True'
# Cette boucle se répète sans fin jusqu'à ce qu'une instruction break soit exécutée
while True:
    # Accès à l'élément le plus récent de la liste, c'est-à-dire le dernier élément ajouté
    # len(list) donne le nombre d'éléments dans la liste
    # len(list)-1 donne l'index du dernier élément (car l'indexation commence à 0)
    # Si cet élément est divisible par 2 (c'est-à-dire si c'est un nombre pair)
    if list[len(list)-1] % 2 == 0:
        # Si le nombre est pair, on calcule sa moitié en le divisant par 2
        # L'opérateur '/' fait une division réelle, donc le résultat est un nombre à virgule flottante (float)
        a = list[len(list)-1] / 2
    else:
        # Sinon, si le nombre est impair, on applique la formule 3n+1
        a = 3 * list[len(list)-1] + 1

    # Vérification si la valeur 'a' calculée existe déjà dans la liste
    # L'opérateur 'in' vérifie la présence de 'a' comme élément dans la liste
    if a in list:
        # Si on retrouve 'a' dans la liste, cela signifie que la séquence entre dans une boucle ou se répète
        # On appelle la fonction 'p' et on lui donne comme argument la longueur de la liste plus un
        # len(list) donne le nombre d'étapes déjà effectuées, on ajoute 1 pour compter le nouvel élément générant la boucle
        p(len(list) + 1)
        # L'instruction 'break' permet de sortir immédiatement de la boucle while, mettant fin à l'exécution répétée du bloc
        break
    else:
        # Si 'a' n'est pas déjà dans la liste, on l'ajoute à la fin de la liste à l'aide de la méthode 'append'
        list.append(a)
        # Ligne commentée qui aurait affiché la liste à chaque itération
        # p(list)