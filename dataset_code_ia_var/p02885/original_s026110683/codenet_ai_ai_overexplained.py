# Demande à l'utilisateur de saisir une ligne de texte. 
# La méthode input() lit cette ligne sous forme de chaîne de caractères (string).
# L'utilisateur est censé entrer deux nombres entiers séparés par un espace, par exemple : "5 3"
ligne = input()

# La méthode split() sépare la chaîne 'ligne' en une liste de sous-chaînes, en utilisant l'espace comme séparateur par défaut.
# Si 'ligne' vaut "5 3", alors ligne.split() renverra la liste ["5", "3"]
liste_de_strings = ligne.split()

# La fonction map applique une fonction à chaque élément d'un itérable.
# Ici, int est appliqué à chaque élément de liste_de_strings, ce qui permet de convertir chaque string en entier.
# map(int, liste_de_strings) produit donc un itérable sur les valeurs entières correspondantes, par exemple 5, 3
liste_d_entiers = map(int, liste_de_strings)

# L'affectation multiple permet de stocker ces deux valeurs entières dans les variables A et B.
# Par exemple, si liste_d_entiers contient 5 et 3, alors A=5 et B=3
A, B = liste_d_entiers

# Calcul de la valeur de l'expression (A - 2*B)
# B est multiplié par 2 d'abord. Cette opération se fait avant la soustraction à cause des règles de priorité des opérateurs.
# Cette quantité est ensuite soustraite à A.
sous_resultat = A - 2 * B

# La fonction max() renvoie le plus grand des deux arguments.
# Ceci garantit que le résultat final ne sera pas inférieur à zéro.
# Si sous_resultat vaut -1, max(0, -1) sera 0 ; si sous_resultat vaut 4, max(0, 4) sera 4.
resultat_final = max(0, sous_resultat)

# La fonction print affiche le résultat final à l'écran pour l'utilisateur.
print(resultat_final)