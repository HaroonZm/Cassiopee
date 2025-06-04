# Demande à l'utilisateur de saisir une valeur, qui est convertie en entier et stockée dans la variable n.
n = int(input())

# Demande à l'utilisateur de saisir une série de nombres séparés par des espaces.
# Chaque nombre saisi sous forme de chaîne de caractères est converti en entier.
# Une liste composée de ces entiers est alors créée et assignée à la variable 'a'.
a = [int(i) for i in input().split()]

# Définition de la fonction f, qui prend un paramètre x.
def f(x):
    # Initialisation d'un compteur ou accumulateur k à 0.
    k = 0
    # Parcours de chaque élément i présent dans la liste a.
    for i in a:
        # Pour chaque élément i, réalise le calcul : (i + x - n) // (n + 1).
        # L'opérateur // effectue une division entière, c'est-à-dire qu'il donne le quotient sans la partie décimale.
        # Ensuite, ajoute 1 au résultat.
        # Le résultat total est ajouté à la variable k.
        k += (i + x - n) // (n + 1) + 1
    # La fonction retourne un booléen indiquant si k est inférieur ou égal à x.
    # Si c'est le cas, retourne True, sinon retourne False.
    return k <= x

# Boucle for qui servira à tester différentes valeurs de i afin de trouver la plus petite satisfaisant la condition f(i).
# La boucle commence à max(0, sum(a) - n * (n - 1)). 'sum(a)' calcule la somme de tous les éléments de la liste a.
# 'n * (n - 1)' multiplie n par n-1. On soustrait ce produit à la somme des éléments et on prend le maximum entre ce résultat et 0.
# Ceci garantit que la boucle ne part jamais d'une valeur négative.
# La boucle va jusqu'à 51 * (10 ** 16), un nombre très grand fixé arbitrairement pour assurer un nombre suffisant d'itérations.
for i in range(max(0, sum(a) - n * (n - 1)), 51 * (10 ** 16)):
    # Pour chaque valeur de i, appelle la fonction f en passant i en argument.
    # Si f(i) retourne True (c'est-à-dire que la condition est satisfaite), on quitte la boucle avec break.
    if f(i):
        break

# Une fois que la boucle for est terminée (soit par break, soit terminaison normale),
# la valeur actuelle de i est affichée à l'aide de la fonction print.
print(i)