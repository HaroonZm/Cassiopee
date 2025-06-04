from collections import Counter  # Importe la classe Counter de la bibliothèque collections
# Counter permet de compter les occurrences des éléments dans des objets itérables

def inpl():
    # Cette fonction lit une ligne depuis l'entrée standard (input)
    # Sépare la ligne en chaînes individuellement sur les espaces (split())
    # Convertit chaque chaîne en entier (map(int, ...))
    # Place le tout dans une liste (list(...))
    return list(map(int, input().split()))

N = int(input())  # Lit une ligne depuis l'entrée standard, la convertit en entier et la stocke dans N. N représente probablement le nombre d'éléments de la liste A.

A = inpl()  # Appelle la fonction inpl() pour lire une liste de N entiers depuis l'entrée. A stocke ces entiers.

Ai = range(N)  # Crée un objet de type range allant de 0 à N-1. Permet de représenter les indices valides de la liste A.

Ad = {a:i for i, a in enumerate(A)}  
# Crée un dictionnaire.
# Pour chaque couple (indice, élément) obtenu grâce à enumerate(A):
#    - 'a' est la valeur d'un élément de la liste A
#    - 'i' est son indice dans la liste
# Ad associe chaque valeur de A à son indice dans A, c'est-à-dire Ad[valeur] = index dans la liste A

F = inpl()  # Lit et stocke une autre liste d'entiers depuis l'entrée. F contient N entiers également.

C = [0]*N  # Crée une liste de N zéros. Cette liste servira à compter le nombre d'apparitions des valeurs F dans la liste A, à l'indice associé à la valeur.

for f in F:
    # Pour chaque élément f dans la liste F (chaque f est un entier)
    C[Ad[f]] += 1  # Trouve l'indice correspondant à la valeur f dans la liste A grâce au dictionnaire Ad,
                   # puis incrémente la valeur à cet indice dans la liste C de 1.
                   # Cela compte le nombre d'occurrences de chaque élément de F, mappé sur la position de cet élément dans A.

if not 0 in C:  
    # Teste si le nombre 0 n'est PAS dans la liste C.
    # Cela signifie que chaque valeur de A (en fait chaque valeur mappée par Ad depuis F) a été comptée au moins une fois.
    print("Yes")  # Si aucune case de C ne contient 0, on affiche "Yes" (toutes les valeurs de A sont couvertes par F)
else:
    print("No")  # Sinon, au moins une valeur de A n'est pas couverte, on affiche "No"
    print(*list(map(str, A)))  
    # Convertit chaque élément de la liste A en chaîne de caractères
    # L'étoile * "dégrappe" la liste, affichant chaque élément séparé par un espace
    # Cela affiche l'ensemble courant A tel quel.
    lack = C.index(0)  
    # Cherche le premier indice dans la liste C pour lequel la valeur est 0,
    # c'est-à-dire la première valeur de A qui n'est pas apparue dans F.
    ans = A[:lack] + [A[lack-1]] + A[lack+1:]  
    # Construit une nouvelle liste ans :
    # - Prend la partie de A avant l'indice 'lack' (A[:lack]), c'est-à-dire du début jusqu'à l'élément manquant (exclu)
    # - Ajoute l'élément qui précède l'élément manquant (A[lack-1]), pour remplacer la valeur manquante
    # - Ajoute le reste de la liste après l'élément manquant (A[lack+1:])
    # Cette opération simule le remplacement de l'élément manquant par la valeur qui le précède dans la liste.
    print(*ans)  
    # Affiche le contenu de la liste 'ans' avec les valeurs séparées par des espaces.
    # Cela produit une nouvelle configuration de la liste A en essayant de corriger le problème détecté.