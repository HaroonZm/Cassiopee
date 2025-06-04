# Commencer une boucle infinie qui ne s'arrête que via une condition de sortie explicite (break)
while True:
    # Demander à l'utilisateur une chaîne de caractères via la fonction input()
    # Convertir cette chaîne directement en liste de caractères avec list() pour permettre leur manipulation ultérieure
    s1 = list(input())
    # Si s1 est égal à une liste contenant le caractère '-', c'est le signal pour arrêter la boucle
    if s1 == ["-"]:
        break  # Quitter la boucle while immédiatement

    # Demander une deuxième entrée utilisateur, qui sera transformée en une liste de caractères nommée s2
    s2 = list(input())

    # Inverser la liste s1 grâce à la méthode reverse(), cela modifie la liste s1 en place (rien n'est renvoyé)
    s1.reverse()
    # Inverser la liste s2 de la même manière
    s2.reverse()

    # Demander à l'utilisateur une autre saisie (probablement une séquence de 'underline'), stockée sous le nom 'under', également convertie en liste de caractères
    under = list(input())
    # Inverser la liste under pour faciliter le traitement ultérieur
    under.reverse()

    # Initialiser une nouvelle liste vide, 'right', qui va contenir des éléments (caractères) au fur et à mesure du processus
    right = []

    # Extraire de la liste s2 le dernier caractère avec pop(), qui enlève et retourne le dernier élément de la liste (s2 est inversée, donc cela récupère le premier caractère original)
    center = s2.pop()

    # Démarrer une boucle qui continue tant qu'il reste au moins un élément dans s1 ou s2 (condition 'or')
    while s1 or s2:
        # Vérifier si la liste under n'est pas vide ET que le caractère center est le même que le dernier élément de la liste under (sous-entendu: 'center' doit être "traité")
        if under and center == under[-1]:
            # Remplacer center par le dernier caractère retiré de s1 (s1.pop()), équivalent à avancer d'un caractère dans la "pile" s1
            center = s1.pop()
            # Enlever également de under le dernier caractère (pour garder les structures synchronisées)
            under.pop()
        else:
            # Si les conditions précédentes ne sont pas vraies, ajouter center à la liste right
            right.append(center)
            # Extraire le caractère suivant depuis la liste s2 (en mode pile), pour devenir le nouveau center
            center = s2.pop()

    # Après la sortie de la boucle, si under n'a plus d'éléments (sous-entendu: tout a été traité dans under)
    if not under:
        # Ajouter le dernier caractère center à la liste right
        right.append(center)

    # Convertir la liste right, qui est une séquence de caractères, en chaîne de caractères via join() et afficher le résultat à l'écran avec print
    print("".join(right))