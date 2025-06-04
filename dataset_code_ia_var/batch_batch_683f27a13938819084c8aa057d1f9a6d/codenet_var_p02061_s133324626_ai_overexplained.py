import math  # Importe le module math, nécessaire pour utiliser la fonction sqrt (racine carrée).

# Définition d'une fonction pour générer les nombres premiers jusqu'à n via le crible d'Ératosthène.
def get_sieve_of_eratosthenes(n):
    # Vérification que l'argument n est bien de type int (entier).
    if not isinstance(n, int):
        raise TypeError('n is int type.')  # Si ce n'est pas un entier, une erreur est levée.
    
    # Vérification que n soit supérieur ou égal à 2, car il n'y a pas de nombre premier en dessous de 2.
    if n < 2:
        raise ValueError('n is more than 2')  # Soulève une erreur si n est inférieur à 2.
    
    prime = []  # Initialise une liste vide qui contiendra les nombres premiers trouvés.
    # Calcule la racine carrée de n pour optimiser le crible (il suffit de criber jusqu'à sqrt(n)).
    limit = math.sqrt(n)
    # Crée une liste contenant les entiers de 2 à n (puisque range(1, n) donne 1 à n-1, on ajoute 1).
    data = [i + 1 for i in range(1, n)]
    # Boucle principale : on itère jusqu'à ce qu'il n'y ait plus de "petit" nombre premier dans data.
    while True:
        p = data[0]  # Prend le premier élément de data comme prochain nombre premier.
        if limit <= p:
            # Si p dépasse la limite, tous les nombres restants de data sont premiers, on retourne le résultat.
            return prime + data
        prime.append(p)  # Ajoute le nombre premier actuel à la liste prime.
        # On filtre data pour enlever tous les multiples de p (autres que p lui-même).
        data = [e for e in data if e % p != 0]

# Attend la saisie d'un entier n via l'utilisateur (nombre de requêtes pour lesquelles donner un résultat).
n = int(input())  # Convertit l'entrée standard (par défaut une chaîne de caractères) en entier.

# Calcule la racine carrée entière de 100 000 pour déterminer jusqu'où nous avons besoin des nombres premiers.
ma = int(math.sqrt(10**5))
# Génére la liste de tous les nombres premiers jusqu'à ma via notre fonction précédente.
lis = get_sieve_of_eratosthenes(ma)
# Crée une liste l_b de booléens de taille 100 001 (indices de 0 à 100 000), initialisée à False.
l_b = [False]*(10**5+1)

# Deux boucles imbriquées pour générer des produits spécifiques de deux nombres premiers.
for item1 in lis:  # Parcourt chaque nombre premier dans la liste lis avec la variable item1.
    for item2 in lis:  # Parcourt chaque nombre premier encore avec la variable item2.
        # Si item2 (deuxième facteur premier) est inférieur à item1, on saute cette itération.
        if item2 < item1:
            continue
        # Si le produit item1 * item2 * 3 dépasse 100 000, pas la peine d'aller plus loin, on quitte la boucle interne.
        if item1*item2*3 > 10**5:
            break
        # Initialise un compteur i à 0 pour multiplier de façon incrémentale.
        i = 0
        # Boucle tant que le produit item1*item2*(3+i) reste dans la limite de 100 000.
        while(item1*item2*(3+i) <= 10**5):
            # Marque dans l_b à l'indice du résultat du produit comme True.
            l_b[item1*item2*(3+i)] = True
            i += 1  # Incrémente i pour vérifier la valeur suivante.

# Pour chaque nombre premier de lis, désactive (remet à False) le booléen correspondant à son cube s’il est dans la plage.
for item in lis:
    if item**3 < 10**5:
        l_b[item**3] = False  # On s'assure que les cubes d'un nombre premier ne sont pas comptés.

# Créée une liste l_count qui va contenir les cumuls des True dans l_b jusqu'à chaque indice, initialisée à 0.
l_count = [0]*(10**5+1)

# On construit le tableau cumulatif : pour chaque i de 1 à 100 000 inclus
for i in range(1,10**5+1):
    if l_b[i]:
        # Si l_b[i] est True, alors on ajoute 1 au cumul précédent pour obtenir le cumul courant.
        l_count[i] = l_count[i-1] + 1
    else:
        # Sinon, le cumul reste identique à celui de l'indice précédent.
        l_count[i] = l_count[i-1]

# Boucle sur n requêtes (nombre saisi précédemment)
for _ in range(n):
    num = int(input())  # Attend l'entrée de l'utilisateur pour le paramètre de requête courant.
    print(l_count[num])  # Affiche le nombre total de valeurs marquées True dans l_b jusqu'à num inclus.