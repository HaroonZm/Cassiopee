# Demande à l'utilisateur de saisir la chaîne de caractères principale (texte) et la stocke dans la variable T.
T = input()

# Demande à l'utilisateur de saisir la sous-chaîne à rechercher (motif) et la stocke dans la variable P.
P = input()

# Calcule la longueur de la chaîne P avec la fonction len et la stocke dans la variable p.
p = len(P)

# Utilise une boucle for pour parcourir chaque indice possible dans T où P pourrait apparaître.
# La fonction range() prend trois arguments : début (par défaut 0), fin (ici, len(T)-p+1), et le pas (par défaut 1).
# On s'arrête à len(T) - p + 1 car après cette position, P ne pourrait pas tenir en entier dans T.
for i in range(len(T) - p + 1):
    # À chaque itération, extrait une sous-chaîne de T commençant à l'indice i et de longueur p.
    # Cette extraction se fait avec la syntaxe de tranchage : T[i:i+p]
    # Compare ensuite la sous-chaîne extraite à la chaîne P avec l'opérateur d'égalité ==.
    if T[i:i+p] == P:
        # Si la condition est vraie, c’est-à-dire si la sous-chaîne trouvée dans T est identique à P,
        # alors affiche la valeur de l’indice i à l’aide de la fonction print().
        print(i)