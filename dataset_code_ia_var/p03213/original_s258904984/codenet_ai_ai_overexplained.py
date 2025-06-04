# Demander à l'utilisateur de saisir un entier, qui sera stocké dans la variable N.
# On convertit l'entrée utilisateur (qui est une chaîne de caractères) en entier grâce à int().
N = int(input())

# Crée une liste initiale de nombres premiers : 2, 3, 5, et 7.
# Les nombres premiers sont des nombres qui n'ont que deux diviseurs distincts, 1 et eux-mêmes.
prime_number = [2, 3, 5, 7]

# La variable 'prim' est ici une copie initiale de prime_number.
# Cette liste va servir plus bas pour tester la primalité de nouveaux nombres.
prim = [2, 3, 5, 7]

# --- Génération de la liste des nombres premiers entre 2 et 100 inclus ---

# Pour chaque nombre i allant de 2 jusqu'à 100 inclus (la borne supérieure de range est exclusive, donc on met 101).
for i in range(2, 101):

    # On commence en supposant que i est premier (prime_flag placé à True au début de chaque itération).
    prime_flag = True

    # On teste la divisibilité de i par tous les nombres premiers déjà trouvés (qui sont dans la liste prim).
    # Cela correspond au "crible d'Ératosthène" pour trouver les nombres premiers efficacement.
    for j in prim:

        # Si i est divisible par j, alors i n'est pas un nombre premier (car il existe un diviseur autre que 1 et lui-même).
        if i % j == 0:
            # On marque que i n'est pas un nombre premier.
            prime_flag = False
            # On sort de la boucle interne puisque l'on a déjà trouvé que i n'est pas premier.
            break

    # Si prime_flag est encore à True après toutes les vérifications, cela signifie que i n'est pas divisible par aucun nombre premier plus petit,
    # donc i est effectivement un nombre premier.
    if prime_flag:
        # On ajoute i à la liste des nombres premiers trouvés.
        prime_number.append(i)

# --- Compte des facteurs premiers dans la décomposition en facteurs premiers de tous les entiers de 2 à N ---

# On initialise une liste de compteurs, un pour chaque nombre premier identifié jusqu'à présent.
# Chacun est mis à zéro au départ.
prime_factor = [0] * len(prime_number)

# Pour chaque entier i de 2 à N inclus (N étant fourni par l'utilisateur),
for i in range(2, N + 1):

    # On crée une variable temporaire 'tmp' qui va permettre de faire la division sans modifier i.
    tmp = i

    # Pour chaque indice j correspondant à un nombre premier dans la liste prime_number,
    for j in range(len(prime_number)):

        # On va compter combien de fois le nombre premier prime_number[j] divise tmp de façon successive.
        # Cela correspond à son exposant dans la décomposition en facteurs premiers de i.
        while tmp % prime_number[j] == 0:
            # On ajoute 1 au compteur du nombre premier correspondant.
            prime_factor[j] += 1
            # On divise tmp par ce nombre premier pour enlever cette puissance.
            tmp //= prime_number[j]

# --- Comptage du nombre de facteurs premiers ayant des exposants d'au moins certaines valeurs ---

# On initialise à zéro les compteurs correspondants aux divers paliers d'exposant des facteurs premiers.
count2 = 0    # Compte le nombre de facteurs premiers avec un exposant d'au moins 2.
count4 = 0    # Même chose pour au moins 4.
count14 = 0   # Pour au moins 14.
count24 = 0   # Pour au moins 24.
count74 = 0   # Pour au moins 74.

# On parcourt la liste des quantités de chaque nombre premier dans la factorisation de N! (factorielle de N).
for i in prime_factor:
    # Si le nombre premier apparaît au moins 2 fois (exposant >= 2), incrémenter count2.
    if i >= 2:
        count2 += 1
    # Si l'exposant est au moins 4, incrémenter count4.
    if i >= 4:
        count4 += 1
    # Pour au moins 14, incrémenter count14.
    if i >= 14:
        count14 += 1
    # Pour au moins 24, incrémenter count24.
    if i >= 24:
        count24 += 1
    # Pour au moins 74, incrémenter count74.
    if i >= 74:
        count74 += 1

# --- Calcul du nombre de combinaisons de deux facteurs premiers distincts ayant un exposant d'au moins 4 chacun ---

# Si le nombre de facteurs premiers avec au moins 4 occurrences est au moins 2,
# alors il existe count4 * (count4 - 1) / 2 paires distinctes (combinaison sans répétition de 2 parmi count4 éléments).
if count4 >= 2:
    # Calcul du nombre de combinaisons possibles de 2 parmi count4.
    combination4 = count4 * (count4 - 1) // 2  # // signifie division entière.
else:
    # S'il n'y a pas assez de facteurs avec exposant >= 4, alors aucune combinaison possible.
    combination4 = 0

# --- Calcul du nombre total de façons de composer un nombre ayant exactement 75 diviseurs ---

# Le nombre de diviseurs d'un nombre N est donné par le produit (e1+1)*(e2+1)*...*(en+1), où ei sont les exposants de chaque facteur premier.
# Pour obtenir un nombre ayant exactement 75 diviseurs, il y a différentes combinaisons possibles d'exposants :

# Par exemple, 75 = 75
# 75 = 3 * 25
# 75 = 5 * 15
# 75 = 25 * 3
# 75 = 5 * 5 * 3

# On réalise ci-dessous la somme de toutes les manières d'obtenir 75 diviseurs par configuration adaptée.

# combination4 * (count2 - 2) :
#   Cas où on prend deux facteurs premiers avec au moins 4 occurrences (count4),
#   et un troisième (différent) qui a au moins 2 occurrences (count2).
#   On enlève 2 du total car les deux déjà pris pour les facteurs d'exposant 4 ne peuvent pas être repris.

# count14 * (count4 - 1) :
#   Cas où un facteur premier a au moins 14 occurrences, et un autre a au moins 4 occurrences.
#   (On enlève 1 au deuxième car il ne doit pas être le même que le premier.)

# count24 * (count2 - 1) :
#   Cas où un facteur premier a au moins 24 occurrences, et un autre a au moins 2 occurrences.
#   (On enlève 1 pour ne pas choisir le même facteur premier deux fois.)

# count74 :
#   Cas où un facteur premier a au moins 74 occurrences. Il suffit à lui-seul pour obtenir 75 diviseurs.

ans = combination4 * (count2 - 2) + count14 * (count4 - 1) + count24 * (count2 - 1) + count74

# Finalement, on affiche le résultat total à l'utilisateur.
print(ans)