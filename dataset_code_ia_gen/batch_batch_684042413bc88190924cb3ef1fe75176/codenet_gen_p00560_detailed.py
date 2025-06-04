import sys
import bisect

# Lecture des données d'entrée
N, M, K = map(int, sys.stdin.readline().split())
A, B, C = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())

# Lecture des stations où l'express s'arrête (triées)
S = [int(sys.stdin.readline()) for _ in range(M)]

# L'idée principale est d'utiliser une programmation dynamique sur les arrêts de semiexpress train.
# On sait que semiexpress doit s'arrêter sur toutes les stations d'express,
# et aussi à K stations au total (K >= M).
# Les arrêts de semiexpress sont un sous-ensemble de stations (numérotées entre 1 et N),
# contenant obligatoirement S_1,...,S_M, et de taille K.
#
# Nous devons choisir les K stations (avec les M stations fixes déjà choisies) pour minimiser
# les temps de trajet en utilisant une combinaison d'express, semiexpress et local,
# pour maximiser le nombre de stations accessibles dans T minutes.
#
# Le graphe est simple: stations numérotées en ordre croissant,
# voyages toujours dans le sens croissant de stations.
#
# Transferts sont possibles en stations d'arrêt communes.
#
# Les trains ont temps de parcours spécifiques par segment:
# local: A minutes / segment
# express: B minutes / segment
# semiexpress: C minutes / segment
#
# Trouver l'ensemble des arrêts du semiexpress implique de choisir (K - M) stations supplémentaires 
# entre les arrêts express pour que la durée la plus courte pour aller jusqu'à une station i soit <= T.
#
# On modélise ainsi:
# - On sépare la ligne en segments entre express stops S[i], S[i+1].
# - Dans chaque segment, on va choisir x arrêts de semiexpress en plus des 2 arrêts express (les extrémités du segment),
#   total des arrêts dans le segment = x + 2.
# - Le nombre total d'arrêts semiexpress sur toute la ligne est K.
# - Le nombre d'arrêts semiexpress imposées est M (les express stops).
# - Il faut donc ajouter (K - M) arrêts entre les segments.
# - Le voyage avec semiexpress s'effectue en segments entre arrêts semiexpress,
#   chaque segment a un coût en temps : 
#     segment_distance * C (temps semiexpress)
# - On peut faire aussi transfert à chaque arrêt : possibilité de changer de train.
#
# Le calcul du temps depuis la station 1 à une station i est donc la somme des temps 
# entre arrêts semiexpress sur le trajet, plus éventuellement du local à côté.
#
# Pour maximiser le nombre de stations accessibles, il faut maximiser la couverture (station reachable within T).
#
# On va donc considérer les arrêts semiexpress comme à répartir entre les M-1 intervalles entre arrêts express:
# Chaque intervalle [S[i], S[i+1]] comprend (S[i+1] - S[i]) stations.
#
# Si on divise cet intervalle en segments par arrêts semiexpress,
# l'intervalle est découpé en (number of semiexpress stops in interval - 1) segments,
# chaque segment a une longueur en stations.
#
# Par vide, choisir plus de stops = découper segments en parties plus petites,
# réduisant la somme des segments * C, donc le temps en semiexpress.
#
# Détaillons:
# - On fixe où choisir les arrêts semiexpress dans chaque intervalle.
# - Pour chaque intervalle, le temps minimum pour se rendre à une station dans l'intervalle dépend de la distance jusqu'à cette station,
#   des arrêts semiexpress (car on mesti voyager entre arrêts semiexpress par train semiexpress)
#   et de la possibilité de changer entre express et semiexpress.
#
# Simplification:
# Avec un nombre donné de stops dans un intervalle, on peut calculer la vitesse moyenne semiexpress efficace pour ce segment.
#
# L'approche efficace:
# - On note que sur le trajet 1->station i, on peut aussi passer par express train sur les arrêts fixes (coût B par segment entre S stops)
# - On inclut les arrêts semiexpress entre les arrêts express, ce qui permet de "couper" un segment long en plusieurs petits segments, chacun qui coûtent C par segment plus court.
#
# Ainsi, pour chaque intervalle entre S_i et S_{i+1}, de longueur d := S_{i+1} - S_i,
# on peut choisir x_i >= 1 arrêts semiexpress au total pour ce segment (car aux extrémités on a déjà les arrêts express, qui sont aussi stops semiexpress).
#
# Le total des arrêts semiexpress est K, donc la somme des x_i sur i = 0..M-2 est K.
#
# Le temps pour traverser ce segment entre deux arrêts semiexpress consécutifs est : (segment_length_part) * C.
#
# Pour accéder à une station située à une distance d' desde S_i, 
# on projette les stations comme divisées en (x_i - 1) segments égales (en nombre d'intervalles),
# chaque segment de longueur approx floor(d / (x_i - 1)) ou ceil(d / (x_i - 1)).
#
# Le temps minimum pour atteindre la station k dans ce interval dépend de la minimal segment qu'elle est dans + le minimal local train usage.
#
# On a aussi le train express avec vitesse B entre stops S_i.
#
# Pour les stations avant le premier semiexpress stop dans l'intervalle, on peut voyager local (coût A).
#
# L'objectif final est de calculer pour un choix donné de arrêts semiexpress par intervalle,
# combien de stations peuvent être atteintes sous le temps T.
#
# Cette solution est compliquée mais on peut faire une recherche binaire sur la distance atteignable avec un choix de arrêts semiexpress,
# car le temps minimal pour accéder à une station i est monotone croissant en station i.
#
# Solution détaillée dans l'éditorial du problème JOI 2016: 
# On fait une recherche binaire sur la station maximale atteignable i_max,
# et on vérifie si on peut choisir les arrêts semiexpress (respectant contraintes)
# telle que le temps pour atteindre la station i_max est ≤ T.
#
# Vérifier la condition est possible avec un DP en O(M*K), grâce à la taille limitée des arrêts express M <= K <= 3000.
#
# Comme N peut être très grand (jusqu'à 10^9), on fait binaire sur station reachable (entre 1 et N),
# pour trouver la plus grande station possible.
#
# Implementation en résumé:
# 1) Recherche binaire sur la station max à atteindre.
# 2) Pour une station x testée, on teste si temps minimal ≤ T possible en choisissant les arrêts semiexpress.
# 3) DP sur arrêts express et arrêts semiexpress.
#
# Les temps sur les intervalles sont calculés avec les segments coupés en stops semiexpress,
# le temps minimal pour aller jusqu'à un point est en simple formule.
#
# On code.

