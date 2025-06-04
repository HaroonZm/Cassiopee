def counting_sort(n, A, k=10001):
    # n: Le nombre d'éléments dans le tableau A
    # A: Le tableau/list des éléments à trier, chaque élément étant un entier
    # k: La valeur maximale potentielle d'un élément de A, par défaut 10001 (pour compter de 0 à 10000 inclus)

    # Création d'une nouvelle liste C, de taille k, initialisée avec des zéros.
    # C servira à compter le nombre d'occurrences de chaque valeur présente dans A.
    # Par exemple, C[5] contiendra le nombre d'éléments égaux à 5 dans A.
    C = [0 for _ in range(k)]

    # Création d'une nouvelle liste B, de taille n, initialisée à 0.
    # B contiendra finalement le résultat du tri, c'est-à-dire la version triée de A.
    B = [0 for _ in range(n)]

    # Première boucle : On compte combien de fois chaque valeur apparaît dans A.
    # On parcourt tous les indices de A, de 0 à n-1 inclus.
    for i in range(n):
        # On prend l'élément A[i] (c'est un entier), et on incrémente de 1 la case correspondante dans C.
        # Par exemple, si A[i] vaut 3, alors C[3] sera incrémenté.
        C[A[i]] += 1

    # Deuxième boucle : Calcul du cumul des effectifs.
    # Pour chaque indice de 1 à k-1 (car le premier n'a pas de prédecesseur),
    # on ajoute à C[i] la valeur de C[i-1]. Après ce traitement,
    # C[i] indiquera combien d'éléments de A sont inférieurs ou égaux à i.
    for i in range(1, k):
        # On additionne la valeur de la case précédente à la case courante.
        C[i] = C[i] + C[i-1]

    # Troisième boucle : On place chaque élément de A à sa position triée dans B.
    # On parcourt A à l'envers (du dernier indice au premier), ce qui garantit la stabilité du tri.
    for j in range(n-1, -1, -1):
        # C[A[j]] contient le nombre total d'éléments <= A[j] dans A.
        # Donc, l'indice correct de A[j] dans B est C[A[j]]-1 (car l'indice commence à zéro).
        # On place l'élément A[j] à cet endroit précis dans B.
        B[C[A[j]]-1] = A[j]
        # On décrémente le compteur C[A[j]] de 1, car on a placé un élément de cette valeur,
        # pour que le prochain (éventuel) A[j] identique soit placé juste avant.
        C[A[j]] -= 1

    # On retourne le tableau trié B. Il contient les éléments de A rangés par ordre croissant.
    return B

def main():
    # On lit un entier n depuis l'entrée standard. Il représente le nombre d'éléments à trier.
    n = int(input())
    # On lit une ligne d'entrée, on la découpe en morceaux (séparés par des espaces)
    # et on convertit chaque morceau en entier grâce à la fonction map(int, ...).
    # On transforme ensuite le résultat en une liste. Cette liste forme le tableau A à trier.
    A = list(map(int, input().split()))
    # On appelle la fonction counting_sort avec nos paramètres, ce qui retourne la liste triée.
    # On affiche alors tous les éléments de la liste triée, séparés par des espaces, grâce à l'unpacking *.
    print(*counting_sort(n, A))

# Ce bloc vérifie si ce fichier est exécuté comme programme principal et non importé.
# Si c'est le cas, il appelle la fonction main() pour lancer le programme.
if __name__ == '__main__':
    main()