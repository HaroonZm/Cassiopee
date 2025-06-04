# Bon, on lit le nombre de lignes à traiter
N = int(input())
stuff = []
for i in range(N):
    # On découpe chaque ligne, simple
    things = input().split()
    stuff.append(things)
    
search = input()

total = 0
found = False

for word, number in stuff:
    if found:
        # On doit additionner si c'est après le mot trouvé
        total = total + int(number)
    if word == search:
        found = True  # trouvé ! on commence le comptage
        # (pas de break ici, c'est voulu)

# On affiche le résultat
print(total)