# Demander à l'utilisateur de saisir un nombre entier via l'entrée standard.
# La fonction input() lit une chaîne de caractères; int() la convertit en entier.
n = int(input())

# Vérifier si la valeur de n est strictement inférieure à 7.
if n < 7:
    # Si n est inférieur à 7, afficher le nombre 1 à l'écran.
    # La fonction print() écrit la valeur passée dans la console.
    print(1)
    # La fonction exit() termine immédiatement l'exécution du programme.
    exit()

# Calculer la partie entière de la division de n par 11.
# L'opérateur // est la division entière (quotient sans reste).
base = n // 11

# Multiplier le résultat précédent par 2, car chaque tranche complète de 11 compte pour 2.
result = base * 2

# Calculer le reste de la division de n par 11 en utilisant l'opérateur %.
remainder = n % 11

# Ajouter 1 à result si le reste est strictement supérieur à 0.
# L'expression (remainder > 0) donne True (équivalent à 1) si c'est vrai, sinon False (équivalent à 0).
result += (remainder > 0)

# Ajouter encore 1 à result si le reste dépasse 6 (c'est-à-dire s'il est au moins égal à 7).
result += (remainder > 6)

# Afficher la valeur finale de result.
print(result)