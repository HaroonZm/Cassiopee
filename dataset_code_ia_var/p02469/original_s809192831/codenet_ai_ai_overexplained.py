import fractions  # Importe le module 'fractions' qui fournit des outils pour manipuler des fractions et des opérations liées au PGCD (plus grand commun diviseur)

n = int(input())  # Demande à l'utilisateur de saisir un nombre entier, qui sera converti en entier et stocké dans la variable 'n'.
# 'n' représente le nombre d'éléments que l'utilisateur souhaite traiter dans la suite du code.

l = list(map(int, input().split()))  # Demande à l'utilisateur de saisir une ligne de nombres séparés par des espaces.
# La méthode 'input().split()' retourne une liste de chaînes de caractères entrées par l'utilisateur.
# 'map(int, ...)' convertit chaque chaîne de la liste en un entier.
# 'list(...)' transforme le map object résultant en une liste d'entiers qui sera stockée dans la variable 'l'.

m = l[0]  # Assigne à 'm' la première valeur de la liste 'l'. Cette valeur servira comme base de calcul pour déterminer le PPCM.

# Démarre une boucle qui va parcourir tous les indices i de 0 à n-1 (soit tous les éléments de la liste 'l').
for i in range(n):
    # À chaque itération, on met à jour la valeur de 'm' en calculant le PPCM (plus petit commun multiple)
    # entre la valeur courante de 'm' et l'élément de 'l' à l'indice i.
    # Pour cela, on utilise la formule PPCM(a, b) = (a * b) // PGCD(a, b)
    # 'fractions.gcd(m, l[i])' calcule le PGCD (plus grand commun diviseur) des valeurs 'm' et 'l[i]'.
    # On multiplie ensuite 'm' par 'l[i]', puis on divise le résultat entier par ce PGCD pour obtenir le PPCM.
    m = m * l[i] // fractions.gcd(m, l[i])

# Après avoir parcouru tous les éléments de la liste, 'm' contient le PPCM de tous les nombres de la liste 'l'.
print(m)  # Affiche la valeur finale de 'm', qui est le PPCM de la liste d'entiers entrée par l'utilisateur.