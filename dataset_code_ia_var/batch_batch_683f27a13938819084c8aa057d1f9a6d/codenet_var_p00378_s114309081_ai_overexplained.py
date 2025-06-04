# Demande à l'utilisateur de saisir trois entiers séparés par des espaces, puis utilise la fonction map pour convertir les entrées en entiers.
# Les valeurs sont stockées dans les variables a, b et x respectivement.
a, b, x = map(int, input().split())

# Utilise la fonction divmod pour effectuer à la fois une division entière et obtenir le reste.
# divmod(x, 1000) retourne un tuple : le premier élément (d) est le quotient (c'est-à-dire le nombre de fois où 1000 rentre dans x),
# le deuxième élément (mo) est le reste de la division de x par 1000.
d, mo = divmod(x, 1000)

# Vérifie si le reste mo est strictement supérieur à 500.
if mo > 500:
    # Si c'est le cas, on calcule trois expressions différentes qui représentent divers coûts possibles.
    # 1. d*a + 2*b : On multiplie le quotient d par a (coût pour chaque mille), puis ajoute 2 fois b (peut représenter un surcoût).
    # 2. (d+1)*a : On ajoute 1 à d puis multiplie par a, c'est-à-dire on prend un supplément complet de mille.
    # 3. (d*2 + 2)*b : On multiplie d par 2 puis ajoute 2, le tout multiplié par b (autre manière de calculer un coût).
    # La fonction min retourne la plus petite des trois valeurs.
    print(min(d*a + 2*b, (d+1)*a, (d*2 + 2)*b))
# Si le reste mo n'est pas supérieur à 500, on vérifie maintenant s'il est différent de 0 (donc compris entre 1 et 500 inclus).
elif mo != 0:
    # Calcule trois autres expressions correspondant à d'autres stratégies de coût.
    # 1. d*a + b : d fois a, puis ajoute simplement b.
    # 2. (d+1)*a : Comme précédemment, on paie un supplément complet.
    # 3. (d*2 + 1)*b : d fois 2, puis ajoute 1, le tout multiplié par b.
    # Encore une fois, on imprime le minimum des trois.
    print(min(d*a + b, (d+1)*a, (d*2 + 1)*b))
# Si le reste mo vaut 0, c'est-à-dire que x est un multiple exact de 1000.
else:
    # Calcule deux façons de calculer le coût.
    # 1. d*a : d multiplié par a.
    # 2. d*2*b : d multiplié par 2, puis multiplié par b.
    # Utilise min pour prendre la valeur la plus petite et l'affiche.
    print(min(d*a, d*2*b))