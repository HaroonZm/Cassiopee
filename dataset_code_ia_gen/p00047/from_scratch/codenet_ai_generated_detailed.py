# Initialisation de la position du ballon sous le cup A
ball_position = 'A'

# Lecture des lignes d'entrée jusqu'à la fin
import sys
for line in sys.stdin:
    # Nettoyer la ligne pour enlever les espaces et les sauts de ligne
    line = line.strip()
    if not line:
        continue

    # Extraire les deux cups à échanger
    cup1, cup2 = line.split(',')

    # Si le ballon est sous un des cups échangés, on le déplace sous l'autre cup
    if ball_position == cup1:
        ball_position = cup2
    elif ball_position == cup2:
        ball_position = cup1

# Afficher la position finale du ballon
print(ball_position)