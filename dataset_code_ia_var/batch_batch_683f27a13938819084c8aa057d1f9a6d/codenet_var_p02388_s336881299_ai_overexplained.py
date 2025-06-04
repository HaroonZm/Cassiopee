# Demande à l'utilisateur d'entrer une valeur au clavier.
# La fonction input() lit une ligne de texte qui est tapée par l'utilisateur et la retourne sous forme de chaîne de caractères (string).
x = input()

# Multiplie x par lui-même deux fois pour obtenir son cube.
# En pratique : x * x donne x au carré, puis (x * x) * x donne x au cube.
# IMPORTANT : En Python 2, la fonction input() évalue automatiquement l'entrée, donc x peut devenir un int ou un float directement.
# La multiplication * est utilisée ici pour les nombres, c'est l'opération mathématique de base qui multiplie les deux valeurs.
resultat = x * x * x

# Affiche le résultat sous forme de chaîne de caractères à l'écran.
# La fonction str() convertit n'importe quel objet en une représentation sous forme de chaîne de caractères (string).
# Cela signifie que si resultat est un nombre, str(resutat) va créer un texte correspondant à ce nombre pour l'affichage.
# La fonction print affiche ce texte à la sortie standard (la console ou le terminal).
print str(resultat)