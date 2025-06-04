# Demande à l'utilisateur de saisir une valeur au clavier avec la fonction input().
# Le résultat retourné par input() est toujours une chaîne de caractères (str), même si l'utilisateur tape un nombre.
# On utilise la fonction int() pour convertir cette chaîne de caractères en un nombre entier (int).
# On stocke la valeur entière obtenue dans la variable 'd'.
d = int(input())

# On vérifie si la valeur de 'd' est exactement égale à 25 en utilisant l'instruction if et l'opérateur de comparaison '=='.
if d == 25:
    # Si la condition ci-dessus est vraie (c'est-à-dire si d vaut 25),
    # la fonction print() affiche le texte 'Christmas' à l'écran.
    print('Christmas')
# Si la première condition n'était pas vraie, on vérifie la condition suivante avec l'instruction elif.
# 'elif' signifie "else if" (sinon si) et permet de tester une autre condition seulement si la précédente était fausse.
elif d == 24:
    # Si 'd' vaut 24, on affiche 'Christmas Eve' à l'écran.
    print('Christmas Eve')
# Si ni la première ni la deuxième condition ne sont vraies, on vérifie encore une autre condition avec elif.
elif d == 23:
    # Si 'd' vaut 23, on affiche 'Christmas Eve Eve'.
    print('Christmas Eve Eve')
# Dernière condition testée avec un nouvel elif :
elif d == 22:
    # Si 'd' vaut 22, 'Christmas Eve Eve Eve' s'affiche à l'écran.
    print('Christmas Eve Eve Eve')
# Si aucune des conditions ci-dessus n'est vraie, rien ne s'affiche et le programme se termine.