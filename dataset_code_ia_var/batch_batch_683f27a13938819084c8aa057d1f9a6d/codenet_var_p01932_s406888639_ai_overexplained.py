# Début du programme : AOJ 2832 All Japan Association of Return Home
# Le programme lit des entrées, effectue des calculs, puis imprime un résultat basé sur certaines conditions.

# Lecture de deux entiers depuis l'entrée standard, séparés par un espace
# n : nombre d'éléments ou d'événements à traiter
# d : une limite maximale associée à une contrainte (par exemple, capacité maximale)
n, d = map(int, input().split())

# Initialisation de plusieurs variables :
# ans : accumule ou garde la réponse finale calculée (ex : coût, temps total, etc.), initialisée à 0
# t0 : stocke la valeur précédente du temps (ou de la première coordonnée), initialisée à 0
# f0 : stocke la valeur précédente de f (par exemple, emplacement), initialisée à 0
# num : nombre d'éléments consécutifs traités (compteur pour le groupe courant), initialisé à 0
ans = 0
t0 = 0
f0 = 0
num = 0

# Boucle for pour traiter chaque événement ou chaque entrée, i s'incrémente de 0 à n-1
for i in range(n):
    # Lecture de deux entiers depuis l'entrée standard à chaque itération
    # t : moment ou temps de l'ième entrée (par exemple, temps d'arrivée)
    # f : position, lieu ou étage de l'ième entrée (par exemple, étage d’arrivée)
    t, f = map(int, input().split())
    
    # Correction de l'indice de f
    # Comme les indices commencent à 1 dans l'entrée mais à 0 dans le programme, on enlève 1 à f
    f -= 1
    
    # Calcul du déplacement entre la position actuelle (f) et la précédente (f0)
    # df sera positif si déplacement vers un étage supérieur
    # df sera négatif si déplacement vers un étage inférieur
    df = f - f0
    
    # Si df est négatif (descente d'étages), le rendre positif (distance absolue)
    if df < 0:
        df = -df

    # Calcul du temps passé depuis la dernière entrée
    dt = t - t0

    # Vérification que l'on peut se déplacer en temps dt d'une position à une autre (cf contrainte du problème)
    # Si le temps passé depuis la dernière entrée est strictement inférieur à la distance parcourue,
    # cela signifie que ce déplacement est impossible, on écrit -1 comme résultat et on interrompt le programme
    if dt < df:
        ans = -1         # Marquer comme erreur
        break            # Sortir prématurément de la boucle principale

    # Condition : si le temps écoulé est plus large que la somme des positions actuelle et précédente (f0 + f)
    # Cela vérifie si l'intervalle permet une certaine opération (par exemple, tout déplacer en bloc)
    if dt >= f0 + f:
        # Ajoute au total la valeur courante de num (nombre de personnes/groupe en attente) multipliée par f0 (étage précédent)
        # Cela peut modéliser le fait que chacun doit déplacer quelque chose depuis l'ancien étage
        ans += num * f0

        # Remise à zéro du compteur d’individus/groupe, car ils ont été déplacés ou servis
        num = 0
    else:
        # Cas où on ne peut pas tout traiter d’un coup, donc on voit si la capacité n’est pas dépassée

        # Si le fait d’ajouter une nouvelle entité dépasserait la capacité maximale d (contrainte du problème)
        if num + 1 > d:
            ans = -1     # Erreur : impossible compte tenu des contraintes
            break        # Arrêt du traitement

        # Sinon, ajouter au total la valeur de num multipliée par le temps écoulé
        ans += num * dt

    # Mise à jour des variables pour la prochaine itération :
    # f0 : devient f, c’est-à-dire la nouvelle position de référence
    # t0 : devient t, c’est-à-dire le nouveau temps de référence
    f0, t0 = f, t

    # Incrémentation du nombre d'entités/groupe en attente ou à traiter
    num += 1

# Une fois la boucle terminée (traitement terminé ou interrompu plus tôt),
# on vérifie si une erreur a été rencontrée (ans < 0), on imprime -1, sinon le calcul finalisé

# Comme la dernière opération peut laisser quelques entités/groupe non traitées,
# on ajoute num * f0 au total pour traiter ce reste
if ans < 0:
    print(-1)
else:
    print(ans + num * f0)