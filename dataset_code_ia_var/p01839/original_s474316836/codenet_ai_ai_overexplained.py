# Création d'une liste vide qui va contenir les éléments saisis par l'utilisateur
l = []
# Demande à l'utilisateur de saisir le nombre total d'éléments qu'il va entrer,
# et convertit ce nombre en entier avec la fonction int()
nombre_delements = int(input())
# Utilisation d'une boucle for pour répéter le processus de saisie 'nombre_delements' fois
for _ in range(nombre_delements):
    # À chaque itération, on demande à l'utilisateur de saisir un élément avec input()
    # La chaîne saisie est ajoutée à la liste 'l' à l'aide de la méthode append()
    l.append(input())

# Création d'une nouvelle liste vide 's', qui sera utilisée comme une pile (stack)
s = []

# Création d'un indicateur booléen initialisé à False pour savoir si l'on doit afficher 'NO'
isno = False

# Début d'une boucle for pour parcourir chaque élément 'i' dans la liste 'l'
for i in l:
    # Vérifie si l'élément 'i' est égal à la chaîne de caractères "A"
    if i == "A":
        # Si c'est le cas, on ajoute l'entier 1 à la pile 's'
        # Cela représente le fait d'ajouter un élément à la pile
        s.append(1)
    else:
        # Si l'élément n'est pas "A", on tente de retirer un élément de la pile
        try:
            # La méthode pop() essaie de retirer et de retourner le dernier élément de 's'
            # Ici, la valeur retournée n'est pas utilisée, donc on l'affecte à la variable '_'
            _ = s.pop()
        except:
            # Si une exception se produit dans le bloc try (par exemple, si la pile est vide),
            # alors la pile était vide et on ne peut pas retirer d'élément : c'est une erreur
            # On affiche donc "NO" pour indiquer une opération invalide
            print("NO")
            # On met à jour l'indicateur pour signaler l'affichage de "NO"
            isno = True
            # On interrompt la boucle for en utilisant break, car une erreur a été détectée
            break

# Après la boucle, on vérifie les conditions pour afficher le résultat final
# Si l'indicateur 'isno' est toujours False (c'est-à-dire qu'aucune erreur n'a eu lieu dans la boucle)
# et si la pile 's' est vide, cela veut dire que toutes les opérations étaient valides et qu'il n'y a pas d'éléments restants
if not isno and not s:
    # Affiche "YES" pour indiquer que la séquence d'opérations était valide et correctement appariée
    print("YES")
# Sinon, si aucune erreur n'a été détectée (isno est False), mais qu'il reste des éléments dans la pile 's'
elif not isno and s:
    # Cela veut dire qu'il reste des éléments sans correspondance dans la pile, donc on affiche "NO"
    print("NO")