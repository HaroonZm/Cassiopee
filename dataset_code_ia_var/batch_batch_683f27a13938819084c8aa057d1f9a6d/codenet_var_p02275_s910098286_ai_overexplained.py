# Définition de la fonction countingsort prenant deux arguments :
# - A : une liste d'entiers à trier.
# - k : la valeur maximale possible parmi les éléments de A (on suppose A ne contient pas d'éléments > k).
def countingsort(A, k):
    # Création de la liste de résultat res qui aura la même taille que la liste d'origine A.
    # On initialise chaque élément de res à None.
    # On utilise ici une compréhension de liste pour itérer sur chaque élément de A sans s'intéresser à sa valeur.
    res = [None for _ in A]
    
    # Création d'une liste de comptage (C) contenant k+1 éléments (de l'indice 0 à l'indice k).
    # Tous les éléments de cette liste sont initialisés à 0.
    # Cette liste servira à compter combien de fois chaque valeur (comprise entre 0 et k) apparaît dans A.
    C = [0 for i in range(k + 1)]
    
    # Parcours de tous les éléments de la liste A.
    # Pour chaque élément x, on incrémente la valeur correspondante dans la liste C à la position x.
    # Cela permet de "compter" combien de fois chaque valeur apparaît dans A.
    for x in A:
        C[x] += 1
    
    # Parcours de tous les indices i de 0 à k-1.
    # On transforme la liste de comptage C pour obtenir des positions d'insertion.
    # Pour chaque valeur de i, on ajoute la valeur de C[i] à C[i+1].
    # Ainsi, C[i] indiquera à la fin combien de valeurs dans A sont inférieures ou égales à i.
    for i in range(k):
        C[i + 1] = C[i + 1] + C[i]
    
    # Parcours des éléments de A dans l'ordre inverse (du dernier au premier).
    # Ceci permet d'assurer que l'algorithme soit "stable", c'est-à-dire que l'ordre des éléments égaux soit conservé.
    for x in reversed(A):
        # On place l'élément x à la position correspondant à C[x]-1 dans le tableau res.
        # C[x] représente le nombre d'éléments dans A inférieur ou égal à x, donc l'indice de l'élément x correctement trié est C[x] - 1.
        res[C[x] - 1] = x
        # On décrémente C[x] afin de gérer le cas où la même valeur apparaisse plusieurs fois dans la liste.
        # Ainsi, à chaque insertion d'un x, on place l'élément précédent x à l'indice juste avant.
        C[x] -= 1
    
    # On renvoie la liste triée res.
    return res

# Appel de la fonction input() sans sauvegarder le résultat.
# Cette instruction attend une entrée sur une ligne mais ne fait rien avec. 
# Cela correspond généralement à une lecture du nombre d'éléments, qui n'est pas utilisée ici.
input()

# Lecture de la ligne suivante en entrée standard, qui est censée contenir des entiers séparés par des espaces.
# La fonction input() lit la ligne, map(int, ...) permet de convertir chaque élément texte en entier.
# On transforme le résultat de map en une liste d'entiers qui sera stockée dans la variable A.
A = list(map(int, input().split()))

# Appel de la fonction countingsort sur la liste de nombres A, en utilisant 10000 comme valeur maximale k.
# Cela suppose qu'aucun nombre dans A ne dépassera 10000. Le résultat trié est stocké dans la variable ret.
ret = countingsort(A, 10000)

# Affichage du résultat.
# On convertit chaque élément de ret (une liste d'entiers triés) en chaîne de caractères à l'aide de map.
# Ensuite, on joint toutes les chaînes en une seule, séparées par des espaces, grâce à " ".join().
# Enfin, on affiche la chaîne obtenue avec print.
print(" ".join(map(str, ret)))