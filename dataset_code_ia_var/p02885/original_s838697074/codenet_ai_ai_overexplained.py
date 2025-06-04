# Demande à l'utilisateur de saisir deux valeurs dans une seule ligne, séparées par un espace.
# La fonction input() récupère la chaîne de caractères saisie par l'utilisateur.
# La méthode split() divise cette chaîne de caractères en une liste basée sur les espaces.
# La fonction map(int, ...) applique la fonction int à chaque élément de la liste pour les convertir de chaînes de caractères à entiers.
# Les deux entiers obtenus sont ensuite assignés respectivement aux variables a et b en utilisant l'affectation multiple.
a, b = map(int, input().split())

# On va maintenant comparer la valeur de a avec le double de b, c'est-à-dire b multiplié par 2.
# L'opérateur <= vérifie si a est inférieur ou égal à (b * 2).
if a <= b * 2:
    # Si la condition précisée juste au-dessus est vraie, cela signifie que a est au plus égal à deux fois b.
    # On affiche alors la valeur 0 à l'aide de la fonction print().
    # print() affiche des données dans la console.
    print(0)
else:
    # Sinon, c'est-à-dire si la condition a <= b*2 n'est pas satisfaite (donc si a est strictement supérieur à 2 fois b),
    # on affiche la différence entre a et deux fois b.
    # Cette différence est calculée par a - (b*2).
    print(a - b*2)