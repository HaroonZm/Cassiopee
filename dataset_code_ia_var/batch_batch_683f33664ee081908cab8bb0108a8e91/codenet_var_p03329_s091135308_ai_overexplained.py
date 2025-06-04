# Demande à l'utilisateur de saisir un nombre entier, stocké dans la variable 'y'.
# La fonction input() lit une entrée utilisateur, qui est une chaîne, donc on utilise int() pour la convertir en entier.
y = int(input())

# On crée une liste vide appelée 'res', qui va servir à stocker les résultats des calculs pour chaque valeur possible de i.
res = []

# On commence une boucle for. La variable de boucle 'i' va de 1 jusqu'à y inclus (range commence à 1, finit à y+1 car le deuxième argument n'est pas inclus).
for i in range(1, y + 1):
    # On initialise un compteur 'cnt' à 0. Il va stocker le nombre total d'opérations minimales pour représenter 'y' en utilisant 9^j et 6^j.
    cnt = 0

    # On assigne 'i' à la variable temporaire y1 (copie de i).
    y1 = i
    # On assigne (y - i) à la variable temporaire y2 (complément à i pour faire un découpage de y).
    y2 = y - i

    # On utilise une autre boucle for pour parcourir les valeurs de 'j' de 6 jusqu'à 1 (inclus), en décrémentant à chaque fois.
    # Ceci va servir à examiner les puissances de 9, de 9^6 à 9^1.
    for j in range(6, 0, -1):
        # On calcule 9 exposant j et le stocke dans t9.
        t9 = 9 ** j
        # Si y1 est supérieur ou égal à t9, cela signifie qu'on peut retirer (y1 // t9) fois t9 de y1.
        if y1 >= t9:
            # On incrémente le compteur cnt par le nombre de fois où t9 peut rentrer dans y1.
            cnt += y1 // t9
            # On met à jour y1 en enlevant tout ce qui peut être retiré par des entiers multiples de t9.
            y1 = y1 % t9
    # Après la boucle, on ajoute le reste de y1 à y2 pour pouvoir traiter le reste avec les puissances de 6.
    y2 += y1

    # Maintenant on va essayer de représenter y2 avec des puissances de 6.
    # Encore une boucle for, cette fois 'j' va de 7 à 1 (inclu), de haut en bas.
    for j in range(7, 0, -1):
        # On calcule 6 exposant j et le stocke dans t6.
        t6 = 6 ** j
        # Si y2 est plus grand ou égal à t6, on peut retirer (y2 // t6) fois t6 de y2.
        if y2 >= t6:
            # On incrémente cnt du nombre correspondant.
            cnt += y2 // t6
            # On met y2 à jour avec le reste de la division par t6.
            y2 = y2 % t6

    # Finalement, tout ce qui reste dans y2 ne peut être retiré qu'un par un (avec des 1), donc on ajoute directement y2 à cnt.
    cnt += y2
    # On ajoute cnt dans la liste res. Celle-ci garde le résultat pour chaque valeur de i.
    res.append(cnt)

# Quand toutes les valeurs possibles de i ont été testées, on affiche le minimum des résultats de la liste res.
# print() permet d'afficher la valeur sur la sortie standard (écran).
print(min(res))