def can_reach(station_limit):
    # Vérifie si on peut atteindre la station station_limit en ≤ T minutes
    # en choisissant les arrêts semiexpress.
    #
    # DP sur arrêts express, où dp[i][j] = le temps minimal pour atteindre S[i]
    # en ayant utilisé j arrêts semiexpress jusqu'à S[i].
    #
    # Ici, les arrêts semiexpress choisis sont au minimum les M arrêts express fixes (incluant les extrêmes),
    # et on doit choisir (K - M) arrêts supplémentaires répartis sur intervalles.
    # On suppose un arrêt semiexpress aux points S[i], donc les arrêts supplémentaires dans chaque intervalle.

    # Notation:
    # intervals: segment i = [S[i], S[i+1]] de longueur d_i = S[i+1]-S[i]
    # pour chaque intervalle, on choisit x_i stops semiexpress (≥1), 
    # avec sum x_i = K

    # On trouve la position p du station_limit dans les arrêts express S par bisect:
    # station_limit peut être avant ou dans un intervalle, on va traiter jusqu'à intervalle contenant station_limit.

    # On effectue dp[i][j]: minimal temps pour atteindre S[i] en utilisant j arrêts semiexpress au total.
    # On construit dp sur i and j.

    # On modifie légèrement la méthode.

    # On va stocker un tableau expr[i]: stations S[i]
    # Et traiter en intervalles.

    # On prépare un tableau permettant d'avoir d_i = longeur des intervalles

    # max dp dimension: M x (K+1)

    # Le nombre total d'arrêts semiexpress = K, déjà M fixes, donc (K - M) supplémentaires à répartir

    # Préalable: on sait que les arrêts express sont aussi des arrêts semiexpress obligatoires:
    # Cela signifie que les arrêts semiexpress dans chaque intervalle i >= 1 (car 2 arrêts fixes aux extrémités),
    # nombre d'arrêts dans intervalle i ≥ 2 (minimale), puisque 2 arrêts fixes.

    # Correction sur notation: dans l’énoncé, M arrêts express (stations S1 to SM), 
    # ces stations sont arrêts de semiexpress.
    # Nombre total arrêts semiexpress K ≥ M.

    # Donc pour chaque intervalle i, nombre d’arrêts semiexpress dans intervalle i peut être >2 si on en rajoute.

    # On définit pour chaque intervalle le nombre de segments = nombre d’arrêts semiexpress dans intervalle i - 1

    # Pour un intervalle de distance d, coupé en s segments, le temps pour traverser un segment est ≤ segment_length * C

    # On veut minimiser le temps pour arriver à une station x ≤ station_limit.

    # On va approximer:
    # Dans l’intervalle on ne peut pas distinguer la position exacte de station_limit.

    # On ajoute dans le dernier intervalle le calcul spécial, car station_limit peut être à l’intérieur.

    # Implémentation du DP:

    # dp[i][j] = minimal total time pour atteindre S[i] en utilisant j arrêts semiexpress (parmi lesquels les i arrêts express fixes).

    # Base: dp[0][M] = 0 (car station 1, l’arrêt express de départ, déjà arrêts semiexpress minimum)

    # Pour i in range(M-1), on essaye toutes allocations x des arrêts semiexpress sur l’intervalle (x ≥ minimal 2)
    # On a (K - M) arrêts supplémentaires à répartir.

    # Mais pour optimiser, on fait dp[i+1][j+x-1] = min(
    #   dp[i][j] + cost(interval i, x arrêts semiexpress dans cet intervalle, station_limit?)
    # )

    # Définition de cost(interval, x, station_limit_in_interval):
    # Calcule le temps maximal nécessaire pour traverser l’intervalle i
    # jusqu'à la station station_limit si elle est dedans;
    # sinon temps total pour traverser l’intervalle.

    # On doit gérer le cas où station_limit est dans cet intervalle.

    # PSEUDO-CODE RAISONNEMENT:

    # Finalement le problème demande combien de stations i≥2 sont atteignables ≤ T.

    # On fait une recherche binaire sur le nombre de stations atteignables.

    # Enfin on code.

    # -----------------------------

    # Trouver l’intervalle où station_limit se trouve:
    idx = bisect.bisect_right(S, station_limit) -1
    # idx entre 0 et M-1 (segment contenant station_limit)
    # si station_limit == S[idx], la station est à l’arrêt express, donc on peut directement prendre semiexpress express.

    # On pré-calcul les distances d_i entre arrêts express
    intervals = [S[i+1] - S[i] for i in range(M-1)]

    # dp: taille M x (K+1), initialisé à grand nombre
    INF = 10**20
    dp = [[INF]*(K+1) for _ in range(M)]
    # A S[0] (station 1), on a déjà M arrêts semiexpress fixes,
    # donc dp[0][M] = 0
    dp[0][M] = 0

    # Fonction pour calculer temps sur un intervalle i en fonction du nombre d'arrêts semiexpress x
    # et la station limite dans cet intervalle (si dans intervalle)

    def cost(i, x, endpoint):
        """
        Calculate the minimal time to reach station endpoint in the i-th interval [S[i], S[i+1]] 
        given x semiexpress stops in this interval,
        including the fixed stops at S[i] and S[i+1].

        x >= 2 (because S[i], S[i+1] fixed), so number of segments = x-1
        segments are equally split intervals: length = intervals[i] / (x-1)

        endpoint: the position of station_limit if is > S[i] and ≤ S[i+1],
                  otherwise endpoint = None meaning full interval to S[i+1]

        Returns minimal time needed to reach endpoint from S[i] with stops semiexpress.

        The travel time is sum of segments * C

        However, to reach station inside the segment, we can combine semiexpress segments and local train.

        Local train cost per segment A > C > B.

        So the minimal time to reach station k is minimal over:
        - using semiexpress between semiexpress stops + local in last segment

        We approximate by:
        - Cutting interval i in segments of length segment_length = intervals[i] // (x-1)
        - station_offset = endpoint - S[i]

        We find in which segment station_offset falls:
        segment index s = (station_offset -1) // segment_length
        then distance from start of this segment to station_offset is:
        last_segment_length = station_offset - s*segment_length

        The time is:
        time to pass s segments with semiexpress = s * segment_length * C
        + time to pass last part by local = last_segment_length * A

        (car on last sub-segment on peut quitter semiexpress pour local)

        En cas où interval_length % (x-1) != 0, les segments ne sont pas égales,
        la division en floor ci-dessus reste une bonne approximation conservatrice.

        """
        d = intervals[i]
        segments = x -1
        segment_length_base = d // segments
        remainder = d % segments

        # Construction du tableau segment_lengths des segments:
        # Les premiers remainder segments ont 1 élément de plus
        segment_lengths = [segment_length_base+1 if j < remainder else segment_length_base for j in range(segments)]

        if endpoint is None:
            # On couvre tout l’intervalle, donc temps total = d * C (en semiexpress)
            return d*C

        # station_offset = endpoint - S[i]
        station_offset = endpoint - S[i]

        # Trouver dans quel segment la station_offset se trouve
        cumu = 0
        seg_idx = 0
        while seg_idx < segments and cumu + segment_lengths[seg_idx] < station_offset:
            cumu += segment_lengths[seg_idx]
            seg_idx +=1

        # seg_idx est le segment contenant station_offset
        # Longueur du dernier segment à parcourir en local:
        last_seg_local_len = station_offset - cumu

        # Time = temps semiexpress pour segments complètes + local sur dernier segment
        time = seg_idx * C * 0  # initialisation, on multiplie par 0 faute de relecture (corriger)
        # correction: temps pour segments complètes = somme longueur segments * C
        # segments complètes = cumu stations parcourues en semiexpress
        time = cumu * C + last_seg_local_len * A
        # On ajoute aussi les segments accèdant au segment: c'est cumu (nombre de stations dans segments complétés)

        return time

    # Dans DP, pour chaque intervalle on essaie de répartir arrêts semiexpress supplémentaires
    # x_i dans [2..interval_length+1], mais attention: x_i ≤ stations dans l’intervalle + 1

    # Or arrêts semiexpress maximum par intervalle ≤ stations dans cet intervalle +1

    # En pratique, l’intervalle entre S[i] et S[i+1] contient intervals[i] stations.

    # Le maximum de arrêts semiexpress dans un intervalle ne peut excéder intervals[i] +1.

    # On réalise que K ≤ 3000 donc on peut limiter x dans [2..intervals[i]+1], mais intervals[i] peut être grand.

    # Pour limiter, on fixe x dans [2..max_x], max_x = min(K, intervals[i]+1)

    # On implémente.

    for i in range(M-1):
        for used_stops in range(M, K+1):
            if dp[i][used_stops] == INF:
                continue
            # Max stops dans interval
            max_x = min(K - used_stops + 1 + 1, intervals[i] + 1)
            # x ≥ 2 minimum car on a S[i] et S[i+1]
            # On augmente de 0 à max_possible forcément
            for x in range(2, max_x+1):
                nxt_j = used_stops + x -1
                if nxt_j > K:
                    break
                # Calcul cout interval:
                # Si interval i == idx (où se trouve station_limit), on restreint à station_limit
                if i == idx:
                    costc = cost(i, x, min(station_limit, S[i+1]))
                elif i < idx:
                    costc = cost(i, x, None)
                else:
                    # Intervalle après station_limit, on pas besoin d’aller au delà
                    # On ne traite pas, mais pour la continuité on force gros cout
                    costc = INF

                val = dp[i][used_stops] + costc

                if val < dp[i+1][nxt_j]:
                    dp[i+1][nxt_j] = val

    # Maintenant à la fin, pour la dernière station S[M-1] = station N,
    # on cherche le minimum dp[M-1][j] où j en M..K et si S[M-1] ≥ station_limit

    # S[M-1] est station N, toujours ≥ station_limit (car station_limit ≤ N)

    for stops_used in range(M, K+1):
        if dp[M-1][stops_used] <= T:
            # Ici, station_limit coincide ou est au max possible
            return True