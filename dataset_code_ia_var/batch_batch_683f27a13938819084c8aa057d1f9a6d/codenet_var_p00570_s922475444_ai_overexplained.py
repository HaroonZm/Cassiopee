# Demande à l'utilisateur de saisir deux valeurs entières séparées par un espace.
# Ces deux valeurs sont lues sous forme de chaîne de caractères par input().
# split() découpe la chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur.
# map(int, ...) applique la fonction int à chaque élément de la liste pour les convertir en entiers.
# Les deux entiers ainsi obtenus sont stockés dans les variables n et k.
n, k = map(int, input().split())

# Crée une liste t qui contiendra n éléments entiers.
# Pour chaque valeur dans la plage de 0 à n-1, on appelle input() pour lire un entier sur une ligne séparée.
# int(input()) convertit l'entrée en entier.
# Cette liste représente une série de temps ou de positions ordonnées croissantes, en fonction du contexte du problème.
t = [int(input()) for _ in range(n)]

# Crée une liste v de longueur n-1, initialisée à zéro pour chaque élément.
# Cette liste sera utilisée pour stocker des valeurs calculées à partir des éléments successifs de t.
# range(n-1) produit les indices de 0 à n-2 inclus, ce qui donne n-1 éléments.
v = [0 for _ in range(n - 1)]

# Boucle sur tous les indices de 0 à n-2 (inclus), donc sur chaque paire consécutive dans la liste t.
for i in range(n - 1):
    # À chaque itération, calcule la différence entre l'élément suivant et l'élément courant de t: t[i+1] - t[i].
    # Puis soustrait 1 à ce résultat.
    # Le résultat est stocké à la position i dans la liste v. 
    v[i] = t[i + 1] - t[i] - 1

# Trie la liste v en ordre décroissant (du plus grand au plus petit) en utilisant l'argument reverse = True.
# Ceci est utile pour accéder facilement aux plus grandes valeurs de v en début de liste.
v.sort(reverse = True)

# Calcule une valeur finale à afficher :
# - t[-1] donne le dernier élément de la liste t, c'est-à-dire la plus grande valeur.
# - t[0] donne le premier élément de t, c'est-à-dire la plus petite valeur.
# - t[-1] - t[0] + 1 mesure la distance (ou le nombre d'unités) entre le minimum et le maximum, en incluant les extrêmes.
# - v[:(k - 1)] sélectionne les k-1 premières valeurs de la liste v (celles qui sont les plus grandes à cause du tri).
# - sum(...) calcule la somme de ces k-1 valeurs.
# - Le résultat final consiste à soustraire cette somme de l'intervalle initial, réduisant la "longueur" totale de t en tenant compte des plus grands intervalles internes.
print(t[-1] - t[0] + 1 - sum(v[:(k - 1)]))