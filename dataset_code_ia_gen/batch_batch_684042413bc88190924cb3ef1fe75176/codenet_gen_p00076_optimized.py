import sys
import math

def treasure_position(n):
    # On commence à (1,0) face à l'ouest (vers le puits à l'ouest de cette position)
    # L'actuelle position est donc après le premier déplacement
    x, y = 1.0, 0.0
    # Direction initiale face au puits : vers l'ouest (angle π rad)
    angle = math.pi
    for _ in range(n - 1):
        # Tourner à droite de 90° (−π/2)
        angle -= math.pi / 2
        # Avancer de 1 mètre dans la direction actuelle
        x += math.cos(angle)
        y += math.sin(angle)
        # Se tourner vers le puits (ouest), angle π
        angle = math.pi
    return x, y

for line in sys.stdin:
    line = line.strip()
    if line == '-1':
        break
    n = int(line)
    x, y = treasure_position(n)
    print(f"{x:.2f}")
    print(f"{y:.2f}")