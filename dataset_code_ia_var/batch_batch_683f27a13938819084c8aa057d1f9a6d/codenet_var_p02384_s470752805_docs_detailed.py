def North(dice):
    """
    Effectue une rotation nord sur le dé. Déplace les faces du dé comme si on roulait le dé vers le nord.
    Args:
        dice (list): Liste représentant les faces du dé [top, front, right, left, back, bottom].
    Returns:
        list: Dé après la rotation nord.
    """
    # Stocke temporairement la valeur de la face du haut
    temp = dice[0]
    # La face du haut reçoit la face de devant
    dice[0] = dice[1]
    # La face de devant reçoit la face du bas
    dice[1] = dice[5]
    # La face du bas reçoit la face de derrière
    dice[5] = dice[4]
    # La face de derrière reçoit la valeur temporisée (ancienne face du haut)
    dice[4] = temp
    return dice

def East(dice):
    """
    Effectue une rotation est sur le dé. Déplace les faces du dé comme si on roulait le dé vers l'est.
    Args:
        dice (list): Liste représentant les faces du dé [top, front, right, left, back, bottom].
    Returns:
        list: Dé après la rotation est.
    """
    # Stocke temporairement la valeur de la face de devant
    temp = dice[1]
    # La face de devant reçoit la face de droite
    dice[1] = dice[2]
    # La face de droite reçoit la face de derrière
    dice[2] = dice[4]
    # La face de derrière reçoit la face de gauche
    dice[4] = dice[3]
    # La face de gauche reçoit la valeur temporisée (ancienne face de devant)
    dice[3] = temp
    return dice

def West(dice):
    """
    Effectue une rotation ouest sur le dé. Déplace les faces du dé comme si on roulait le dé vers l'ouest.
    Args:
        dice (list): Liste représentant les faces du dé [top, front, right, left, back, bottom].
    Returns:
        list: Dé après la rotation ouest.
    """
    # Stocke temporairement la valeur de la face du haut
    temp = dice[0]
    # La face du haut reçoit la face de droite
    dice[0] = dice[2]
    # La face de droite reçoit la face du bas
    dice[2] = dice[5]
    # La face du bas reçoit la face de gauche
    dice[5] = dice[3]
    # La face de gauche reçoit la valeur temporisée (ancienne face du haut)
    dice[3] = temp
    return dice

# Constante représentant le nombre maximum de rotations pour chacune des trois directions
maxloop = 4

# Compteurs pour les rotations nord, est, ouest
Ncnt = 0
Ecnt = 0
Wcnt = 0

# Lecture des valeurs initiales du dé, sous forme d'une liste de chaînes
Dice = input().split()

# Conversion stricte : tous les éléments sont des chaînes à ce stade
q = int(input())  # Le nombre de questions

# Copie de la configuration initiale du dé pour pouvoir la restaurer après chaque requête
CopyDice = Dice.copy()

# Boucle principale : traite chaque question (configuration cible)
for i1 in range(q):
    # Boucles de contrôle pour chaque direction de rotation
    Nloop = True
    Eloop = True
    Wloop = True
    Ncnt = 0
    Ecnt = 0
    Wcnt = 0
    # Lecture des valeurs cibles (face du haut, face de devant)
    I = input().split()
    top = I[0]
    front = I[1]
    # Réinitialise la configuration du dé pour chaque question
    Dice = CopyDice.copy()
    # Essaye toutes les combinaisons possibles de rotations pour trouver la configuration désirée
    while Eloop:
        while Nloop:
            while Wloop:
                # Si la configuration courante du dé correspond à la cible
                if Dice[0] == top and Dice[1] == front:
                    # Affiche la valeur de la face droite
                    print(Dice[2])
                    # Termine toutes les boucles
                    Nloop = False
                    Eloop = False
                    Wloop = False
                    break
                # Sinon, effectue une rotation ouest
                Dice = West(Dice)
                Wcnt += 1
                # Après 4 rotations ouest on a fait le tour, on sort de la boucle ouest
                if Wcnt == maxloop:
                    Wloop = False
            # Rotation nord pour changer l'orientation verticale
            Dice = North(Dice)
            Wcnt = 0
            Wloop = True  # Réactive la boucle ouest pour la nouvelle orientation
            Ncnt += 1
            # Après 4 rotations nord on a fait le tour, on sort de la boucle nord
            if Ncnt == maxloop:
                Nloop = False
        # Rotation est pour changer le "plan" des faces
        Dice = East(Dice)
        Ncnt = 0
        Nloop = True  # Réactive la boucle nord pour la nouvelle orientation
        Ecnt += 1
        # Après 4 rotations est, on a fait le tour, on sort de cette boucle
        if Ecnt == maxloop:
            Eloop = False
    # Après avoir trouvé la réponse ou parcouru toutes les possibilités, on passe à la requête suivante
    # La configuration du dé est restaurée au début de la boucle, pas besoin ici de le faire