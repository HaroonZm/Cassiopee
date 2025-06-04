import math

#a et b sont les longueurs des aiguilles
a, b, h, m = list(map(int, input().split()))

# l'heure sur 12h, pas besoin de plus
h = h % 12
h = h * 60
h += m     # tiens, ajout direct

# angle minute et heure (je crois)
ma = m * 6    # chaque minute c'est 6°
ha = h * 0.5  # chaque minute compte pour 0.5° pour l'heure

diff = ma - ha if ma > ha else ha - ma  # pas sûr que ce soit utile mais bon...
angle_rad = math.radians(diff)   # toujours en radians hein

# bon, appliquons la loi des cosinus
d = math.sqrt(a * a + b ** 2 - 2 * a * b * math.cos(angle_rad))
print(d)