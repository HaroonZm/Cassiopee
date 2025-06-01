# Initialisation d'une liste appelée 'a' contenant quatre éléments, chacun initialisé à 0.
# Cette liste servira à compter le nombre d'occurrences de chaque groupe sanguin dans la liste 'aa'.
a = [0, 0, 0, 0]

# Initialisation d'une liste appelée 'aa' contenant quatre chaînes de caractères représentant des groupes sanguins.
# Ces chaînes correspondent aux groupes sanguins possibles que nous allons rencontrer dans les entrées utilisateur.
aa = ["A", "B", "AB", "O"]

# Création d'une boucle infinie while True, qui s'exécutera indéfiniment jusqu'à ce qu'une interruption explicite survienne.
while True:
    try:
        # Lecture d'une ligne de texte saisie par l'utilisateur, stockée dans la variable 's'.
        # La fonction input() attend que l'utilisateur entre une chaîne de caractères puis appuie sur Entrée.
        s = input()
    except:
        # Si une exception survient lors de la lecture (par exemple fin de fichier/end of input),
        # alors on interrompt la boucle avec un break.
        break

    # La chaîne 's' est supposée contenir deux parties séparées par une virgule.
    # La méthode split(",") découpe la chaîne 's' en une liste de sous-chaînes, utilisées ici pour stocker dans 'b' et 'c'.
    # 'b' va contenir la première partie avant la virgule, et 'c' la deuxième partie après la virgule.
    b, c = s.split(",")

    # La méthode index() recherchera la position de la chaîne 'c' dans la liste 'aa'.
    # Puis, on utilise cet indice pour accéder à l'élément correspondant dans la liste 'a'.
    # Ensuite, on incrémente la valeur de cet élément de 1, comptabilisant ainsi une occurrence de ce groupe sanguin.
    a[aa.index(c)] += 1

# Après la sortie de la boucle, c'est-à-dire quand plus aucune entrée utilisateur n'est disponible,
# on utilise une boucle for pour parcourir les indices de 0 à 3 (car 4 éléments).
for i in range(4):
    # Pour chaque indice i, on affiche la valeur entière contenue dans la liste 'a' à cet indice.
    # Cela correspond au nombre total d'occurrences rencontrées pour le groupe sanguin correspondant.
    print(a[i])