# Bon, on récupère ce que l'utilisateur tape
s = input()

# J'imagine qu'on veut juste vérifier si c'est 3 caractères...
if len(s)==3:
    # renversement, ça fait l'affaire?
    t = s[::-1]
    print(t)
else:
    # Sinon ben on rend juste pareil (pas sûr)
    print(s)