# Demande à l'utilisateur de saisir une entrée (par défaut une string)
a = list(input())  # Convertit la chaîne de caractères entrée en liste de caractères

# Boucle à travers tous les éléments de la liste 'a' pour les convertir en entiers
for i in range(len(a)):
    # Accède à la i-ème position de la liste et la convertit en entier
    a[i] = int(a[i])

# Initialise un compteur pour le résultat final à zéro. Ce compteur va stocker le nombre de cas qui remplissent certaines conditions.
ans = 0

# Boucle principale : parcourt chaque index de la liste 'a'
for i in range(len(a)):
    # Si l'élément à la position 'i' est égal à zéro, on passe à l'itération suivante (on saute le reste de la boucle)
    if a[i] == 0:
        continue

    # Initialise le nombre 'c' à zéro. Ce nombre va représenter la première partie du nombre séparé à la position 'i'.
    c = 0
    # Boucle pour construire le nombre 'c' en utilisant les chiffres de la position 0 à la position i-1 (non inclus)
    for j in range(i):
        # Multiplie 'c' par 10 pour décaler les chiffres vers la gauche (équivalent à ajouter un chiffre à droite)
        c *= 10
        # Ajoute le chiffre à la position 'j' à 'c'
        c += a[j]

    # Initialise le nombre 'd' à zéro. Ce nombre va représenter la deuxième partie du nombre à partir la position 'i' jusqu'à la fin.
    d = 0
    # Boucle pour construire le nombre 'd' en utilisant les chiffres de la position 'i' à la dernière position (inclus)
    for j in range(i, len(a)):
        # Multiplie 'd' par 10 pour décaler les chiffres de 'd' vers la gauche
        d *= 10
        # Ajoute le chiffre à la position 'j' à 'd'
        d += a[j]

    # Condition : si la somme des deux nombres 'c' et 'd' n'est pas paire (autrement dit, si elle est impaire)
    # L'opérateur % calcule le reste de la division par 2, != 0 signifie que le reste n'est pas zéro (impair)
    if (c + d) % 2 != 0:
        # Si la somme n'est pas paire, on n'exécute pas la suite, on passe à la prochaine itération
        continue

    # Calcule le nombre 'x' en tant que moitié de la somme de 'c' et 'd'. Ici, // représente la division entière.
    x = (c + d) // 2
    # Calcule le nombre 'y' en soustrayant 'x' de 'd'
    y = d - x

    # Vérifie que 'x' et 'y' sont tous deux supérieurs ou égaux à zéro.
    # Ceci garantit que les résultats sont valides (nombres entiers positifs ou nuls)
    if x >= 0 and y >= 0:
        # Si la condition est vérifiée, alors on incrémente le compteur 'ans' de 1
        ans += 1

# Affiche le résultat final à la fin du programme.
print(ans)  # 'ans' correspond au nombre total de cas où les conditions spécifiées sont satisfaites