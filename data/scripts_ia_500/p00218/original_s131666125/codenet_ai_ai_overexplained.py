# Boucle infinie qui s'exécute continuellement jusqu'à ce qu'une condition d'arrêt soit rencontrée
while True:
    # Lecture de l'entrée utilisateur sous forme de chaîne de caractères
    n = input()
    # Conversion implicite de n en entier est nécessaire pour la comparaison,
    # mais ici on compare avec 0, donc n doit être converti en entier pour être fiable
    # pour s'assurer que n est un entier on peut faire int(n)
    # Si l'utilisateur entre "0" sous forme de chaîne, cela arrête la boucle
    if int(n) == 0:
        break  # Sort de la boucle infinie lorsque n est égal à zéro
    # Pour chaque i dans la plage de 0 à n-1, on exécute le corps de la boucle
    for i in range(int(n)):
        # Lecture d'une ligne de saisie utilisateur, attend 3 entiers séparés par espaces
        # Ensuite, on utilise map pour appliquer int à chaque élément séparé par split()
        # Cela convertit les trois valeurs lues en entiers spécifiques à pm, pe, pj
        pm, pe, pj = map(int, raw_input().split())
        # Calcul de la moyenne des trois notes comme un nombre à virgule flottante (float)
        ave = (pm + pe + pj) / 3.0  # division flottante pour précision décimale
        # Condition pour assigner la note "A":
        # 1) si n'importe quelle note est exactement égale à 100,
        # 2) ou si la moyenne de pm et pe est au moins 90,
        # 3) ou si la moyenne générale est au moins 80,
        # alors la note attribuée est "A"
        if (100 in (pm, pe, pj)) or ((pm + pe) / 2 >= 90) or (ave >= 80):
            print "A"  # affichage de la lettre "A"
        # Sinon, on évalue si on peut attribuer la note "B":
        # 1) si la moyenne générale est au moins 70,
        # 2) ou si la moyenne est au moins 50 et en même temps pm ou pe est au moins 80,
        # alors on affiche "B"
        elif (ave >= 70) or ((ave >= 50) and ((pm >= 80) or (pe >= 80))):
            print "B"  # affichage de la lettre "B"
        else:
            # Si aucune des conditions précédentes n'est remplie,
            # on attribue la note "C"
            print "C"  # affichage de la lettre "C"