# Demander à l'utilisateur de saisir un nombre entier, puis stocker cette valeur dans la variable n.
# La fonction input() lit une ligne de texte de l'entrée standard (habituellement le clavier) sous forme de chaîne.
# La fonction int() convertit cette chaîne en un entier.
n = int(input())

# Lire la deuxième ligne de l'entrée utilisateur, sensée contenir des entiers séparés par des espaces.
# La fonction input() lit la ligne complète. La méthode split() découpe la chaîne à chaque espace, produisant une liste de sous-chaînes contenant les valeurs.
# La fonction map() applique la fonction int sur chaque chaîne, la transformant en entier.
# list() convertit l'objet map en une liste contenant les entiers lus. La liste est stockée dans la variable a.
a = list(map(int, input().split()))

# Trier la liste a dans l'ordre croissant à l'aide de la méthode sort(), qui modifie a sur place.
a.sort()

# Trouver le plus grand élément de la liste a grâce à la fonction max().
# Cela donne la valeur maximale présente dans la liste, stockée dans a_max.
a_max = max(a)

# Créer une liste appelée check, de longueur a_max + 1 (ainsi elle va de l'indice 0 à a_max inclus).
# L'opération [0] * (a_max+1) génère une liste contenant uniquement des zéros.
# Chaque indice de check représentera un entier de 0 à a_max, et la valeur stockée représentera un état pour cet entier.
check = [0] * (a_max + 1)

# Parcourir chaque entier de la liste triée a.
for i in a:
    # Vérifier si check[i] est différent de 0, c'est-à-dire si la valeur a déjà été traitée ou marquée.
    # Si check[i] n'est pas 0, une des conditions suivantes s'applique :
    # - check[i] == 1, c'est-à-dire i a déjà été considéré comme "bon"
    # - check[i] == 2, c'est-à-dire i a déjà été marqué comme "composite" ou "mauvais"
    if check[i] != 0:
        # Si check[i] n'est pas 0, marquer check[i] comme 2 (non admissible, par exemple, pas unique premier dans le contexte).
        check[i] = 2
        # Passer au prochain nombre de la liste avec continue, c'est-à-dire ne pas exécuter le reste du bloc pour ce i.
        continue

    # Si check[i] est 0, c'est-à-dire ce nombre n'a pas encore été marqué.
    if check[i] == 0:
        # Marquer check[i] comme 1, signalant que jusqu'à présent i est considéré comme "admissible".
        check[i] = 1

        # Parcourir j de 1 jusqu'à la valeur entière de a_max divisé par i (exclus).
        # Cette boucle sert à marquer tous les multiples de i supérieurs à i comme non admissibles.
        # range(1, a_max // i) donne les valeurs j = 1, 2, ..., jusqu'à ce que (j+1)*i <= a_max
        for j in range(1, a_max // i):
            # Calculer le multiple (j+1)*i de i.
            # Marquer check[(j+1)*i] comme 2, ce qui signale que ce nombre a été engendré par i, donc il n'est pas unique.
            check[(j + 1) * i] = 2

# Compter le nombre d'occurrences de la valeur 1 dans la liste check.
# La méthode count() parcourt toute la liste check et compte le nombre d'éléments égaux à 1.
# Cela donne le résultat final recherché.
print(check.count(1))