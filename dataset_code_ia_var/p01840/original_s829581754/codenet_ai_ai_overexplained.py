# Demande une saisie utilisateur, récupère une ligne, la découpe en parties sur les espaces, puis convertit chaque élément en entier grâce à la fonction map(int, ...), puis transforme le résultat (un itérable) en liste et stocke le tout dans la variable 'a'
a = list(map(int, input().split()))

# Demande une seconde saisie utilisateur de la même manière, récupère une autre série d'entiers et la stocke dans la liste 'b'
b = list(map(int, input().split()))

# Crée une liste 'k' de longueur égale à la 3ème valeur de la liste 'a' (à l’index 2)
# Tous les éléments de cette liste sont initialisés à zéro. Cette liste va servir à compter des occurrences selon certains critères plus loin dans le code.
k = [0] * a[2]

# Initialise la variable 'pp' à zéro. Cependant, cette variable ne sera pas utilisée ailleurs dans le code.
pp = 0

# Initialise la variable 'su' à zéro. Elle va servir à compter un certain nombre d'éléments selon un critère défini plus loin.
su = 0

# Parcours chaque élément 'i' de la liste 'b' grâce à une boucle for
for i in b:
    # Pour chaque élément de 'b', exécute une boucle interne sur tous les indices 'j' dans l’intervalle allant de 0 à a[2]-1 (car range(a[2]) s'arrête avant a[2])
    for j in range(a[2]):
        # Vérifie si l'indice 'j' est compris entre (i - a[1]) et (i + a[1] - 1), autrement dit dans un intervalle centré sur la valeur 'i'
        if j >= i - a[1] and j <= i + a[1] - 1:
            # Si la condition est remplie, alors incrémente la valeur de 'k' à l'indice correspondant de 1
            k[j] += 1

# Parcours chaque indice 'i' de la liste 'k' (qui contient a[2] éléments)
for i in range(a[2]):
    # Si la valeur de k[i] est exactement égale à 0, c’est-à-dire si aucun des intervalles précédents n’a touché cet indice 'i'
    if k[i] == 0:
        # Augmente su de 1 pour comptabiliser cet indice comme "non couvert"
        su += 1

# Affiche à l’écran la valeur totale de 'su', qui correspond au nombre d’indices dans 'k' qui sont restés à zéro après tous les marquages
print(su)