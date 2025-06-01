import sys  # Importation du module sys qui permet d'accéder à des fonctions et variables utilisées ou maintenues par l'interpréteur Python.

# Lecture d'une ligne de l'entrée standard, segmentation de cette ligne en deux parties avec split(),
# puis conversion de ces deux parties en entiers grâce à map(int, ...),
# enfin assignation des deux entiers obtenus aux variables w (largeur) et h (hauteur).
w, h = map(int, input().split())

# Initialisation des variables sumC et sumR qui serviront à stocker la somme des valeurs des colonnes et des lignes respectivement. Elles commencent à zéro.
sumC = 0
sumR = 0

# Lecture d'une autre ligne de l'entrée standard, cette ligne contient des entiers séparés par des espaces.
# Ces entiers sont convertis en une liste d'entiers grâce à list(map(int, ...)) et assignés à la variable col.
# Cette liste représente les valeurs associées aux colonnes.
col = list(map(int, input().split()))

# Pareil que pour col, mais pour la variable row qui représente les valeurs associées aux lignes.
row = list(map(int, input().split()))

# Boucle for pour parcourir chaque élément c dans la liste col.
# Ici, on ajoute chaque élément c à la variable sumC pour obtenir la somme totale des valeurs des colonnes.
for c in col:
    sumC += c  # Ajout de c à sumC

# Boucle similaire à la précédente, mais pour la liste row.
# Addition de chaque élément r dans row à sumR pour obtenir la somme totale des valeurs des lignes.
for r in row:
    sumR += r  # Ajout de r à sumR

# Condition if pour vérifier si la somme des lignes diffère de la somme des colonnes.
# Le programme suppose que ces deux sommes doivent être identiques pour que la suite fonctionne correctement.
if sumR != sumC:
    # Si la somme des lignes n'est pas égale à la somme des colonnes, on imprime 0 (échec).
    print(0)
    # Puis on quitte le programme immédiatement avec sys.exit(0),
    # ce qui signifie que le programme se termine sans erreur mais sans exécuter la suite.
    sys.exit(0)

# Boucle for qui itère sur la variable i allant de 0 jusqu'à w-1 (exclu), parcourant ainsi tous les indices des colonnes.
for i in range(w):
    # On trie la liste row en ordre décroissant avec sort(reverse=True).
    # Cela réarrange les valeurs de row pour que les plus grandes soient en premier.
    # Ce tri est fait à chaque itération de la boucle sur i.
    row.sort(reverse=True)
    # Boucle imbriquée pour parcourir j de 0 à h-1 (tous les indices des lignes).
    for j in range(h):
        # Condition pour arrêter la boucle si la valeur col[i] est zéro ou si la valeur row[j] est zéro.
        # Le mot-clé not est utilisé pour tester la "valeur de vérité" (False si la valeur est zéro).
        if not col[i] or not row[j]:
            break  # Si l'une des deux valeurs est zéro, on sort de la boucle interne.

        # Si aucune des valeurs ci-dessus n'est nulle, on décrémente row[j] de 1.
        # Cela signifie qu'on utilise une unité de la ligne j.
        row[j] -= 1

        # On décrémente également col[i] de 1, consommant une unité de la colonne i.
        col[i] -= 1

    # Après la boucle interne, on vérifie si col[i] est toujours supérieur à 0.
    # Cela signifie que la colonne i n'a pas été totalement couverte par la soustraction précédente.
    if col[i] > 0:
        # Si oui, on imprime 0 (indiquant un échec) et on quitte le programme immédiatement.
        print(0)
        sys.exit(0)

# Si toutes les colonnes ont été complètement traitées avec succès,
# on imprime 1 pour indiquer que la condition est remplie correctement.
print(1)