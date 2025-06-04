# Lire une ligne de l'entrée utilisateur (saisie clavier), supprimer les espaces inutiles au début et à la fin puis séparer la ligne en morceaux selon les espaces.
# Pour chaque morceau, le transformer en entier grâce à int(s), et placer le résultat dans une liste.
# Cette liste contient deux éléments : le premier est n, le nombre d'éléments dans la liste suivante, et le second est k, le nombre d'opérations.
n, k = [int(s) for s in input().strip().split()]

# Lire la ligne suivante (hauteurs), supprimer les espaces en trop au début et à la fin, puis découper la chaîne selon les espaces pour obtenir chaque nombre sous forme de chaîne.
# Pour chaque chaîne obtenue, la convertir en entier avec int(s), et construire la liste H qui contient toutes ces hauteurs sous forme entière.
H = [int(s) for s in input().strip().split()]

# Vérifier si le nombre d'opérations k est supérieur ou égal au nombre d'éléments n.
# Si c'est le cas, cela signifie que nous pouvons supprimer ou ignorer tous les éléments de la liste H.
if k >= n:
    # Dans ce cas, il ne reste rien, donc le résultat est 0.
    result = 0
else:
    # Si le nombre d'opérations k est strictement inférieur au nombre d'éléments n,
    # nous devons garder certains éléments.
    
    # Trier la liste H (les hauteurs) par ordre croissant. Cela place les plus petits avant les plus grands.
    H.sort()
    
    # Pour minimiser la somme, il faut supprimer (ou ignorer) les k plus grands éléments.
    # Pour ce faire, on garde seulement les (n - k) plus petits éléments de la liste triée.
    # H[:n - k] signifie 'prendre les éléments depuis le début de H jusqu'à l'indice (n-k)-1 inclus'.
    # sum(H[:n - k]) calcule la somme de ces éléments restants.
    result = sum(H[:n - k])

# Afficher le résultat final (la somme calculée ou 0 si tout a été supprimé).
print(result)