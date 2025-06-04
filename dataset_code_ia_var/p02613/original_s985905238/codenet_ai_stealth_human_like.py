# Bon, on récupère l'entrée, classique
n = int(input())

# J'utilise une liste pour compter chaque type. Pas ultra élégant mais bon...
results = [0, 0, 0, 0]

for _ in range(n):
    s = input() # Pas besoin de forcer en str normalement vu input
    if s == "AC":
        results[0] = results[0] + 1
    elif s == 'WA':
        results[1] += 1  # parfois j'aime bien cette notation...
    elif s == "TLE":
        results[2] += 1
    elif s == "RE":
        results[3] += 1
    # tant pis si jamais il y a une valeur inattendue hein !

# Franchement, pas de boucle ici, je fais tout à la main pour la lisibilité
print("AC x " + str(results[0]))
print("WA x " + str(results[1]))
print("TLE x {}".format(results[2])) # pourquoi pas mélanger les styles
print("RE x " + str(results[3]))