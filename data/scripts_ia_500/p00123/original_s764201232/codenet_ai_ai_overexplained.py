import sys  # Importe le module 'sys' qui fournit l'accès aux variables utilisées ou maintenues par l'interpréteur Python, notamment sys.stdin, qui est un objet de type fichier représentant l'entrée standard.

# Définition d'une liste nommée R contenant des chaînes de caractères représentant des catégories ou niveau de classification.
# Chaque élément est une chaîne de caractères correspondant à un niveau, avec "AAA" comme le meilleur niveau et "NA" représentant une absence ou non applicable.
R = ["AAA","AA","A","B","C","D","E","NA"]

# Boucle for qui itère sur chaque ligne d'entrée lue à partir de sys.stdin (l'entrée standard).
# Chaque variable 'i' correspond à une ligne de texte reçue, typiquement une chaîne de caractères se terminant par un saut de ligne '\n'.
for i in sys.stdin:
    # Pour chaque ligne 'i', on procède à décomposer (split) cette ligne en sous-chaînes en se servant de l'espace comme séparateur par défaut,
    # On obtient ainsi une liste de chaînes de caractères qui sont supposées représenter des nombres.
    # La fonction 'map' est utilisée pour appliquer la fonction float à chaque élément de cette liste, transformant ainsi les chaînes de caractères en nombres à virgule flottante.
    # On récupère ensuite les deux premiers éléments obtenus après la transformation pour les stocker dans les variables t1 et t2 respectivement.
    t1,t2 = map(float,i.split())

    # Initialisation des variables t5 et t10 à 0 ; celles-ci vont servir à enregistrer des indices correspondant aux niveaux déterminés par des seuils sur t1 et t2.
    t5 = t10 = 0

    # Bloc conditionnel if-elif-else qui détermine la valeur de t5 selon la valeur de t1.
    # Il s'agit d'attribuer un indice en fonction de la plage dans laquelle t1 tombe.
    # Chaque condition précise une borne supérieure exclusive. Si t1 est inférieur à cette borne, alors t5 prend une certaine valeur.
    if   t1 < 35.5: t5 = 0            # Si t1 < 35.5, t5 vaut 0
    elif t1 < 37.5: t5 = 1            # Si t1 >= 35.5 et t1 < 37.5, t5 vaut 1
    elif t1 < 40  : t5 = 2            # Si t1 >= 37.5 et t1 < 40, t5 vaut 2
    elif t1 < 43  : t5 = 3            # Si t1 >= 40 et t1 < 43, t5 vaut 3
    elif t1 < 50  : t5 = 4            # Si t1 >= 43 et t1 < 50, t5 vaut 4
    elif t1 < 55  : t5 = 5            # Si t1 >= 50 et t1 < 55, t5 vaut 5
    elif t1 < 70  : t5 = 6            # Si t1 >= 55 et t1 < 70, t5 vaut 6
    else          : t5 = 7            # Sinon (t1 >= 70), t5 vaut 7

    # Bloc conditionnel similaire à celui ci-dessus, mais cette fois pour déterminer la valeur de t10 en fonction de la valeur de t2.
    # On compare t2 à différentes bornes supérieures strictes et on assigne à t10 un index correspondant.
    if   t2 < 71  : t10 = 0           # Si t2 < 71, t10 vaut 0
    elif t2 < 77  : t10 = 1           # Si t2 >= 71 et t2 < 77, t10 vaut 1
    elif t2 < 83  : t10 = 2           # Si t2 >= 77 et t2 < 83, t10 vaut 2
    elif t2 < 89  : t10 = 3           # Si t2 >= 83 et t2 < 89, t10 vaut 3
    elif t2 < 105 : t10 = 4           # Si t2 >= 89 et t2 < 105, t10 vaut 4
    elif t2 < 116 : t10 = 5           # Si t2 >= 105 et t2 < 116, t10 vaut 5
    elif t2 < 148 : t10 = 6           # Si t2 >= 116 et t2 < 148, t10 vaut 6
    else          : t10 = 7           # Sinon (t2 >= 148), t10 vaut 7

    # La variable t est assignée à la valeur maximale entre t5 et t10.
    # Ceci permet de choisir l'indice le plus élevé entre les deux indices obtenus, ce qui correspond à la catégorie la plus sévère ou la plus basse en qualité selon l'échelle définie dans la liste R.
    t = max(t5,t10)

    # Affichage (print) de l'élément de la liste R situé à l'index t.
    # Cela affiche la classification finale correspondante aux mesures t1 et t2 traitées.
    print(R[t])