# Demande à l'utilisateur d'entrer une chaîne de caractères via le clavier.
# Cette chaîne doit contenir deux chiffres séparés par un espace.
ab = input()

# La méthode split() divise la chaîne 'ab' en une liste de sous-chaînes,
# en utilisant l'espace " " comme séparateur. Par exemple, si l'utilisateur saisit "3 5",
# ab.split(" ") retournera ["3", "5"].
a, b = ab.split(" ")

# La fonction int() convertit la chaîne 'a' en un entier.
# Par exemple, si a == "3", alors int(a) == 3.
A = int(a)

# De même, la fonction int() convertit la chaîne 'b' en un entier.
B = int(b)

# Ici, nous vérifions plusieurs conditions en même temps à l'aide du mot-clé 'or', 
# qui est l'opérateur logique OU en Python.
# "0" in a : Vérifie si le caractère '0' est présent dans la chaîne 'a'
# "0" in b : Vérifie si le caractère '0' est présent dans la chaîne 'b'
# A > 9 : Vérifie si la valeur entière contenue dans A est supérieure à 9
# B > 9 : Vérifie si la valeur entière contenue dans B est supérieure à 9
#
# Si au moins une de ces conditions est vraie, on entre dans le bloc if.
if "0" in a or "0" in b or A > 9 or B > 9:
    # Affiche -1 à l'écran pour indiquer une erreur ou des entrées invalides
    print(-1)
else:
    # Cette partie de code n'est exécutée que si toutes les conditions ci-dessus sont fausses,
    # c'est-à-dire si ni 'a' ni 'b' ne contiennent le chiffre '0', et si A et B sont tous les deux inférieurs ou égaux à 9.
    #
    # On affiche le produit de A et B, c'est-à-dire le résultat de leur multiplication.
    print(A * B)