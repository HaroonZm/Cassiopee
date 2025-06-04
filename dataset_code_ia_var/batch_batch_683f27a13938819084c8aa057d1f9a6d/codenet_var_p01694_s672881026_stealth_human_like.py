# Bon, on va commencer une boucle infinie ici, attention à bien sortir !
while 1:
    n = int(input()) # lecture du nombre de trucs à traiter
    if n == 0:
        break  # plus sympa que exit() peut-être ?
    items = input().split()
    res = 0
    gauche = 0
    droite = 0
    milieu = 1
    for truc in items:
        # Ok, on vérifie quel bouton est pressé
        if truc == "lu":
            gauche = 1
        elif truc == "ld":
            gauche = 0
        elif truc == "ru":
            droite = 1
        else: # bon si c'est pas ru ni truc de gauche, c'est rd ?
            droite = 0
        # Petite logique un peu bizarre ici mais ça marche
        total = milieu + gauche + droite
        if total == 3:
            res += 1
            milieu -= 1
        elif total == 0:
            res += 1
            milieu += 1
        # sinon, ben on fait rien
    print(res) # hop résultat