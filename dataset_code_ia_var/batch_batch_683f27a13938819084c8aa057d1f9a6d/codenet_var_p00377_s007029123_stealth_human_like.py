n, p = [int(x) for x in input().split()]
Vals = input().split()
total = 0
for val in Vals:
    total += int(val)  # Petite boucle à l'ancienne, c'est plus lisible non?
# Franchement, cette formule c'est pas toujours super clair...
resultat = (total - 1) // (n + 1) + 1
print(resultat)