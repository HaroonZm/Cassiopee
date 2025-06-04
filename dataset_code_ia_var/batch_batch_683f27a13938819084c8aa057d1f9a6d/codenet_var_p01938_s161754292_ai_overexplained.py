from sys import stdin  # Importe l'objet 'stdin' du module 'sys' pour lire l'entrée standard (par exemple, l'entrée utilisateur ou les fichiers redirigés)

# Lis une ligne de texte depuis l'entrée standard, élimine les caractères de fin de ligne (\n ou \r\n),
# puis ajoute le caractère "A" au début. Cela crée une nouvelle chaîne commençant par "A" suivie de l'entrée.
s = "A" + stdin.readline().rstrip()

# Crée une chaîne de caractères contenant toutes les lettres majuscules de l'alphabet anglais, de 'A' à 'Z'.
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Initialise une variable 'ans' à zéro, qui servira à compter le nombre d'occurrences détectées plus tard.
ans = 0

# Démarre une boucle for qui va de 1 jusqu'à la longueur de la chaîne 's' (non inclus),
# ce qui permet d'examiner chaque paire de caractères adjacents dans 's'.
for i in range(1, len(s)):
    # Utilise la méthode 'find' sur la chaîne 'AZ' pour obtenir la position de la lettre 's[i]' dans l'alphabet.
    # Faites de même avec la lettre précédente 's[i-1]'.
    # Compare les positions pour déterminer si la lettre courante n'est pas après (ou à la même position que)
    # la lettre précédente dans l'alphabet.
    if AZ.find(s[i]) <= AZ.find(s[i-1]):
        # Si la position de 's[i]' dans 'AZ' est inférieure ou égale à celle de 's[i-1]',
        # cela signifie que l'ordre alphabétique n'est pas strictement croissant ou qu'il y a une régression,
        # alors incrémente le compteur 'ans' de 1.
        ans += 1

# Affiche la valeur finale de 'ans', qui correspond au nombre de positions où une lettre
# n'est pas strictement plus grande (dans l'ordre alphabétique) que la précédente.
print(ans)