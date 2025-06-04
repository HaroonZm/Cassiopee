# Demande à l'utilisateur de saisir une valeur entière qui sera assignée à la variable N.
N = int(input())

# Crée une liste de zéros de taille N+1.
# Cette liste servira à compter combien de fois chaque nombre de 2 à N apparaît comme facteur premier.
y = [0]*(N+1)

# Cette boucle va de 1 à N inclus, c'est-à-dire qu'elle examine chaque entier de 1 à N.
for i in range(1, N+1):
    # Copie la valeur de i dans une variable temporaire M.
    M = i
    # Cette boucle va continuer tant que M est strictement supérieur à 1.
    # Elle sert à décomposer M en facteurs premiers.
    while M > 1:
        # Parcourt tous les entiers j de 2 jusqu'à M inclus pour trouver un diviseur de M.
        for j in range(2, M+1):
            # Vérifie si j est un diviseur de M en testant si le reste de la division de M par j est égal à 0.
            if M % j == 0:
                # Si c'est le cas, divise M par ce diviseur pour retirer ce facteur premier de M.
                M = M // j
                # Augmente de 1 la case y[j], ce qui veut dire qu'on a trouvé un nouveau facteur premier j.
                y[j] += 1
                # Utilise break pour sortir de la boucle interne afin de recommencer la recherche sur le nouveau M.
                break

# Initialise la variable ans à 1. Cette variable contiendra le résultat final.
ans = 1

# Pour chaque élément i de la liste y, effectue la multiplication suivante.
# On ajoute 1 à chaque i car la formule utilise (exposant + 1) pour chaque facteur premier.
for i in y:
    # Multiplie ans par (i + 1), puis prend le reste de la division par 10**9 + 7
    # Cela permet d'éviter que ans devienne trop grand (gestion du dépassement de capacité).
    ans = (ans * (i + 1)) % (10**9 + 7)

# Affiche le résultat final, qui correspond au nombre de diviseurs du produit de tous les entiers de 1 à N.
print(ans)