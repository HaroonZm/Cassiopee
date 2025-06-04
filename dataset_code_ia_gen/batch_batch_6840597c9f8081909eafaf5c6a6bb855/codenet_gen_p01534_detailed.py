# Solution complète pour le problème Anipero 2012

# Approche :
# - On a n chansons successives, chacune dure 5 minutes.
# - On dispose au départ de m sairyums (bâtons lumineux).
# - Au début de chaque chanson, on peut décider combien de nouveaux sairyums on casse (on "fold")
#   et on ne peut pas casser plus que ce qu'on possède encore.
# - Chaque sairyum éclairera soit au niveau 2 pendant 5 minutes (donc pour la chanson actuelle),
#   soit au niveau 1 pendant les 5 minutes suivantes.
# - Puisqu'une chanson dure 5 minutes, et que la luminosité baisse après 5 minutes,
#   les sairyums cassés au début de la chanson i seront au niveau 2 pendant cette chanson,
#   puis au niveau 1 pendant la chanson i+1.
# - On ne peut pas changer le nombre de sairyums en cours de chanson.
# - Max 8 sairyums peuvent être secoués simultanément lors d'une chanson.
# - On peut aussi décider de ne pas secouer de sairyum dans une chanson : dans ce cas, 
#   on a une satisfaction c_i spécifique par chanson.
# - Objectif : répartir les m sairyums cassés au début des différentes chansons pour maximiser la satisfaction totale.

# Modélisation dynamique :
# - On va modéliser avec un DP d'état (chanson i, nombre de sairyums cassés restants m_rest, nombre de sairyums nous arrivant en niveau 1 cette chanson)
# - En effet, les sairyums cassés à la chanson i-1 éclaireront au niveau 1 à la chanson i.
# - A la chanson i, on casse k sairyums (0 <= k <= min(m_rest, 8) car on peut secouer max 8 sairyums et on ne peut pas secouer plus que ce qu'on casse cette chanson).
# - On décide combien d'entre ceux au niveau 1 (appelons cela l) on secoue.
# - On prendra x sairyums niveau 2 (k cassés à cette chanson), et y sairyums niveau 1 disponibles (venant de la chanson précédente).
# - Le total secoué ne peut pas dépasser 8.
# - Si on ne secoue pas de sairyum, on prend satisfaction c_i.
# - Sinon, satisfaction = a_i * nombre niveau 2 + b_i * nombre niveau 1.
# - Les sairyums niveau 1 qui ne sont pas secoués restent pour la chanson suivante ?
#   NON, selon l'énoncé, une fois que le sairyum est cassé, il ne peut pas être remis de côté.
#   Cependant, comme la lumière se perd au bout de 10 minutes, on ne peut pas reporter plus tard.
#   Le problème indique que lorsqu'on décide de secouer un sairyum, il l'est durant tout la chanson.
#   Le reste (non secoué) ne compte pas pour la satisfaction, mais on ne peut pas remettre en réserve des sairyums.
# - En réalité, la contrainte impose que les sairyums qui éclairent au niveau 1 proviennent uniquement des sairyums cassés la chanson précédente et qui n'ont pas été secoués la précédente chanson (ce qui est impossible). Donc on doit considérer que les sairyums cassés la chanson i éclaire niveau 2 cette chanson i et niveau 1 la chanson i+1.
# - On a donc besoin de conserver le nombre de sairyums niveau 1 utilisés cette chanson (issus de la chanson précédente).
# - Ainsi on a 3 variables d'état : chanson i, nombre sairyums restants m_rest, et nombre sairyums niveau 1 disponibles level1_avail.
# - Par définition, level1_avail correspond au nombre de sairyums restant de la chanson précédente au niveau 1.
# - Les sairyums niveau 1 disponibles à la chanson i sont ceux cassés à la chanson i-1 moins ceux utilisés la chanson i-1.
# - Or on a une confusion : l'énoncé ne dit pas que les sairyums niveau 1 se perdent si on ne les utilise pas, mais la dernière contrainte est "Une fois qu'on a décidé de secouer un sairyum, on ne peut pas changer pendant la chanson", et on ne peut pas les utiliser plus d'une fois.
# - Donc on va considérer que tous les sairyums cassés sont utilisés directement la chanson où ils sont cassés (level 2), et pour la chanson suivante (level 1), on a les sairyums cassés la chanson précédente, qui éclairent en niveau 1 pour la chanson suivante.
# - Par conséquent, lors de la chanson i, on peut secouer :
#   - k sairyums niveau 2 cassés à la chanson i
#   - l sairyums niveau 1 provenant de la chanson i-1
# - Mais on n'a jamais utilisé les sairyums niveau 1 lorsque l'on secoue au niveau 2, donc  il n'y a pas conflit.
# - Cette modélisation DP apporte un état à 3 dimensions : i, m_rest, level1_avail.
# - Pour chaque état, on essaie toutes les combinaisons possibles k (0 to min(8,m_rest)), l (0 to min(8-k, level1_avail))
#   - Si k+l == 0, satisfaction = c_i
#   - Else satisfaction = a_i*k + b_i*l
#   - On passe au prochain état i+1 avec m_rest-k, et level1_avail = k (car les sairyums cassés cette chanson i seront le level1 du i+1)
# - On cherche max total satisfaction pour i=0..n-1, m_rest from 0..m, level1_avail in 0..8 (on ne peut pas casser plus de 8 sairyums par chanson)
# - Le niveau 1 disponible peut être au max 8 car on ne peut secouer jusque 8 sairyums à la fois.
# - Initialement, i=0, m_rest=m, level1_avail=0 (aucun sairyum cassé auparavant au niveau 1).

# Implementation :
# - On va utiliser memoisation pour ce DP.
# - Valeurs négatives possibles, on garde un bon initial min.
# - A la fin, on affiche la valeur max de la fonction DP au départ.

import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
# songs[i] = (a_i, b_i, c_i)

from functools import lru_cache

@lru_cache(None)
def dp(i, m_rest, level1_avail):
    # i : chanson actuelle [0..n]
    # m_rest : nombre de sairyums encore non cassés
    # level1_avail : nombre de sairyums niveau 1 disponibles (cassés la chanson précédente)

    if i == n:
        # Toutes les chansons ont été traitées
        return 0

    a_i, b_i, c_i = songs[i]
    max_satisfaction = -10**9  # valeur basse pour max

    # On peut casser entre 0 et min(m_rest,8) sairyums cette chanson (car max 8 sairyums peuvent être secoués)
    max_fold = min(m_rest, 8)

    # On teste toutes combinaisons k (saierums niveau 2 cassés cette chanson), l (niveau 1 utilisés cette chanson)
    # avec k+l <= 8 et l <= level1_avail
    for k in range(max_fold+1):
        max_l = min(level1_avail, 8 - k)
        for l in range(max_l+1):
            if k + l == 0:
                # Aucun bâton secoué cette chanson : satisfaction c_i
                sat = c_i
            else:
                # satisfaction calculée par k et l
                sat = a_i * k + b_i * l

            # next level1_avail = k (les sairyums cassés cette chanson éclaire niveau 1 la chanson suivante)
            next_sat = sat + dp(i+1, m_rest - k, k)

            if next_sat > max_satisfaction:
                max_satisfaction = next_sat

    return max_satisfaction

print(dp(0, m, 0))