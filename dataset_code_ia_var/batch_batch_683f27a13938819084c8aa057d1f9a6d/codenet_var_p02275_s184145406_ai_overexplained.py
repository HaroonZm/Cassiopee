# Définition de la fonction CountingSort qui prend en entrée :
#   - A : une liste d'entiers à trier.
#   - k : la plus grande valeur présente dans la liste A.
def CountingSort(A, k):
    # Initialisation du tableau de comptage C avec des zéros.
    # La taille du tableau est k+1 car les indices vont de 0 à k inclus.
    C = [0] * (k + 1)
    
    # Première boucle : compter le nombre d'occurrences de chaque valeur dans A.
    # Pour chaque élément 'a' dans la liste A, on incrémente la case correspondante dans C.
    for a in A:
        C[a] += 1  # On ajoute 1 à C[a] car la valeur 'a' a été rencontrée une fois de plus.
    
    # Deuxième boucle : calculer la somme cumulative dans le tableau C.
    # Ceci permet de savoir combien d'éléments sont inférieurs ou égaux à chaque valeur possible.
    # On commence à partir de l'indice 1 jusqu'à k inclus, car on cumule avec la valeur précédente.
    for i in range(k):
        C[i + 1] += C[i]  # On additionne la valeur du précédent à l'actuel.
    
    # Préparation de la liste de sortie 'ret', initialisée à zéro.
    # Sa taille est la même que celle de la liste A, car on veut trier tous les éléments d'A.
    ret = [0] * len(A)
    
    # Troisième boucle : parcours de la liste A à l'envers (du dernier au premier élément).
    # Ceci est important pour que l'algorithme soit stable (l'ordre des éléments identiques est conservé).
    for a in A[::-1]:  # A[::-1] crée une copie de A inversée.
        ret[C[a] - 1] = a  # On place 'a' à la bonne position dans la liste résultat.
        C[a] -= 1  # On décrémente la position dans C pour gérer un futur élément identique.
    
    # La liste 'ret' est maintenant triée, on la retourne comme résultat de la fonction.
    return ret

# Lecture d'un entier 'n' depuis l'entrée standard.
# Il représente le nombre d'éléments à trier.
n = int(input())  # L'utilisateur saisit un nombre (converti de chaîne à entier).

# Lecture de 'n' entiers depuis l'entrée standard, séparés par des espaces.
# La fonction map applique int() à chaque élément de l'entrée divisée par split(), puis on transforme le tout en liste.
A = list(map(int, input().split()))

# Appel de la fonction CountingSort avec la liste A et la plus grande valeur de A (pour déterminer la taille de C).
# max(A) retourne la plus grande valeur dans la liste A.
# L'opérateur * devant CountingSort(...) permet d'afficher tous les éléments de la liste triée séparés par un espace.
print(*CountingSort(A, max(A)))