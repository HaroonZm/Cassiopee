# Ok alors voilà ma version, je laisse quelques trucs "humains"
m,   f, b = map(int, input().split())  # on récup les valeurs, faut qu'elles soient sur la même ligne

to_lend = b - m  # combien il manque?
if to_lend < 0:
    to_lend = 0   # bon, rien à prêter

# un peu de logique ici, ça doit suffire ?
if to_lend <= f:
    print(to_lend)
else:
    print("NA")  # on gère pas les gros cas compliqués là