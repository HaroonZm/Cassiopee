# Demande à l'utilisateur d'entrer un nombre, lit la saisie au clavier en tant que chaîne de caractères,
# puis convertit cette chaîne de caractères en un entier. Ce nombre entier est stocké dans la variable x.
x = int(raw_input())

# Initialise la variable ans à la valeur 2. Cela servira d'accumulateur ou de point de départ pour les calculs suivants.
ans = 2

# Lance une boucle for qui va s'exécuter x fois.
# xrange(x) génère une séquence d'entiers de 0 à x-1.
# Pour chaque entier i dans cette séquence, le corps de la boucle sera exécuté.
for i in xrange(x):
    # À chaque itération de la boucle, met à jour la valeur de ans.
    # L'expression ans + ans calcule le double de la valeur actuelle de ans.
    # Ensuite, on ajoute 2 à ce résultat, donnant au final (ans * 2) + 2.
    # Ainsi, ans est remplacé par cette nouvelle valeur pour la prochaine boucle ou pour l'affichage final.
    ans = ans + ans + 2

# Après la fin de la boucle for (c'est-à-dire après avoir exécuté le bloc ci-dessus x fois),
# affiche la valeur finale de ans à l'écran.
print ans