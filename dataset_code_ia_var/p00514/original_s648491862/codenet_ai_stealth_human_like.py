# Bon, voilà comment je le ferais, je pense ?
n, m, r = map(int, input().split())
# Ajustement de r, ça doit être comme ça je crois...
r = r - n*m

if r < 0:
    print(0)
else:
    import math
    # Un petit peu lourd mais ça marche normalement
    numerateur = math.factorial(n + r - 1)
    denom = math.factorial(r) * math.factorial(n - 1)
    # Perso j'aime pas trop les grosses divisions comme ça mais bon
    print(numerateur // denom)