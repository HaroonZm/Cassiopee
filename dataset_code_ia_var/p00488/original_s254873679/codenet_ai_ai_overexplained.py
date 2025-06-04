# Ce code va demander à l'utilisateur d'entrer plusieurs valeurs, trouver le minimum parmi deux groupes de valeurs
# puis effectuer une opération arithmétique finale en soustrayant 50 au total obtenu.
# Les commentaires expliquent chaque concept, même les plus basiques.

# On commence par demander les entrées du premier groupe :
# Nous utilisons une liste en compréhension pour stocker les entrées.
# [1,1,1] est une liste de longueur 3. Cela signifie que la boucle 'for' sera exécutée trois fois.
# 'i' est juste une variable de contrôle de boucle ; sa valeur importe peu ici.
# input() demande à l'utilisateur d'entrer une valeur. Par défaut, cette valeur est considérée comme une chaîne de caractères (str).
# Pour effectuer des calculs numériques, il faut convertir cette entrée en entier (int).
first_group = [int(input()) for i in [1, 1, 1]]  # Demande 3 fois une entrée utilisateur et les convertit en entier, stocké dans une liste

# On cherche le plus petit élément parmi les 3 valeurs saisies ci-dessus.
# La fonction min() prend une liste et retourne le plus petit élément de cette liste.
min_first = min(first_group)  # On conserve le minimum du premier groupe

# On recommence pour le deuxième groupe :
# [1,1] crée une liste de longueur 2, donc la boucle s'exécutera deux fois.
second_group = [int(input()) for i in [1, 1]]  # Demande 2 nouvelles entrées, converties en entier, stockées dans une liste

# On trouve aussi le plus petit élément parmi les valeurs du deuxième groupe.
min_second = min(second_group)  # Minimum du second groupe

# On additionne les deux minimums trouvés.
# L'opérateur '+' additionne les deux nombres.
total = min_first + min_second

# On soustrait 50 au total des deux minimums trouvés.
# L'opérateur '-' effectue une soustraction entre deux opérandes.
result = total - 50

# Enfin, on affiche le résultat final à l'aide de la fonction print().
# print() permet d'afficher ce que l'on veut à l'utilisateur dans la console.
print(result)  # Affiche le résultat final