# Demander à l'utilisateur de saisir une chaîne de caractères, généralement constituée de chiffres.
# Utilise la fonction input(), qui récupère l'entrée standard sous forme de chaîne.
S = input()

# Initialisation d'une variable entière i à 0.
# Cette variable servira comme indice pour parcourir la chaîne S.
i = 0

# Initialiser la variable min_dif à 754.
# Cette variable va garder en mémoire la plus petite différence trouvée, initialisée ici à 754,
# car la différence minimale entre un nombre quelconque et 753 sera au maximum 754 (si le nombre est 0 ou 1507).
min_dif = 754

# Utilisation d'une boucle while pour parcourir la chaîne S.
# La boucle continue tant que i + 2 est inférieur ou égal à la longueur de S.
# Cela permet de toujours extraire un sous-ensemble de 3 caractères à partir de la position i,
# sans dépasser la fin de la chaîne.
while i + 2 <= len(S):
    # Extraire une sous-chaîne de 3 caractères de S à partir de la position i. S[i:i+3]
    # Par exemple, si S = "12345" et i = 1, S[1:4] == "234".
    # Ensuite, convertir cette sous-chaîne en entier avec int().
    x = int(S[i:i+3])
    
    # Calculer la valeur absolue de la différence entre x et 753.
    # abs(x - 753) renvoie la distance positive entre le nombre x extrait et 753.
    # Ensuite, on compare cette différence à la valeur actuelle de min_dif.
    # Si la différence courante est plus petite ou égale à min_dif,
    # alors on met à jour min_dif avec cette nouvelle valeur.
    if min_dif >= abs(x - 753):
        min_dif = abs(x - 753)
    
    # Incrémenter i de 1 pour passer à la prochaine position de la chaîne,
    # afin d'examiner le prochain groupe de 3 chiffres consécutifs.
    i += 1

# Quand la boucle est terminée, cela signifie que tous les groupes de 3 chiffres consécutifs
# de la chaîne S ont été examinés, et min_dif contient maintenant la plus petite différence trouvée.
# On affiche min_dif à l'écran avec la fonction print, ce qui montre le résultat à l'utilisateur.
print(min_dif)