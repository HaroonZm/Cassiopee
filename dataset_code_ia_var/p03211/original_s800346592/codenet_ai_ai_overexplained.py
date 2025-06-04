# Demande à l'utilisateur de saisir une chaîne de caractères (par exemple, une suite de chiffres)
s = input()

# Initialise une variable 'ans' avec la valeur entière 1000
# 'ans' va servir à stocker la plus petite différence trouvée pendant l'exécution de la boucle ci-dessous
ans = 1000

# Démarre une boucle 'for' qui va itérer sur les indices de la chaîne 's'
# La fonction 'range' génère une séquence de nombres, ici de 0 jusqu'à 'len(s) - 2' (exclu)
# On utilise 'len(s) - 2' pour s'assurer que l'index 'i+2' ne dépasse pas la longueur de 's',
# car nous allons extraire une sous-chaîne de longueur 3 à chaque itération.
for i in range(len(s) - 2):
    # À chaque itération, on extrait une sous-chaîne de 3 caractères consécutifs à partir de la position i.
    # 's[i:i+3]' veut dire "prend les caractères de l'index i jusqu'à (mais sans inclure) l'index i+3".
    sous_chaine = s[i:i+3]

    # On convertit la sous-chaîne extraite (3 caractères) en un entier avec int().
    valeur = int(sous_chaine)

    # On calcule la différence absolue entre cette valeur et 753
    difference = abs(valeur - 753)

    # On compare cette différence avec la plus petite différence trouvée jusque-là, stockée dans 'ans'.
    # La fonction 'min(a, b)' retourne la plus petite des deux valeurs 'a' et 'b'.
    # Si 'difference' est plus petite que 'ans', alors 'ans' prend la valeur de 'difference', sinon il reste inchangé.
    ans = min(difference, ans)

# Après la boucle, on affiche la plus petite différence trouvée.
print(ans)