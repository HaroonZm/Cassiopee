# Demande à l'utilisateur de saisir un nombre entier au clavier
# La fonction input() récupère une chaîne de caractères depuis la console
# int() convertit cette chaîne de caractères en nombre entier
a = int(input())  # Stocke la première valeur saisie dans la variable 'a'

# Demande une deuxième saisie utilisateur d'un nombre entier
b = int(input())  # Stocke la deuxième valeur saisie dans la variable 'b'

# Trouve le plus petit nombre entre 'a' et 'b' grâce à la fonction min()
# min(a, b) retourne la plus petite des deux valeurs
X = min(a, b)  # Stocke ce minimum dans la variable 'X'

# Demande une nouvelle saisie utilisateur, pour remplacer la valeur de 'a'
a = int(input())  # Cette nouvelle saisie écrase la valeur précédente de 'a'

# Demande une quatrième saisie utilisateur, pour remplacer la valeur de 'b'
b = int(input())  # Cette nouvelle saisie écrase la valeur précédente de 'b'

# Trouve le minimum entre ces deux nouvelles valeurs
# Encore une fois, min(a, b) détermine le plus petit des deux
Y = min(a, b)  # Stocke ce minimum dans la variable 'Y'

# Additionne les deux minimums trouvés précédemment : 'X' et 'Y'
# Utilise l'opérateur d'addition '+'
# print() affiche le résultat final de cette addition dans la console
print(X + Y)  # Affiche le résultat de X + Y à l'utilisateur