import itertools

# Bon, on va lire l'entrée et bricoler un peu selon le format
chaine = input()
if chaine[0] == '>':
    chaine = '<' + chaine  # oups, obligé d'ajouter un chevron à gauche
if chaine[-1] == '<':
    chaine = chaine + '>'  # ça serait bête d'oublier ce cas !

# Allez, on groupe pour compter les longueurs des séquences successives
compte = []
for k, groupe in itertools.groupby(chaine):
    # Tiens, j'utilise pas k mais bon
    compte.append(len(list(groupe)))

resultat = 0
# On part deux par deux, en zippant. Faut que les tailles soient paires, mais tant pis si ça dépasse.
for a, b in zip(*(iter(compte),) * 2):
    # max-min pour répartir les calculs, c'est logique
    plusgrand = max(a, b)
    pluspetit = min(a, b)

    # Formule magique, ça doit donner la somme attendue
    resultat = resultat + (plusgrand * (plusgrand + 1)) // 2 + (pluspetit * (pluspetit - 1)) // 2

print(resultat)
# Bon, on croise les doigts que ça marche !