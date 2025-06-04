# Demander à l'utilisateur de saisir le premier entier
# input() lit une chaîne depuis l'utilisateur, int() convertit cette chaîne en entier
a = int(input())

# Même démarche pour le second entier
b = int(input())

# Même démarche pour le troisième entier
c = int(input())

# Même démarche pour le quatrième entier
d = int(input())

# Même démarche pour le cinquième entier
e = int(input())

# Créer une liste appelée input_list contenant les cinq entiers ci-dessus, dans l'ordre de saisie
input_list = [a, b, c, d, e]

# Créer une liste vide qui servira à stocker chaque nombre après qu'il ait été arrondi au multiple supérieur de 10
# (sauf s'il est déjà multiple de 10, auquel cas il reste identique)
ten_up_list = []

# Créer une liste vide qui servira à stocker le reste de la division par 10 (appelé 'amari' en japonais) seulement pour les nombres non multiples de 10
amari_list = []

# Initialiser une variable total à 0; elle servira à additionner les valeurs après arrondi
total = 0

# Boucle sur tous les nombres de input_list pour appliquer le traitement
for i in input_list:
    # Calculer le reste de la division du nombre par 10
    # Ceci donne la partie "unité" du nombre (ex: 23 % 10 == 3)
    amari = i % 10
    # Si ce reste est égal à 0, cela signifie que le nombre est déjà un multiple de 10
    if amari == 0:
        # Dans ce cas, ajouter le nombre lui-même (sans modification) à ten_up_list
        ten_up_list.append(i)
    else:
        # Sinon, le nombre n'est pas un multiple de 10
        # Calculer combien il manque pour atteindre le multiple de 10 supérieur le plus proche
        # Ceci revient à faire (10 - amari), puis on ajoute ce montant au nombre original
        ten_up_list.append(i + 10 - amari)
        # Également, enregistrer ce reste dans amari_list pour un usage ultérieur d'optimisation
        amari_list.append(amari)

# Après la boucle, on a une liste ten_up_list où chaque nombre a été arrondi au multiple de 10 supérieur

# Ajouter toutes les valeurs de ten_up_list pour obtenir le total
for i in ten_up_list:
    # Ajouter la valeur courante de i à la variable total
    total += i

# Ensuite, il y a une optimisation : on réduit le gaspillage causé par l’arrondi
# Plus précisément, on souhaite soustraire le "surplus" minimal
# Cela est seulement nécessaire si il y avait au moins un nombre qui n'était pas un multiple de 10, donc amari_list n'est pas vide
if len(amari_list) != 0:
    # Trier amari_list pour mettre le plus petit reste en premier (ordre croissant)
    amari_list.sort()
    # Retirer 10 du total, car lorsqu'on arrondissait tous les nombres vers le haut,
    # pour chaque nombre non multiple de 10, on ajoutait "jusqu'à +9" en trop
    # On peut compenser ce "gaspillage" pour un nombre, celui dont le reste était le plus faible
    # On ajoute son reste au total pour rétablir la différence
    total = total - 10 + amari_list[0]

# Afficher le résultat final à l'écran avec la fonction print
print(total)