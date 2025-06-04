import sys  # On importe le module 'sys' pour permettre l'utilisation de sys.exit() afin d'arrêter proprement l'exécution du programme si nécessaire.

# Lecture de deux entiers à partir de la première ligne d'entrée utilisateur. On suppose que l'utilisateur va entrer deux nombres entiers séparés par un espace.
# Ces deux entiers sont stockés dans les variables n et k.
n, k = map(int, input().split())

# Lecture d'une séquence d'entiers à partir de la deuxième ligne d'entrée utilisateur.
# Cette séquence représente les éléments d'un tableau/list et est stockée dans la liste 'a'.
a = list(map(int, input().split()))

# Calcul du maximum de la liste 'a' afin de déterminer la plus grande valeur dans cette liste.
tmp = max(a)

# Calcul d'une nouvelle valeur 'tmp2' qui est le maximum parmi tmp, n et k, auquel on ajoute 1.
# Cela permet d'avoir une taille suffisante pour le tableau 'chk' qui sera utilisé ensuite.
tmp2 = max(tmp, n, k) + 1

# Création d'une liste 'chk' de taille 'tmp2' initialisée à 0. Cette liste va servir à compter les occurrences de chaque valeur présente dans la liste 'a'.
chk = [0] * (tmp2)

# Boucle pour compter combien de fois chaque élément de 'a' apparaît dans la liste.
# Pour chaque index i allant de 0 à n-1 (n éléments au total), on incrémente la valeur correspondant à a[i] dans la liste 'chk'.
for i in range(n):
    chk[a[i]] += 1

# Vérification que toutes les valeurs entre 1 et k (inclus) apparaissent au moins une fois dans 'a'.
# La sous-liste chk[1:k+1] correspond alors au nombre de fois que chaque nombre entre 1 et k apparaît dans 'a'.
# Si 0 apparaît dans cette sous-liste, cela signifie qu'au moins un nombre dans l'intervalle 1..k n'est pas présent dans 'a'.
# Si c'est le cas, on affiche 0, puis on termine le programme immédiatement avec sys.exit() pour éviter toute exécution supplémentaire.
if 0 in chk[1:k+1]:
    print(0)
    sys.exit()

# Initialisation de la variable 'right' avec la valeur n-1. Cette variable va être utilisée comme indice de la fin de la fenêtre courante d'étude dans la liste 'a'.
right = n - 1

# Initialisation de la variable 'left' avec la valeur 0. Cette variable va être utilisée comme indice du début de la fenêtre courante d'étude dans la liste 'a'.
left = 0

# Initialisation d'une liste vide 'L' qui va stocker les longueurs de différentes fenêtres/subséquences étudiées au cours de l'algorithme.
L = []

# Début d'une boucle principale. Tant que l'indice 'right' est inférieur à n,
# cela veut dire que la fenêtre d'étude demeure dans les bornes du tableau.
while right < n:

    # Cette boucle intérieure sert à diminuer la taille de la fenêtre par la droite ('right')
    # tant que le nombre à l'indice 'right' apparaît plus d'une fois dans la fenêtre
    # ou que sa valeur dépasse k (ce qui la rend invalide pour notre problème).
    while chk[a[right]] > 1 or a[right] > k:
        chk[a[right]] -= 1  # On retire une occurrence de cet élément du compteur.
        right -= 1  # On déplace la borne droite de la fenêtre vers la gauche.

    # Calcul de la longueur actuelle de la fenêtre valide, c'est-à-dire le nombre d'éléments
    # qu'il y a entre les indices 'left' et 'right' (inclus).
    ln = right - left + 1

    # On ajoute cette longueur à la liste des longueurs trouvées.
    L.append(ln)

    # Cette boucle intérieure sert cette fois à déplacer la borne gauche de la fenêtre ('left')
    # tant que l'élément en position 'left' apparaît plus d'une fois dans la fenêtre
    # ou que sa valeur est supérieure à k.
    while chk[a[left]] > 1 or a[left] > k:
        chk[a[left]] -= 1  # On retire sa contribution dans le compteur d'occurrences.
        left += 1  # On avance la borne gauche de la fenêtre.

    # Nouvelle longueur de fenêtre après déplacement de 'left'. À nouveau, on calcule la taille de la fenêtre et on l'ajoute à la liste des longueurs.
    ln = right - left + 1
    L.append(ln)

    # On retire du compteur l'élément à la nouvelle position 'left' puis on avance encore 'left'.
    # Cela permet d'explorer différentes positions pour le début de la fenêtre.
    chk[a[left]] -= 1
    left += 1

    # Cette boucle vise à faire avancer à nouveau 'right' pour "rééquilibrer" la fenêtre,
    # c'est-à-dire rajouter des éléments jusqu'à ce que tous les éléments nécessaires soient à nouveau présents.
    # On augmente 'right' tant que la dernière occurrence retirée n'est plus présente dans la fenêtre.
    while chk[a[left - 1]] == 0:
        right += 1  # On étend la fenêtre par la droite.
        if right >= n:  # Si on dépasse la limite du tableau, on arrête la boucle.
            break
        chk[a[right]] += 1  # On compte la nouvelle occurrence ajoutée à la fenêtre.

    # À la fin de ce processus, on recalcul encore la longueur de la fenêtre courante et on l'ajoute à la liste 'L'.
    ln = right - left + 1
    L.append(ln)

# À la fin de la boucle, la liste 'L' contient les différentes tailles de fenêtre valides rencontrées.
# On affiche la plus petite de ces longueurs, qui correspond à la plus petite fenêtre contenant tous les nombres de 1 à k.
print(min(L))  # Affiche le résultat final qui est la taille minimale recherchée.