# Demande à l'utilisateur de saisir un entier depuis l'entrée standard (habituellement le clavier).
# Cela correspond généralement à la taille des listes qui seront introduites ensuite.
n = int(input())

# Demande à l'utilisateur de saisir une ligne de nombres entiers séparés par des espaces.
# 'input()' permet de recevoir cette ligne sous forme de chaîne de caractères.
# 'split()' divise la chaîne en sous-chaînes selon les espaces, pour donner une liste de chaînes numériques.
# 'map(int, ...)' convertit chaque chaîne en entier.
# 'list(...)' transforme le map object en une vraie liste Python d'entiers.
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

# Trie la liste a_list dans l'ordre croissant (du plus petit au plus grand)
# La méthode 'sort()' modifie la liste sur place.
a_list.sort()
b_list.sort()
c_list.sort()

# Création d'une liste vide n_b qui va stocker, pour chaque élément 'a' de a_list,
# le nombre d'éléments dans b_list qui sont strictement supérieurs à 'a'.
n_b = []  # Liste initialement vide

current = 0  # Un pointeur ou un index qui va nous permettre d'itérer dans b_list efficacement

# On parcourt tous les éléments de a_list par leur indice i (de 0 à n-1)
for i in range(n):
    a = a_list[i]  # On prend l'élément courant de a_list
    # Tant que le pointeur 'current' ne dépasse pas le dernier indice valide de b_list
    # et que l'élément b_list[current] est inférieur ou égal à 'a',
    # on incrémente current pour continuer à avancer dans b_list
    while current <= n-1 and b_list[current] <= a:
        current += 1
    # Lorsque la boucle s'arrête, current pointe sur le premier élément de b_list strictement supérieur à 'a'
    # Donc il y a (n - current) éléments dans b_list qui sont strictement supérieurs à 'a'
    n_b.append(n - current)  # On ajoute ce nombre à la liste n_b

# Même démarche pour compter, pour chaque élément de b_list,
# le nombre d'éléments dans c_list qui sont strictement supérieurs à cet élément.
n_c = []  # Liste qui va stocker pour chaque 'b' de b_list, le nombre d'éléments de c_list supérieurs à 'b'
current = 0  # On réinitialise le pointeur à 0
for i in range(n):
    b = b_list[i]
    # On avance dans c_list tant que l'élément courant est <= à 'b'
    while current <= n-1 and c_list[current] <= b:
        current += 1
    # On compte le nombre d'éléments strictement supérieurs à 'b' dans c_list
    n_c.append(n - current)

# Construction d'une liste cum_nc qui va stocker des sommes cumulées particulières tirées de n_c,
# utilisée dans la dernière partie du programme.
cum_nc = [0] * n  # Initialise une liste de n zéros

# On commence par y placer le dernier élément de n_c à la position 0 : cum_nc[0] = n_c[n-1]
cum_nc[0] = n_c[n-1]
# Pour chaque i de 1 à n-1, cum_nc[i] va contenir la somme de cum_nc[i-1] et d'un élément de n_c particulier :
for i in range(1, n):
    # Le terme n_c[n-1-i] sélectionne les éléments de n_c de la fin au début
    cum_nc[i] = cum_nc[i-1] + n_c[n-1-i]

# Initialisation de la variable ans qui servira à accumuler le résultat final
ans = 0

# Parcourt tous les éléments de n_b (qui correspond au nombre de bs>ai pour chaque ai)
for i in n_b:
    # On ne considère que les cas où i > 0 (donc il existe au moins un b > ai)
    if i > 0:
        # On ajoute à ans la valeur cum_nc[i-1]
        # Cela revient à additionner, pour chaque a, un cumul des combinaisons possibles avec c,
        # en fonction du nombre d'éléments dans b_list qui peuvent lui correspondre.
        ans += cum_nc[i-1]

# Affiche le résultat final
print(ans)