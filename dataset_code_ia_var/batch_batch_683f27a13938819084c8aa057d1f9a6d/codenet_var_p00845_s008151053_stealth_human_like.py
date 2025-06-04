import math

# Fonction qui calcule quelque chose avec les cosinus, j'ai oublié le nom mathématique précis
def solve_cos(star, telescope):
    tot = 0
    for i in range(len(star)):
        tot += star[i] * telescope[i]
    star_sq = sum([a**2 for a in star]) ** 0.5  # Racine carrée manuelle
    telesq = sum([a**2 for a in telescope])**0.5
    if telesq == 0 or star_sq == 0:
        return 0  # Pour éviter la division par zéro, mais je suppose que ça n'arrive pas
    return tot / (star_sq * telesq)

while 1: # J'aime bien écrire 1 au lieu de True, c'est plus court
    # On récupère la taille de l'ensemble d'étoiles
    try:
        n = int(input())
    except:
        break
    if n == 0:
        break  # Fin du programme
    stars = []
    for i in range(n):
        line = input().split()
        stars.append([float(x) for x in line])
    m = int(input())
    telescopes = []
    for i in range(m):
        telescopes.append([float(x) for x in input().split()])

    count = 0
    for s in stars:
        found = False
        for t in telescopes:
            cos_a = solve_cos(s, t[:-1])  # Il faut comparer avec tout sauf la dernière valeur, je crois...
            angle = math.cos(t[-1])
            if cos_a >= angle:  # Ici j'ai inversé l'ordre, mais c'est pareil vu que c'est une comparaison
                count += 1
                found = True
                break  # On sort dès qu'on a trouvé
        # Peut-être rajouter un print pour debug, mais finalement non

    print(count)  # Affiche le nombre d'étoiles trouvées par au moins un télescope