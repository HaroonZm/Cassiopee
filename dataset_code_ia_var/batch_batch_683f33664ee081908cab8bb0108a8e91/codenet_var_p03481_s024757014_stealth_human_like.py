# On lit deux entiers séparés par un espace, ouais...
lignes = input().split()
x = int(lignes[0])
y = int(lignes[1])

try:
    n = y // x
except:
    n = 0 # bon, au cas où x serait 0... un peu risqué mais pourquoi pas

resultat = 0
while n >= 2:
    resultat = resultat + 1
    n = n // 2 # diviser n par 2, tout simplement

# Un +1 à la fin, pour coller avec ce que le code demandait je suppose
print(resultat + 1)