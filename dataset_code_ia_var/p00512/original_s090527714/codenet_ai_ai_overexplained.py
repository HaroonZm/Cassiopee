# Création d'un dictionnaire vide nommé d, qui va servir à stocker des paires clé-valeur.
d = {}

# Demande à l'utilisateur de saisir un entier, convertit l'entrée texte en entier avec int(),
# puis la multiplie avec la liste [0], ce qui crée une liste remplie de zéros ayant pour longueur la valeur entrée.
# Par exemple, si l'utilisateur tape 3, [0]*3 donne [0,0,0].
for _ in [0] * int(input()):
    # Pour chaque itération de la boucle (autant de fois qu'indiqué par l'utilisateur) :
    # Saisie d'une ligne contenant deux éléments séparés par un espace (par exemple "A 5").
    # La méthode input() lit une ligne au clavier. La méthode split() coupe la chaîne selon les espaces et retourne une liste.
    # On assigne le premier élément à k (clé), le second à v (valeur).
    k, v = input().split()
    # On met à jour le dictionnaire :
    # d.get(k,0) : si la clé k existe déjà dans d, récupère sa valeur actuelle, sinon 0.
    # int(v) : convertit v (qui est une chaîne) en entier.
    # On additionne les deux et on assigne le résultat comme nouvelle valeur de la clé k dans d.
    d[k] = d.get(k, 0) + int(v)

# On veut maintenant afficher le contenu du dictionnaire d, trié selon un ordre particulier sur les clés.

# On va utiliser la fonction sorted() pour trier les éléments selon une clé de tri personnalisée.
# Parcours de chaque clé k dans le dictionnaire d, triées avec une clé de tri spéciale.
for k in sorted(
    d,  # On trie les clés du dictionnaire d.
    key=lambda x: (
        # La clé de tri est un tuple. Elle comporte deux éléments pour chaque clé x :
        # Premier élément du tuple :
        #   Pour chaque position i (indice retourné par enumerate())
        #   et chaque caractère k dans la clé x parcourue en sens inverse (x[::-1]),
        #   calcule : 27 puissance i, multiplié par la valeur numérique de la lettre (ord(k) - 64).
        #   ord(k) donne le code ASCII du caractère k.
        #   Pour 'A', ord('A') == 65, donc ord(k)-64 est 1 ; pour 'B', c'est 2, etc.
        #   sum(...) fait la somme de tous ces produits.
        sum(27 ** i * (ord(char) - 64) for i, char in enumerate(x[::-1])),
        # Deuxième élément du tuple (pour éviter les égalités) : la clé elle-même (x).
        x
    )
):
    # Pour chaque clé k triée selon la règle ci-dessus,
    # affiche la clé suivie d'un espace puis sa valeur correspondante dans d.
    print(k, d[k])