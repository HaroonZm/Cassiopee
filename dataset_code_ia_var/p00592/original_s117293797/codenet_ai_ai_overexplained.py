# Définition de la fonction cv(t)
def cv(t):
    # Cette fonction convertit l'heure donnée au format 'hhmm' en nombre de minutes
    # 1. t//100 donne les heures
    # 2. On multiplie par 60 pour obtenir les minutes totales d'heures entières
    # 3. t%100 donne les minutes (la partie des dizaines et unités)
    # Par exemple : t=1345 => 13*60 + 45 => 825 minutes
    return t // 100 * 60 + t % 100

# Début d'une boucle infinie : l'exécution se poursuit jusqu'à ce qu'on rencontre 'break'
while 1:
    # Lecture d'une ligne d'entrée, séparation en 3 entiers : n, p, q
    # 'map' applique int() sur chaque élément du résultat de split()
    # raw_input() lit une ligne entrée par l'utilisateur (compatible Python 2)
    n, p, q = map(int, raw_input().split())
    
    # Si n vaut 0, on quitte la boucle avec 'break'
    if n == 0:
        break
    
    # Création d'une liste v de 1440 zéros
    # 1440 correspond au nombre total de minutes dans une journée (24 * 60)
    v = [0] * 1440
    
    # On itère sur les n personnes/emplois du temps
    for i in range(n):
        # On lit un entier k : le nombre de créneaux occupés par la personne
        k = int(raw_input())
        
        # On lit ensuite une liste de 2*k entiers (horaires des créneaux)
        # Chaque paire d'entiers consécutifs forme un créneau avec début et fin (au format hhmm)
        a = map(int, raw_input().split())
        
        # On parcourt les k créneaux
        for j in range(k):
            # a[::2] récupère tous les éléments pairs de a (heures de début)
            # a[1::2] récupère tous les éléments impairs (heures de fin)
            
            # On convertit chaque heure de début de créneau en minutes pour l'indice de début
            start = cv(a[::2][j])
            # On convertit chaque heure de fin de créneau en minutes pour l'indice de fin
            end = cv(a[1::2][j])
            
            # On marque toutes les minutes du créneau comme occupées pour cette personne :
            # On parcourt chaque minute du créneau (for l in range(start, end))
            for l in range(start, end):
                # On incrémente la valeur de v[l], signifiant qu'une personne occupe cette minute
                v[l] += 1
    
    # Initialisation de deux variables pour la recherche du maximum :
    # m pour mémoriser le maximum de minutes consécutives disponibles
    m = 0
    # c pour compter la longueur courante d'une série de minutes non prises par tous (v[i] < n)
    c = 0
    
    # On convertit p (heure de début de la plage de recherche) en index de minute grâce à cv(p)
    # Même chose pour q (heure de fin de la plage)
    for i in range(cv(p), cv(q)):
        # Si la minute i n'est pas occupée par tout le monde (v[i] < n), on incrémente c
        # Sinon (au moins une personne occupe cette minute), on remet c à 0
        if v[i] < n:
            c = c + 1
        else:
            c = 0
        # On compare et retient le maximum obtenu jusqu'ici dans m
        m = max(m, c)
    
    # On affiche le résultat : la plus longue séquence de minutes consécutives
    # durant lesquelles au moins une personne est libre pendant la plage [p, q[
    print m