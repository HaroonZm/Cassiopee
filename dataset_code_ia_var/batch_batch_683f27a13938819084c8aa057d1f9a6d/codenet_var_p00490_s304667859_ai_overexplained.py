# Demander à l'utilisateur d'entrer un nombre entier représentant le nombre de garnitures possibles
# raw_input() lit une ligne saisie à partir de l'entrée standard (utilisateur)
# int() convertit la chaîne de caractères donnée en entier
n = int(raw_input())

# Demander à l'utilisateur d'entrer deux valeurs séparées par un espace (le prix de base et le coût par garniture)
# raw_input() lit la ligne
# split(" ") sépare la ligne en plusieurs sous-chaînes en utilisant un espace comme délimiteur
# map(float, ...) convertit chaque sous-chaîne en un nombre à virgule flottante (float),
#   car les prix peuvent contenir des décimales
# Le résultat est stocké dans deux variables a (prix de base) et b (coût pour chaque garniture)
a, b = map(float, raw_input().split(" "))

# Demander à l'utilisateur d'entrer la quantité de calories de la pizza de base
# raw_input() lit la ligne entrée, float() convertit en nombre à virgule flottante
c = float(raw_input())

# Initialiser une liste vide pour contenir les calories de chaque garniture possible
toppings = []

# Boucle qui s'exécute n fois (pour chaque garniture)
for i in range(n):
    # Pour chaque itération, demander à l'utilisateur la quantité de calories pour la garniture
    # float(raw_input()) lit l'entrée, la convertit en nombre à virgule flottante
    topping = float(raw_input())
    # On ajoute la valeur à la liste toppings grâce à la méthode append()
    toppings.append(topping)

# Trier la liste des calories de garnitures dans l'ordre décroissant (de la plus calorique à la moins calorique)
# sort() permet de trier une liste, cmp permet de fournir une fonction de comparaison personnalisée
# cmp lambda renvoie -1 si le second élément est supérieur au premier, 1 si inférieur, et 0 si égal (tri décroissant)
toppings.sort(cmp=(lambda x, y: cmp(y, x)))

# Initialiser la somme totale des calories avec celles de la pizza de base
cal_sum = c

# Initialiser la somme totale du coût avec le prix de base de la pizza
doll_sum = a

# Boucle qui parcourt chacune des garnitures dans la liste
for i in range(n):
    # Calculer la densité calorique actuelle = calories totales / coût total
    # Calculer la densité calorique potentielle si on ajoute la garniture courante
    # On compare ces deux ratios :
    #   si le ratio augmente en ajoutant la garniture, alors on ajoute vraiment la garniture à la pizza
    if cal_sum/doll_sum < (cal_sum + toppings[i])/(doll_sum + b):
        # Ajouter les calories de la garniture à la somme totale de calories
        cal_sum += toppings[i]
        # Ajouter le coût de la garniture au coût total
        doll_sum += b
    else:
        # Si l'ajout de la garniture ne permet pas d'augmenter le ratio calories/prix, on arrête la boucle
        break

# Afficher la valeur entière de la densité calorique finale (donc tronquer la partie décimale)
# int() convertit le résultat en entier
print int(cal_sum / doll_sum)