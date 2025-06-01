# Demande à l'utilisateur de saisir une ligne de texte qui contiendra plusieurs valeurs séparées par des espaces
# input() est une fonction intégrée qui attend que l'utilisateur entre une chaîne de caractères au clavier puis appuie sur Entrée
# L'utilisateur est censé entrer ici trois nombres séparés par des espaces

# La méthode .split() appliquée sur la chaîne de caractères retournée par input() découpe cette chaîne en plusieurs sous-chaînes 
# en utilisant par défaut l'espace comme séparateur. Cela crée une liste de chaînes représentant chaque nombre entré.
# Par exemple, si l'utilisateur tape "1.0 2.0 3.0", .split() retourne ["1.0", "2.0", "3.0"]

# La compréhension de liste [float(i) for i in input().split()] parcourt chaque élément i de la liste créée par .split()
# et convertit cette chaîne de caractères i en un nombre décimal (float) grâce à la fonction float()
# Cela produit une liste de trois nombres à virgule flottante, prêts à être utilisés dans des calculs numériques

# L'affectation multiple a,t,r = [...] prend les trois nombres de cette liste dans l'ordre 
# et les assigne respectivement aux variables a, puis t, puis r
# C'est une manière concise d'écrire : 
# a = liste[0]
# t = liste[1]
# r = liste[2]

a,t,r = [float(i) for i in input().split()]

# Calcule l'expression t * r / a:
# D'abord, la multiplication t * r est effectuée, car l'opérateur * est évalué avant /
# Ensuite, le résultat de cette multiplication est divisé par a

# print() est une fonction intégrée qui affiche le résultat dans la console,
# c’est-à-dire à l'écran, pour que l'utilisateur puisse le voir

print(t * r / a)