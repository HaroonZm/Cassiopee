# Demande à l'utilisateur d'entrer une donnée, mais ici la variable 'n' n'est pas utilisée
n = input()

# Demande à l'utilisateur d'entrer une ligne de texte, sépare cette ligne en une liste de chaînes où chaque chaîne représente un nombre,
# puis convertit chaque chaîne en entier à l'aide d'une compréhension de liste et range les entiers dans la liste An
An = [int(x) for x in input().split()]

# Initialise un compteur pour compter combien de valeurs dans An sont divisibles par 3 sans reste (modulo 0)
mod0 = 0

# Initialise un compteur pour compter combien de valeurs donnent un reste de 1 lorsqu'elles sont divisées par 3 (modulo 1)
mod1 = 0

# Initialise un compteur pour compter combien de valeurs donnent un reste de 2 lorsqu'elles sont divisées par 3 (modulo 2)
mod2 = 0

# Parcourt chaque élément dans la liste An un par un
for x in An:
    # Vérifie si le reste de la division de x par 3 est égal à 0, c'est-à-dire si x est un multiple de 3
    if x % 3 == 0:
        # Si oui, augmente de 1 le compteur mod0
        mod0 += 1
    # Vérifie si le reste de la division de x par 3 est égal à 1
    if x % 3 == 1:
        # Si oui, augmente de 1 le compteur mod1
        mod1 += 1
    # Vérifie si le reste de la division de x par 3 est égal à 2
    if x % 3 == 2:
        # Si oui, augmente de 1 le compteur mod2
        mod2 += 1

# Après avoir compté tous les éléments, examine les valeurs de mod1 et mod2 pour décider quoi afficher
# Si les compteurs mod1 et mod2 sont tous les deux à 0, cela signifie que tous les éléments d'An sont des multiples de 3
if mod1 == 0 and mod2 == 0:
    # Affiche le chiffre "1" à l'écran
    print("1")
# Sinon, si la différence absolue entre mod1 et mod2 est inférieure ou égale à 3
elif abs(mod1 - mod2) <= 3:
    # Alors affiche simplement la somme totale des éléments (la somme des trois compteurs)
    print((mod0+mod1+mod2))
# Sinon (si la différence entre mod1 et mod2 est strictement supérieure à 3)
else:
    # Si mod1 est strictement plus grand que mod2
    if mod1>mod2:
        # Affiche la somme de mod0, deux fois mod2, puis ajoute 3
        print((mod0+mod2+mod2+3))
    # Si mod2 est strictement plus grand que mod1
    if mod1<mod2:
        # Affiche la somme de mod0, deux fois mod1, puis ajoute 3
        print((mod0+mod1+mod1+3))