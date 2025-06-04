N, M, K = map(int, input().split())
A, B, C = map(int, input().split())
T = int(input())
S = [int(input()) for _ in range(M)]

# On va définir une fonction pour calculer le nombre maximal de stations atteignables
# en choisissant K arrêts de semiexpress, qui doivent inclure tous les arrêts express.

# Idée simple:
#  - Les arrêts express sont forcés.
#  - Il faut choisir (K - M) arrêts supplémentaires parmi les stations entre 1 et N
#    (hors celles déjà dans S), pour minimiser le temps pour atteindre un maximum de stations.
#  
# Approche basique:
#  - On peut penser que placer les arrêts semiexpress de manière uniforme entre les arrêts express maximise la couverture.
#
#  - On considère que tous les arrêts semiexpress sont sur la liste "all_stops" = S + (K - M) stations
#    placées dans les intervalles entre arrêts express.
#
#  - Comme N peut être grand, on ne peut pas manipuler toutes les stations.
#
#  - On essaie une solution naïve:
#    On suppose que les K arrêts sont choisis pour répartir le plus possible les arrêts semiexpress
#    entre les arrêts express de sorte que la distance maximale entre arrêts semiexpress soit la plus petite possible.
#
# Ensuite on calcule, en partant du station 1, la longueur max atteignable avec T minutes en utilisant le train le plus rapide
# disponible entre les arrêts : express (time B), semiexpress (time C), local (time A).
#
# Comme les temps sont constants entre stations, on peut calculer les temps cumulés facilement.

# Explications supplémentaires:
# - Les trains locaux s'arrêtent partout, donc on peut toujours marcher de station en station à vitesse A.
# - Les trains express et semiexpress s'arrêtent seulement à leurs arrêts respectifs.
# - On peut changer de train à toutes les stations arrêtées.
# - La vitesse des trains : B < C < A (express est plus rapide que semiexpress, plus rapide que local)

# Pour simplifier, on considère les stations en segments entre les arrêts des trains (express, semiexpress).

# Étapes :
# 1. Construire la liste des arrêts semiexpress:
#    - Elle contient toutes les express stops S.
#    - Ajouter (K - M) stations supplémentaires entre 1 et N.
#    - On place ces arrêts supplémentaires de façon équidistante entre les arrêts express.
# 2. Trier la liste des arrêts semiexpress.
# 3. Calculer le temps cumulatif minimal pour atteindre chaque arrêt semiexpress depuis 1.
#    - Le temps entre arrêts de semiexpress est (distance en stations) * C
#    - Le temps entre arrêts express est (distance en stations) * B
#    - Mais on peut combiner trains. Pour cette solution simple, on suppose que le trajet
#      se fait en combinant local, express et semiexpress, par transfert.

# Pour rendre le problème plus simple:
# - On suppose que le trajet optimal commence par les arrêts express et semiexpress,
#   en sautant entre les arrêts les plus rapides possible,
#   puis on fait local jusqu'à la station cible (si besoin).

# On va calculer pour chaque station i:
#  - Le temps minimal pour arriver à i en utilisant cette décomposition.
#  - Comme N est trop grand, on ne peut pas itérer sur toutes les stations.
#  - On calcule donc par segment entre arrêts semiexpress.

# Nous allons simplement calculer le nombre maximal de stations atteignables en temps T
# en simulant les arrêts semiexpress placés.

def compute_max_stations(N, M, K, A, B, C, T, S):
    S.sort()
    semiexpress = list(S)  # contient M arrêts express d'abord
    
    # Nombre d'arrêts semiexpress à ajouter
    remain = K - M
    
    # On va distribuer ces remain arrêts dans les intervalles entre arrêts express
    
    # Intervalles entre arrêts express : M-1 intervalles
    intervals = []
    for i in range(M - 1):
        length = S[i+1] - S[i]
        intervals.append((length, i))  # length de l'intervalle et index
    
    # Pour chaque intervalle on va ajouter un nombre d'arrêts proportional à sa longueur
    total_length = sum(interval[0] for interval in intervals)
    added = [0] * (M -1)
    
    # distribution brute et simple
    for i in range(M -1):
        added[i] = (intervals[i][0] * remain) // total_length
    allocated = sum(added)
    leftover = remain - allocated
    # Répartir les restes
    for i in range(leftover):
        added[i] += 1

    # Maintenant on ajoute les arrêts semiexpress dans chaque intervalle
    for i in range(M -1):
        start = S[i]
        end = S[i+1]
        cnt = added[i]
        # On veut cnt arrêts entre start et end (exclus), les espacer aussi équitablement que possible
        if cnt == 0:
            continue
        gap = (end - start) / (cnt +1)
        for j in range(1, cnt +1):
            pos = int(start + j * gap)
            # éviter d'ajouter un arrêt qui est déjà présent
            if pos not in semiexpress and 1 < pos < N:
                semiexpress.append(pos)
    
    semiexpress = list(set(semiexpress))
    semiexpress.sort()
    
    # Maintenant on a K arrêts semiexpress avec K = len(semiexpress)
    # On va calculer le temps minimal pour atteindre chaque arrêt semiexpress depuis 1 :
    # On suppose qu'entre arrêts semiexpress on roule en semiexpress à vitesse C
    # et on peut changer de train aux arrêts (incluant express et semiexpress)
    # Donc pour atteindre un arrêt semiexpress i:
    # On calcule le cumul des temps entre arrêts semiexpress depuis 1
    time_at_stop = [0]  # temps pour atteindre semiexpress[0] = station 1
    
    for i in range(1, len(semiexpress)):
        dist = semiexpress[i] - semiexpress[i-1]
        time = time_at_stop[i-1] + dist * C
        time_at_stop.append(time)
    
    # Pour les stations qui ne sont pas arrêts semiexpress, on peut :
    # - atteindre leur dernier arrêt semiexpress antérieur
    # - puis prendre local train (temps A par station) jusqu'à la station ciblée
    
    # On veut compter combien de stations i, 2 <= i <= N, ont un temps <= T

    # Comme N est grand, on va itérer sur les segments entre arrêts semiexpress
    result = 0
    for i in range(len(semiexpress)):
        start_station = semiexpress[i]
        start_time = time_at_stop[i]
        if i == len(semiexpress) -1:
            end_station = N + 1
        else:
            end_station = semiexpress[i+1]
        
        # On regarde sur l'intervalle [start_station, end_station -1]
        # Pour chaque station s dans cette intervalle on calcule
        # time_to_s = start_time + (s - start_station)*A
        # On veut que time_to_s <= T <=> s <= (T - start_time)/A + start_station
        
        max_reach = (T - start_time)//A + start_station
        if max_reach >= end_station -1:
            # On peut atteindre tous les stations de cet intervalle sauf peut être start_station (car c est un arrêt)
            cnt = (end_station - start_station -1)
            # On ne compte pas start_station si c=1
            if start_station != 1:
                cnt += 1
        else:
            if max_reach >= start_station:
                cnt = max_reach - start_station + 1
            else:
                cnt = 0
        result += cnt
    
    # result correspond au nombre de stations >=2 atteignables sous T
    return result

ans = compute_max_stations(N, M, K, A, B, C, T, S)
print(ans)