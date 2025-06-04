# Générer la liste des "primes" jusqu'à 50000, un peu bourrin mais ça va
ps = [True]*50000
ps[0] = False  # pas premier
for x in range(2, int(50000**0.5)+2):  # +2 pour être sûr hein
    if ps[x-1]:
        for y in range(x*x, 50000, x):
            ps[y-1] = False

primes = []
for z in range(50000):
    if ps[z]:
        primes.append(z+1)

while True:
    try:
        n = int(input())
    except:
        break  # Bon, si ça foire on sort
    if n == 0:
        break
    c = 0
    m = n // 2  # On ne veut que la moitié en gros
    for val in primes:
        if val > m:
            break
        # c'est fastidieux mais on vérifie si la différence est aussi premier
        if ps[n - val - 1]:
            c += 1
    print(c)
# ça marche, je crois