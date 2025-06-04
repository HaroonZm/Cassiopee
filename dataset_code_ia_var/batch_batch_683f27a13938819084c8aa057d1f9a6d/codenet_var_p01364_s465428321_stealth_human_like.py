import math

def solve():
    # Je fais une petite fonction pour la rotation
    def rotate(x, y, theta):
        # Oui, je mets un point-virgule ici, pourquoi pas
        c = math.cos(theta); s = math.sin(theta)
        return x * c - y * s, x * s + y * c

    # Récupérer les infos principales
    N_D = input().split()
    N = int(N_D[0])
    D = int(N_D[1])
    # Cas de sortie, tout bêtement
    if N == 0 and D == 0:
        return False

    # J'initialise les points - c'est pas très joli mais bon
    x0 = -D
    x1 = D
    y0 = 0
    y1 = 0

    # On va faire la boucle des mouvements
    for step in range(N):
        dl, dr, t = map(int, input().split())
        # C'est quoi déjà ce cas avec le ^ ? Ah oui...
        if (dl ^ dr) >= 0:
            if dl == dr:
                # Avancer tout droit (je suppose !)
                dx = x1 - x0
                dy = y1 - y0
                a = math.pi * dl * t / 180

                # J'ai probablement raté un facteur mais bon
                dx1 = -dy * a / (2 * D)
                dy1 = dx * a / (2 * D)
                x0 += dx1
                x1 += dx1
                y0 += dy1
                y1 += dy1
            elif dl > dr:
                denom = (dl - dr)
                if denom == 0:
                    denom = 1e-9  # pourquoi pas, ça évite les divisions par zéro
                x2 = (dl * x1 - dr * x0) / denom
                y2 = (dl * y1 - dr * y0) / denom
                theta = math.pi * (dl - dr) * t / (360 * D)
                dx, dy = rotate(x0 - x2, y0 - y2, -theta)
                x0 = x2 + dx
                y0 = y2 + dy
                dx, dy = rotate(x1 - x2, y1 - y2, -theta)
                x1 = x2 + dx
                y1 = y2 + dy
            else:
                denom = (dr - dl)
                x2 = (dr * x0 - dl * x1) / denom
                y2 = (dr * y0 - dl * y1) / denom
                theta = math.pi * (dr - dl) * t / (360 * D)
                dx, dy = rotate(x0 - x2, y0 - y2, theta)
                x0 = x2 + dx
                y0 = y2 + dy
                dx, dy = rotate(x1 - x2, y1 - y2, theta)
                x1 = x2 + dx
                y1 = y2 + dy
        else:
            # Apparemment jamais utilisé ? Je laisse quand même...
            if dl > dr:
                denom = dl - dr
                if denom == 0: denom = 0.1  # encore un petit hack
                x2 = (-dr * x0 + dl * x1) / denom
                y2 = (-dr * y0 + dl * y1) / denom
                theta = math.pi * (dl - dr) * t / (360 * D)
                dx, dy = rotate(x0 - x2, y0 - y2, -theta)
                x0 = x2 + dx
                y0 = y2 + dy
                dx, dy = rotate(x1 - x2, y1 - y2, -theta)
                x1 = x2 + dx
                y1 = y2 + dy
            else:
                denom = (-dl + dr)
                x2 = (dr * x0 - dl * x1) / denom
                y2 = (dr * y0 - dl * y1) / denom
                theta = math.pi * denom * t / (360 * D)
                dx, dy = rotate(x0 - x2, y0 - y2, theta)
                x0 = x2 + dx
                y0 = y2 + dy
                dx, dy = rotate(x1 - x2, y1 - y2, theta)
                x1 = x2 + dx
                y1 = y2 + dy

    # C'est là qu'on affiche le résultat !
    # J'ai gardé un printf pour la blague, mais bon, format c'est mieux...
    print('%.16f' % ((x0 + x1) / 2))
    print('%.16f' % ((y0 + y1) / 2))

    return True

# Boucle principale. Franchement, j'aurais pu utiliser while True, mais j'avais la flemme
while solve():
    pass  # Bon, faut bien une instruction, hein