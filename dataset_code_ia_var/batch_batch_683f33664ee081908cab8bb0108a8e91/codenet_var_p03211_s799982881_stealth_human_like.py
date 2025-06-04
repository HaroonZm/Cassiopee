# Honnêtement, j'aurais pu choisir une valeur plus explicite pour m... mais bon, 999 ça marche
m = 999
s = input('Tape une chaîne : ')
# Parcours un peu bizarre, je trouve, mais bon, c'est comme ça qu'on fait
for i in range(0, len(s) - 2):
    x = int(s[i:i+3])  # Je récupère un groupe de 3 chiffres à partir de là
    diff = abs(753 - x)
    if diff < m:  # Logiquement c'est mieux dans ce sens, non ?
        m = diff
# Peut-être qu'il faudrait afficher autre chose, mais ça suffit pour le moment
print(m)