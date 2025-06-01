# Demander à l'utilisateur d'entrer un nombre entier 'a',
# qui représente généralement la taille d'une séquence ou d'une liste.
a = int(input())

# Demander à l'utilisateur d'entrer plusieurs nombres séparés par des espaces,
# puis convertir chaque élément en entier grâce à 'map', et enfin les stocker dans une liste 'b'.
b = list(map(int, input().split()))

# Initialiser une liste vide nommée 'cave', qui sera utilisée pour stocker certains éléments
# selon des conditions définies dans la boucle suivante.
cave = []

# Commencer une boucle 'for' qui va itérer 'a' fois, où 'i' varie de 0 à a-1.
for i in range(a):
    # Prendre l'élément à la position 'i' dans la liste 'b', et l'assigner à la variable 'cat'.
    cat = b[i]

    # Vérifier si la valeur contenue dans 'cat' est strictement supérieure à zéro.
    if cat > 0:
        # Vérifier si cette valeur positive existe déjà dans la liste 'cave'.
        if cat in cave:
            # Si oui, afficher la position actuelle (index 'i' plus 1 pour humaniser la position)
            # puis arrêter la boucle immédiatement grâce à 'break'.
            print(i + 1)
            break
        else:
            # Si la valeur 'cat' n'est pas dans 'cave', l'ajouter à la liste 'cave'.
            cave.append(cat)
    else:
        # Dans le cas où 'cat' est inférieur ou égal à zéro (ici uniquement strictement négatif car 0 ne semble pas traité),
        # calculer son opposé (valeur positive correspondante) avec '-(cat)'.
        if -(cat) in cave:
            # Si l'opposé de 'cat' est présent dans 'cave',
            # vérifier si cet élément est le dernier de la liste 'cave' (cave[-1] signifie le dernier élément).
            if -(cat) == cave[-1]:
                # Si c'est bien le dernier élément, le retirer avec 'remove'.
                cave.remove(-(cat))
            else:
                # Sinon, afficher la position actuelle (index + 1) et interrompre la boucle.
                print(i + 1)
                break
        else:
            # Si l'opposé n'est pas trouvé dans la liste 'cave',
            # afficher la position actuelle (index + 1) puis arrêter la boucle.
            print(i + 1)
            break

    # Après toutes ces vérifications, si on a atteint la dernière itération (i+1 == a),
    # cela signifie que la boucle s'est terminée sans interruption,
    # donc afficher "OK" pour indiquer que tout est conforme aux conditions attendues.
    if i + 1 == a:
        print("OK")