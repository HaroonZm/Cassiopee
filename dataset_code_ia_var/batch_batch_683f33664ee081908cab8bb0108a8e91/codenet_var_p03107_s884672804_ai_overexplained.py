# Demande à l'utilisateur d'entrer une chaîne de caractères à traiter
# Par défaut, input() lit une ligne de texte depuis la saisie utilisateur
# Ensuite, on utilise une compréhension de liste pour transformer chaque caractère de la chaîne en entier, et on stocke le tout dans la liste S
# Ici, chaque caractère '0' devient l'entier 0, chaque '1' devient l'entier 1, etc.
S = [int(x) for x in input()]

# Calcule la somme totale des éléments de la liste S
# Cela additionne tous les chiffres, c'est-à-dire tous les 1 et tous les 0 convertis préalablement en entiers
# Cette somme correspond donc à la quantité de chiffres '1' dans la chaîne initiale saisie
o = sum(S)

# Calcule la différence absolue entre la longueur totale de la liste S (le nombre de caractères saisis)
# et la somme des chiffres (le nombre de '1')
# En effet, la longueur totale moins le nombre de '1' donne le nombre de '0' dans la liste
# abs() assure que le résultat est positif, ce qui est dans ce contexte facultatif car il sera toujours >= 0
z = abs(len(S) - o)

# Calcule la valeur minimale entre le nombre de '1' (o) et le nombre de '0' (z)
# Multiplie cette valeur minimale par 2
# Ceci donne le nombre maximal de paires (1,0) qui peuvent être formées et supprimées de la chaîne,
# chaque paire nécessitant un '1' et un '0'
# Affiche ce nombre
print(min(o, z) * 2)