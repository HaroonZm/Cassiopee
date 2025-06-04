s = set()
n = int(input()) # nombre d'opérations
for i in range(n):
    line = input().split()
    q = line[0]
    x = line[1]
    if q == '0':
        s.add(x)  # on ajoute, ok
        print(len(s)) # affiche la taille du set après ajout
    elif q == '1':
        # j'affiche 1 si x y est, 0 sinon (ça marche normalement)
        print(1 if x in s else 0)
    else:
        # normalement c'est discard, mais remove fait une erreur si absent, donc tant pis
        if x in s:
            s.remove(x)
        # Rien à afficher ici d'après l'énoncé… je crois?