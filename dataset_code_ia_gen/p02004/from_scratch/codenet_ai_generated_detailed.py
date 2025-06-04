# Solution complète pour le problème GuruGuru

# Approche :
# 1. On modélise l'orientation de Gururin par un entier représentant les 4 directions:
#    0 = Nord, 1 = Est, 2 = Sud, 3 = Ouest.
# 2. Initialement, Gururin fait face au Nord (orientation = 0).
# 3. Pour chaque commande, on met à jour l'orientation:
#      - 'R' : orientation = (orientation + 1) % 4
#      - 'L' : orientation = (orientation - 1) % 4
# 4. Une "magical power" est obtenue chaque fois qu'une sous-séquence spéciale est détectée:
#    - La séquence commence face au Nord,
#    - La séquence se termine face au Nord,
#    - Entre-temps, on ne doit jamais être face au Nord,
#    - Et les directions Est, Sud, Ouest doivent être rencontrées *au moins une fois* chacune,
#      toutes ces directions doivent être rencontrées immédiatement après un 'R'.
# 5. On parcourt la séquence et on détecte ces sous-séquences. Chaque fois qu'on revient à
#    Nord après avoir validé les conditions, on incrémente le compteur.
# 6. On réinitialise les marqueurs à chaque départ d'une nouvelle tentative de "magical power".

s = input()

# variables d'état
orientation = 0  # 0=N,1=E,2=S,3=W
count_magical = 0

# Pour calculer la sous-séquence spéciale:
# On enregistre:
# - set_r_dirs : directions rencontrées immédiatement après un 'R' (doit contenir 1,2,3 à la fin)
# - in_special : indique si on est en train de traiter une sous-séquence spéciale
# - last_cmd : dernière commande lue (permet de savoir si la direction actuelle a été atteinte après un 'R')

in_special = False
set_r_dirs = set()
last_cmd = None  # Stocke 'R' ou 'L'

for cmd in s:
    # Mettre à jour orientation selon commande
    if cmd == 'R':
        orientation = (orientation + 1) % 4
    else:
        orientation = (orientation - 1) % 4

    # Détecter début d'une nouvelle sous-séquence spéciale: orientation == 0 (nord) et pas en cours
    if not in_special and orientation == 0:
        # On commence une nouvelle tentative spéciale ici
        in_special = True
        set_r_dirs = set()
    elif in_special:
        # Si on est en cours de sous-séquence spéciale, vérifier si on rencontre nord
        if orientation == 0:
            # Fin possible de la sous-séquence spéciale
            # Vérifier si conditions sont remplies:
            # 1. on a rencontré Est (1), Sud(2) et Ouest(3) au moins une fois immédiatement après 'R'
            if {1,2,3}.issubset(set_r_dirs):
                count_magical += 1
            # Réinitialiser pour une nouvelle tentative
            in_special = True  # reste True car on est toujours face a Nord, début d'une nouvelle sous-séquence
            set_r_dirs = set()
        else:
            # On est dans le milieu de la sous-séquence spéciale
            # sauf qu'on ne doit pas faire face au Nord ici selon l'énoncé
            # Donc on continue seulement si on ne fait pas face à Nord
            # On vérifie si la direction actuelle est atteinte *après* une commande 'R'
            if last_cmd == 'R':
                # On marque cette direction
                # Seulement relevons Est, Sud, Ouest
                if orientation in (1,2,3):
                    set_r_dirs.add(orientation)
            elif orientation == 0:
                # Cela arrive si on subit un retour au nord non prévu, on doit reset pour repartir proprement
                # mais la condition est déjà vérifiée au dessus, donc ce else est sûr et suffisant
                pass

    last_cmd = cmd

print(count_magical)