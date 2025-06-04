# Demande à l'utilisateur de saisir un nombre entier (le nombre d'éléments de la liste)
N = int(input())  # La fonction input() lit une ligne de texte et int() la convertit en entier

# Demande à l'utilisateur de saisir N entiers séparés par des espaces
# input() lit une chaine, split(' ') découpe la chaine à chaque espace, map(int, ...) convertit chaque élément en entier, et list() fait une liste de ces entiers
H = list(map(int, input().split(' ')))

# Vérifie si la liste contient un seul élément
if N == 1:
    # S'il n'y a qu'un seul élément, on affiche 'Yes' car la séquence respecte forcément la condition imposée
    print('Yes')
else:
    # Cette boucle commence à 1 (deuxième élément) et va jusqu'à N - 1 (dernier élément)
    for i in range(1, N):
        # On regarde si l'élément précédent est STRICTEMENT inférieur à l'élément courant
        if H[i - 1] < H[i]:
            # Si oui, on diminue l'élément courant de 1 pour tenter d'adoucir la pente entre les éléments consécutifs
            H[i] -= 1  # H[i] = H[i] - 1 réduit la valeur de H[i] d'une unité

    # Initialise une variable qui servira de drapeau pour indiquer si la séquence respecte la condition finale
    no_flag = 0  # On commence par supposer qu'il n'y a pas d'anomalie

    # Deuxième boucle pour vérifier si la séquence est non croissante (chaque élément >= suivant)
    for i in range(1, N):
        # Si un élément précédent est supérieur à l'élément courant, la condition n'est pas respectée
        if H[i - 1] > H[i]:
            # On place le drapeau à 1 pour signaler une anomalie
            no_flag = 1

    # Après avoir parcouru la liste, on vérifie la valeur du drapeau
    if no_flag == 0:
        # Si tout va bien, on affiche 'Yes'
        print('Yes')
    else:
        # Sinon, on affiche 'No'
        print('No')

    # Ligne commentée : on pourrait afficher la liste finale H pour vérification supplémentaire
    # print(H)