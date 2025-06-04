# Demande à l'utilisateur de saisir une valeur entière qui sera stockée dans la variable 'time'.
# Cette valeur représente le nombre d'éléments dans la séquence qui sera traitée par le programme.
time = int(input())  # Conversion explicite de l'entrée utilisateur (qui est une chaîne de caractères) en entier

# Demande à l'utilisateur de saisir une séquence de valeurs séparées par des espaces.
# Utilise la méthode split() pour diviser la chaîne saisie en plusieurs sous-chaînes, chacune représentant un nombre.
# Utilise une compréhension de liste pour convertir chaque sous-chaîne en entier en utilisant int().
# Stocke la liste des entiers dans la variable 'nums'.
nums = [int(i) for i in input().split()]

# Initialise un compteur pour le nombre de nombres impairs rencontrés dans la séquence. Commence à 0.
odd = 0

# Initialise un compteur pour le nombre de nombres pairs rencontrés dans la séquence. Commence à 0.
even = 0

# Initialise un compteur pour le nombre de nombres pairs qui sont divisibles par 3 ou par 5.
# Commence également à 0.
even35 = 0

# Parcourt la séquence à l'aide d'une boucle for pour examiner chaque élément individuellement.
# La boucle utilise la fonction range() pour générer des indices de 0 à time-1.
for j in range(time):
    # Vérifie si l'élément courant (nums[j]) est pair en utilisant l'opérateur modulo (%).
    # Si un nombre modulo 2 est égal à 0, cela signifie que le nombre est pair.
    if nums[j] % 2 == 0:
        # Incrémente le compteur 'even' d'une unité car nums[j] est pair.
        even += 1
        # À l'intérieur de la branche pair, vérifie une condition supplémentaire :
        # Teste si nums[j] n'est pas divisible par 3 ET n'est pas divisible par 5.
        # Cela signifie que si nums[j] modulo 3 n'est PAS égal à 0 ET nums[j] modulo 5 n'est PAS égal à 0.
        if nums[j] % 3 != 0 and nums[j] % 5 != 0:
            # Si la condition précédente est vraie, on passe à l'itération suivante de la boucle sans exécuter ce qui suit.
            continue  # L'instruction continue arrête cette itération et passe à la suivante.
        else:
            # Si nums[j] est divisible par 3 ou par 5 (ou les deux), incrémente le compteur 'even35'.
            even35 += 1
    else:
        # Si nums[j] n'est PAS pair (donc il est impair), alors on incrémente le compteur 'odd'.
        odd += 1

# Après la fin de la boucle, tous les éléments de la liste ont été examinés et les compteurs ont été mis à jour.
# Vérifie maintenant si tous les nombres pairs de la séquence sont aussi comptés dans 'even35'.
# Cela revient à tester si tous les nombres pairs sont aussi divisibles par 3 ou par 5.
if even35 == even:
    # Si c'est le cas (tous les nombres pairs dans la séquence sont divisibles par 3 ou 5), affiche 'APPROVED'.
    print("APPROVED")
else:
    # Sinon (il existe au moins un nombre pair qui n'est divisible ni par 3 ni par 5), affiche 'DENIED'.
    print("DENIED")