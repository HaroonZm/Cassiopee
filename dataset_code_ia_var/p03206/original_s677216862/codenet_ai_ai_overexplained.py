# Demande à l'utilisateur d'entrer une valeur, cette valeur représente un jour numérique
# La fonction input() affiche une invite (ici, vide) et retourne la saisie de l'utilisateur sous forme de chaîne de caractères (string)
# int() convertit cette chaîne de caractères en un nombre entier (integer) afin de pouvoir effectuer des comparaisons numériques avec
d = int(input())

# On utilise la structure de contrôle conditionnelle 'if-elif-else' pour déterminer à quel jour de décembre correspond la valeur entrée
# Chaque condition ci-dessous vérifie si la variable d est égale à un nombre précis
if d == 25:
    # Si d est exactement égal à 25, cela signifie que l'utilisateur a saisi 25, on imprime "Christmas"
    # La fonction print() affiche le texte passé en paramètre à l'écran, ici "Christmas"
    print("Christmas")
elif d == 24:
    # 'elif' est l'abréviation de 'else if', elle permet de vérifier une nouvelle condition si la précédente est fausse
    # Si d vaut 24, on affiche "Christmas Eve", qui signifie réveillon de Noël (veille de Noël en anglais)
    print("Christmas Eve")
elif d == 23:
    # Si d vaut 23, cela correspond à l'avant-veille de Noël, on affiche alors "Christmas Eve Eve"
    print("Christmas Eve Eve")
elif d == 22:
    # Si d vaut 22, cela correspond à trois jours avant Noël (l'avant-avant-veille), donc on affiche "Christmas Eve Eve Eve"
    print("Christmas Eve Eve Eve")
# Ici, il n'y a pas de 'else' donc si d n'est ni 25, 24, 23, ni 22, alors le programme ne fait rien et ne produit aucune sortie