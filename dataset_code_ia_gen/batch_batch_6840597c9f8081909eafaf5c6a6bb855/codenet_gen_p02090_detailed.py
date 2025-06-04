import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# Problème : Homura-chan doit manger tous les yokans situés sur un segment [0, M]
# en effectuant des allers-retours entre 0 et M. Elle peut manger un yokan en le parcourant
# intégralement du côté gauche (L_i) vers le côté droit (R_i) si elle est en direction positive,
# ou de droite (R_i) vers gauche (L_i) si elle est en direction négative.
# Elle ne peut manger qu'un yokan à la fois, sans s'interrompre.
# On cherche la distance minimale parcourue pour manger tous les yokans.

# Approche :
# - Classer les yokans selon leur position sur la ligne.
# - On modélise le problème en une programmation dynamique sur la séquence des yokans triés 
#   par leur position. Chaque yokan peut être mangé soit dans le sens gauche->droite (positive), 
#   soit dans le sens droite->gauche (negative).
# - On définit dp[i][d], la distance minimale pour avoir mangé les i premiers yokans,
#   en se positionnant après avoir mangé le i-ème yokan dans la direction d 
#   (d=0 -> à la position R_i si on a mangé de L_i vers R_i,
#    d=1 -> à la position L_i si on a mangé de R_i vers L_i).
# - On initialise dp[0][0] et dp[0][1] depuis la position initiale 0 avec direction positive.
# - On calcule ensuite la transition entre le i-1 et i en considérant 
#   le sens d'où on vient et celui où on va.
# - La réponse finale est min(dp[N-1][0], dp[N-1][1])

# Remarque importante :  
# - la direction du déplacement n'est pas libre ; c'est un mouvement de navette entre 0 et M.
# - Toutefois, on peut modéliser les déplacements nécessaires car Homura peut changer de direction 
#   uniquement aux extrémités 0 ou M.
# - Donc, pour aller d'une position x1 avec direction d1 à une position x2 avec direction d2, 
#   on doit compter la distance minimale avec les allers-retours obligatoires.

# Calcul de la distance entre deux points avec direction :
# - La direction positive signifie se déplace vers M.
# - La direction négative signifie vers 0.
# Si on part de position pos1 en direction dir1 (0=positive), on veut arriver
# à pos2 en ayant la direction dir2 (0=positive).

# Cette fonction calcule la distance minimale nécessaire pour aller de (pos1, dir1) à (pos2, dir2)
# en respectant la contrainte d'aller-retour aux bornes (0 ou M).
def dist_move(pos1, dir1, pos2, dir2, M):
    # Si les directions sont égales
    if dir1 == dir2:
        # Si la direction est positive (0), on doit avancer vers M
        # On peut aller directement si pos2 >= pos1, sinon on doit revenir à 0 puis remonter
        if dir1 == 0:
            if pos2 >= pos1:
                return pos2 - pos1
            else:
                # Aller à M, rebrousser chemin (aller & retour)
                return (M - pos1) + (M - pos2)
        else:
            # direction négative, mouvement vers 0
            if pos2 <= pos1:
                return pos1 - pos2
            else:
                # Aller à 0, rebrousser chemin (aller & retour)
                return pos1 + pos2
    else:
        # Si les directions diffèrent, on doit aller à l'extrémité opposée aux deux pour changer
        # Par exemple, de positive à négative, on doit obligatoirement aller à M puis revenir
        # La distance est: aller à extrémité qui inverse la direction + aller à la destination
        if dir1 == 0 and dir2 == 1:
            # part de pos1 (direction positive), arrive à pos2 (direction négative)
            return (M - pos1) + (M - pos2)
        else: 
            # part de pos1 (direction négative), arrive à pos2 (direction positive)
            return pos1 + pos2

def main():
    N, M = map(int, input().split())
    yokans = [tuple(map(int, input().split())) for _ in range(N)]

    # On trie les yokans par position L_i pour organiser la visite
    yokans.sort(key=lambda x: x[0])

    # dp[i][d] : distance minimale après avoir mangé le i-ème yokan,
    #            en finissant à l'extrémité correspondante selon direction d
    # d=0 : on finit à R_i (mangé de L_i à R_i, direction positive)
    # d=1 : on finit à L_i (mangé de R_i à L_i, direction négative)
    INF = 10**18
    dp = [[INF]*2 for _ in range(N)]

    # Calculer la distance initiale pour le premier yokan
    L0, R0 = yokans[0]

    # Homura commence à 0 en direction positive (0)
    # Elle peut commencer à manger le premier yokan soit dans le sens gauche->droite
    # Elle doit rejoindre le point de départ (L0) en direction positive
    # puis parcourir le yokan:
    # Manger dans le sens positif (L0->R0) : il faut arriver à L0 en direction à 0,
    # puis parcourir (R0 - L0)
    # Distance départ -> L0 (direction positive): pos1=0 dir1=0 pos2=L0 dir2=0
    dist_to_L = dist_move(0, 0, L0, 0, M)
    dp[0][0] = dist_to_L + (R0 - L0) # manger yokan dans le sens positif

    # Manger dans le sens négatif (R0->L0) : il faut arriver à R0 en direction négative,
    # puis parcourir (R0 - L0)
    dist_to_R = dist_move(0, 0, R0, 1, M)
    dp[0][1] = dist_to_R + (R0 - L0) # manger yokan dans le sens négatif

    # Traiter les autres yokans
    for i in range(1, N):
        L, R = yokans[i]
        L_prev, R_prev = yokans[i-1]

        for prev_dir in range(2):
            # position actuelle du yokan i-1 apres avoir mangé:
            pos_prev = R_prev if prev_dir == 0 else L_prev

            for curr_dir in range(2):
                # position de départ du yokan i pour l'état curr_dir (où on finit)
                # on doit commencer à la bonne extrémité pour manger dans ce sens:
                start_curr = L if curr_dir == 0 else R
                # parcours du yokan (toujours la même longueur)
                length = R - L

                # Calculer la distance pour aller de (pos_prev, prev_dir) à (start_curr, curr_dir)
                d = dist_move(pos_prev, prev_dir, start_curr, curr_dir, M)

                # Ajouter le parcours du yokan (length)
                new_dist = dp[i-1][prev_dir] + d + length

                if new_dist < dp[i][curr_dir]:
                    dp[i][curr_dir] = new_dist

    # La réponse est la distance minimale après avoir mangé tous les yokans, peu importe la fin
    ans = min(dp[N-1])
    print(ans)

if __name__ == '__main__':
    main()