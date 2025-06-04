# Demander à l'utilisateur d'entrer deux entiers séparés par un espace sur une seule ligne
# La fonction input() lit la ligne en tant que chaîne de caractères (string)
# La méthode split() découpe la chaîne de caractères en une liste de sous-chaînes là où il y a des espaces
# La fonction map(int, ...) applique la conversion en entier (int) à chaque sous-chaîne obtenue
# La fonction list(...) transforme le résultat de map (un itérable) en une liste d'entiers
n, k = list(map(int, input().split()))

# Vérifier si la valeur de k est exactement égale à 0
if k == 0:
    # Afficher le carré de n (c'est-à-dire n multiplié par lui-même)
    print(n**2)
    # Arrêter immédiatement l'exécution du programme puisqu'il n'y a rien d'autre à faire dans ce cas
    exit()
    
# Initialiser la variable de réponse (ans) à 0
ans = 0

# Lancer une boucle for où la variable b prend toutes les valeurs entières de k+1 jusqu'à n inclus (c'est-à-dire l'intervalle [k+1, n])
# La fonction range(a, b) génère une séquence allant de a jusqu'à b-1, donc on ajoute 1 à n pour l'inclure
for b in range(k+1, n+1):
    # Calculer le nombre de fois où on peut soustraire b de n-k (division entière)
    # Cette quantité est augmentée de 1 parce qu'on compte également le terme initial
    # Cela correspond au nombre de "blocs" entiers de taille b entre k et n
    ans_bk = (n - k) // b + 1
    
    # Multiplier ce nombre par (b-k) pour obtenir le nombre de cas "complets" correspondants à cette valeur de b
    # Cela représente toutes les valeurs possibles quand le reste obtenu (lorsqu'on divise) varie de k à b-1
    ans_b = ans_bk * (b - k)
    
    # Calculer jusqu'où va le dernier de ces blocs (la valeur maximum de la formule)
    mod_k_max = ((n - k) // b) * b + k
    
    # Tester s'il y a un "blanc" à la fin, c'est-à-dire si le bloc final ne contient pas toutes les (b-k) valeurs attendues
    # Si c'est le cas, il faut retirer le nombre de cas excédentaires dans ans_b parce qu'ils ne correspondent à aucune valeur comprise dans [k, n]
    if n - mod_k_max + 1 < b - k:
        # Soustraire le nombre d'occurrences qui débordent du nombre réel de valeurs disponibles
        ans_b -= ((b - k) - (n - mod_k_max + 1))
    # À ce point, ans_b est le nombre exact de couples (a, b) pour ce b donné
    
    # Ajouter ce nombre exact à la variable cumulative de réponse ans
    ans += ans_b

# Après avoir traité toutes les valeurs possibles de b, afficher la réponse finale
print(ans)