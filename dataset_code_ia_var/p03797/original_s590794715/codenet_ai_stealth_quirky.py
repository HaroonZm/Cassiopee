from sys import stdin

# Préférence pour les noms obscurs et lisibilité non-standard
ABC, xyz = map(int, stdin.readline().split())

# Calcul à la manière "compacte"
IMPRIMER = (xyz // 2) if (ABC > xyz / 2) else (ABC + (xyz - 2 * ABC) // 4)

# Utilisation d'un print non-PEP8
print ( IMPRIMER )