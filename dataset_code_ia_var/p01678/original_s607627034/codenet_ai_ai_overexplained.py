#!/usr/bin/env python

# Importation du module 'deque' depuis le module standard 'collections'.
# 'deque' signifie 'double-ended queue' et permet d'ajouter et d'enlever des éléments par les deux extrémités de façon efficace.
from collections import deque

# Importation du module 'itertools' sous le nom de 'it'.
# 'itertools' contient des fonctions utiles pour gérer les itérateurs de manière efficace.
import itertools as it

# Importation du module 'sys' pour interagir avec l'environnement d'exécution Python.
import sys

# Modification de la limite de récursion du programme.
# Par défaut, Python limite la profondeur de récursion pour éviter les débordements de pile (stack overflow).
# Ici, on fixe la limite à un million, ce qui permet de faire un très grand nombre d'appels récursifs sans erreur.
sys.setrecursionlimit(1000000)

# Définition d'une constante INF (abréviation pour 'infinity') utilisée plus tard pour effectuer des opérations modulo,
# assurant que les grands nombres restent gérables et limitent l'apparition d'entiers trop grands.
# Cette valeur est un grand nombre premier, communément utilisé dans les compétitions de programmation pour les modulos.
INF = 1000000007

# Début d'une boucle infinie.
# On lit des entrées utilisateur jusqu'à ce qu'une condition d'arrêt soit atteinte (ici, si l'entrée vaut '0').
while True:
    # Lecture d'une première chaîne de caractères depuis l'entrée standard.
    # 'raw_input()' est la fonction pour lire une entrée ligne par ligne sous Python 2.
    # Elle demande à l'utilisateur de saisir une valeur et retourne cette valeur sous forme de chaîne de caractères.
    A = raw_input()
    
    # Vérification si la chaîne saisie est égale à '0'.
    # Si c'est le cas, cela signifie que l'utilisateur souhaite arrêter le programme,
    # on sort donc de la boucle principale grâce à l'instruction 'break'.
    if A == '0':
        break
    
    # Lecture des deux entrées suivantes (deux autres chaînes de caractères).
    B = raw_input()
    C = raw_input()
    
    # Inversion des chaînes saisies pour faciliter l'alignement en partant du chiffre des unités.
    # Cette opération transforme '123' en '321', par exemple.
    A = A[::-1]
    B = B[::-1]
    C = C[::-1]

    # Vérification de la validité des longueurs des chaînes :
    # on regarde si la longueur maximale entre A et B est égale à la longueur de C ou de C+1.
    # Si ce n'est pas le cas, alors il n'existe aucune solution possible, donc on affiche '0' et on passe à la prochaine itération.
    if not max(len(A), len(B)) in [len(C), len(C) + 1]:
        print 0
        continue
    
    # Complétion des chaînes A et B en ajoutant les caractères '0' à droite, jusqu'à ce que leur longueur égale celle de C.
    # Cela permet de s'assurer que toutes les chaînes sont de même longueur pour l'alignement positionnel des chiffres.
    while len(A) < len(C):
        A += '0'  # Ajout du caractère '0' à la fin de la chaîne A
    
    while len(B) < len(C):
        B += '0'  # Ajout du caractère '0' à la fin de la chaîne B
    
    # Initialisation des variables de comptage pour la dynamique :
    # rem0 compte le nombre de configurations possibles SANS report sur la colonne courante,
    # rem1 compte le nombre de configurations possibles AVEC report d'une retenue (retenue = '1') sur la colonne courante.
    # Initialement, il ne peut pas y avoir de report sur la première colonne donc rem0 commence à 1 et rem1 à 0.
    rem0 = 1  # représente les façons d'obtenir un résultat sans report (retenue)
    rem1 = 0  # représente les façons d'obtenir un résultat avec report (retenue)

    # Parcours de chaque position (chiffre) des chaînes de chiffres, en commençant par le chiffre des unités (puisque les chaînes ont été inversées).
    for index in range(len(C)):
        # Initialisation des compteurs pour la prochaine position, toujours 0 au début.
        nex0 = 0  # nombre de nouvelles façons d'arriver ici SANS retenue
        nex1 = 0  # nombre de nouvelles façons d'arriver ici AVEC retenue

        # Détermination des valeurs possibles pour le chiffre courant de A à la position 'index':
        # Si le caractère est '?', c'est un chiffre indéfini donc on essaiera toutes les valeurs autorisées,
        # sinon il n'y a qu'une possibilité : le chiffre donné.
        # On utilise 'range' pour générer tous les chiffres valides possibles pour ce rang (0 à 9, sauf pour les positions les plus à gauche pour éviter les zéros significatifs).
        if A[index] == '?':
            # Calcul du chiffre minimum valable pour éviter les zéros non significatifs dans les positions de poids fort.
            # Pour les unités, on peut utiliser 0, mais si c'est la position la plus à gauche, on doit commencer par 1.
            la = range(max(0, index - len(C) + 2), 10)
        else:
            # Si un chiffre est déjà donné, on l'utilise tel quel (le chiffre est stocké sous forme de caractère, conversion en entier nécessaire).
            la = [int(A[index])]
        
        # Même logique appliquée pour le chiffre correspondant de B.
        if B[index] == '?':
            lb = range(max(0, index - len(C) + 2), 10)
        else:
            lb = [int(B[index])]
        
        # Même logique appliquée pour C.
        if C[index] == '?':
            lc = range(max(0, index - len(C) + 2), 10)
        else:
            lc = [int(C[index])]
        
        # On parcourt toutes les combinaisons possibles de chiffres pour A, B, et C à cette position,
        # en utilisant le produit cartésien de tous les choix possibles pour chaque chiffre inconnu.
        for a, b, c in it.product(la, lb, lc):
            # Pour chaque triplet de chiffres (a pour A, b pour B, c pour C) :
            # Quatre cas de figures possibles (avec ou sans report) pour l'addition des chiffres.

            # Cas 1 : pas de report, la somme des chiffres actuels (a+b) doit égaler c (le chiffre cible à cette colonne).
            if a + b == c:
                nex0 += rem0  # On ajoute le nombre de façons d'arriver ici sans report.

            # Cas 2 : pas de report, mais la somme (a+b) dépasse 9, donc il y a une retenue de 1 à reporter sur la position suivante.
            # Ici, a+b == 10 + c, car la retenue est générée, et le chiffre colonne est donc c (somme - 10).
            if a + b == 10 + c:
                nex1 += rem0  # On ajoute le nombre de façons d'arriver ici sans report mais avec retenue pour la suite.

            # Cas 3 : si on arrive à cet index AVEC retenue (rem1),
            # alors a+b+cumulé avec la retenue précédente doit égaler c (donc a+b == c-1).
            if a + b == c - 1:
                nex0 += rem1  # On ajoute le nombre de façons d'arriver ici avec report, mais la somme ne génère pas de nouvelle retenue.

            # Cas 4 : si on arrive ici AVEC retenue et la somme génère aussi une nouvelle retenue,
            # alors a+b == 10 + c - 1 (car il y avait un report et un nouveau report).
            if a + b == 10 + c - 1:
                nex1 += rem1  # On ajoute le nombre de façons d'arriver ici avec report et où cela génère une nouvelle retenue.
        
        # Application du modulo à chaque étape pour éviter le dépassement des entiers (overflow) :
        # Seul le reste de la division par INF est conservé.
        rem0 = nex0 % INF
        rem1 = nex1 % INF

    # Une fois toutes les positions de chiffres parcourues, on affiche le nombre total de façons d'obtenir le résultat
    # sans retenue finale (rem0), ce qui signifie que l'addition s'est bien "terminée" sans report à la fin.
    print rem0