# Demander à l'utilisateur de saisir deux entiers séparés par un espace, puis les convertir en entiers.
# raw_input() lit une ligne de texte entrée par l'utilisateur.
# split() découpe la chaîne de caractères en utilisant l'espace comme séparateur, ce qui donne une liste de chaînes.
# map(int, ...) applique la fonction int à chaque élément de la liste obtenue, transformant ainsi les chaînes en entiers.
n, x = map(int, raw_input().split())

# Demander à l'utilisateur de saisir une séquence de nombres séparés par un espace.
# map(int, ...) convertit également chaque élément de la liste en entier.
# Ceci produit un objet de type liste contenant des entiers.
a = map(int, raw_input().split())

# Initialiser une variable compteur à 0. Cette variable servira à stocker le résultat final.
ans = 0

# Utiliser une boucle for pour itérer sur une plage d'entiers.
# xrange(n - 1) génère les entiers de 0 à n-2 inclus (donc n-1 valeurs au total) ; c'est important car l'indice i+1 ne doit pas dépasser la longueur de la liste 'a'.
for i in xrange(n - 1):
    # Calculer la somme des deux éléments consécutifs a[i] et a[i+1].
    # On soustrait ensuite la valeur de x au résultat.
    # Le résultat de cette opération est stocké dans la variable o.
    o = a[i] + a[i + 1] - x
    
    # Si le résultat o est strictement supérieur à 0, cela signifie que la somme des deux éléments dépasse x.
    # Dans ce cas, il faut "corriger" cette somme pour qu'elle ne dépasse pas x, conformément à la logique du problème.
    if o > 0:
        # Ajouter la valeur excédentaire au compteur 'ans'.
        ans += o
        # Réduire la valeur du deuxième nombre (a[i+1]) pour compenser le dépassement.
        # On ne peut pas retirer plus que la valeur actuelle de a[i + 1], donc on prend le minimum entre o et a[i + 1].
        # Cela permet de garder la valeur de a[i+1] non négative tout en respectant la contrainte de somme.
        a[i + 1] -= min(o, a[i + 1])

# Afficher le résultat final qui correspond au total des quantités retirées pour que les sommes successives ne dépassent pas x.
print ans