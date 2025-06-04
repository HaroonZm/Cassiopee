# Bon alors, je vais essayer d'écrire ça un peu... à la va-vite =)
while True:
    n = input()  # On lit le nombre d'entrées
    if n == 0:
        break  # si zéro faut arrêter (rien à calculer hein)
    best = None
    result = 0
    for j in xrange(n):
        idx, taille, poids = map(int, raw_input().split())
        bmi = float(poids) / ((float(taille)/100) ** 2)
        d = abs(22 - bmi)
        if best == None:
            best = d  # Premier passage, donc on prend ce qu'il y a
            result = idx
        else:
            if d < best:
                best = d
                result = idx  # hop, on met à jour si c'est plus proche de 22
    print result  # et voilà, on affiche la réponse
# Je ne sais plus si ça gère bien tous les cas... mais ça doit passer !