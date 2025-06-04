import sys
sys.setrecursionlimit(10**7)

# On cherche le temps minimum (en secondes) pour atteindre le temps t de la scène à VITESSE NORMALE.
# Chaque seconde, on peut choisir d'appuyer sur [3x], sur [1/3x] ou ne rien faire.
# Ces boutons modifient la vitesse de lecture à partir de la seconde suivante (vitesse est multipliée par 3 ou divisée par 3, sauf si la vitesse est déjà normale et on presse [1/3x], elle ne change pas).
#
# On veut minimiser le temps total passé, sachant que le temps "réel" parcouru dans la vidéo est égal à la somme des (secondes écoulées * vitesse au moment de ces secondes).
# La vitesse initiale est normale (1x), et on démarre à la position 0 (millisecondes dans la vidéo).
#
# L'approche est de faire un DFS avec mémorisation pour essayer tous les chemins.
# 
# Arguments clés :
# - pos : position actuelle en secondes dans la vidéo (float ou int)
# - speed : vitesse actuelle (uniquement puissance de 3^n, avec n entier)
# 
# Objectif : atteindre pos == t (la position souhaitée),
# en ayant la position normale de lecture, i.e vitesse == 1 (vitesse normale),
# en minimisant la durée écoulée (en secondes).
#
# On modélise la recherche du temps minimal.
#
# Pour réduire l'état et la mémoire, on note que la vitesse est toujours 3^k pour un entier k (k peut être négatif, 0, ou positif).
# De plus, pos est la distance restante vers t.
#
# Le problème devient : minimiser le temps pour parcourir une distance t avec vitesse pouvant être multipliée ou divisée par 3 aux secondes entières (après le 1er sec, 2nd sec, ...).
# 
# On travaille en distance restante (reste). Comme on peut avancer à vitesse v pendant 1 seconde, puis changer la vitesse.
#
# On utilise une fonction récursive f(remaining_distance, speed_exponent)
#
# On implémente seulement pour distances entières (car t entier), et speed est puissance de 3 (donc on peut stocker l'exposant).
#
# Pour l'exposant : vitesse = 3^k, k entier, vitesse = position avancée par seconde.
#
# On applique aussi un cache (memo) pour éviter recomputations.
#
# Cas de base : if remaining_distance == 0 and speed == 1 -> on a fini, temps = 0
# Si remaining_distance < 0, impossible.
#
# À chaque étape, on peut avancer 1 seconde à la vitesse actuelle (avancer d speed unité),
# puis au prochain instant (dans la prochaine récursion), on peut soit :
# - ne rien faire (garder speed),
# - multiplier speed par 3 (exposant k+1),
# - diviser speed par 3 (exposant k-1), sauf si speed == 1 (exposant == 0) alors on ne peut pas diviser plus bas.
#
# On cherche minimal temps total = 1 + min(f(remaining_distance - speed, speed_modifié))
#
# Restrictions : 
# - remaining_distance et speed sont entiers.
# - remaining_distance >= 0
#
# On limite les exposants car la vitesse peut rapidement devenir énorme ou fragmentée.
#
# Implémentation : une fonction récursive avec cache.

t = int(sys.stdin.readline())

from functools import lru_cache

# On définit la fonction récursive
@lru_cache(None)
def dfs(remaining_distance, speed_exp):
    # remaining_distance >= 0 est un entier
    # vitesse = 3^speed_exp
    if remaining_distance == 0:
        # On doit être à vitesse normale (speed_exp == 0) pour pouvoir "start watching"
        if speed_exp == 0:
            return 0  # on a fini, pas de temps supplémentaire
        else:
            # on doit ramener la vitesse à normale (speed_exp=0) en accélérant ou ralentissant
            # on ne peut rien avancer en avançant vitesse != 1 -> on doit "perdre" du temps à modifier la vitesse
            # Mais comme avancer 1s = avancer 3^k secondes vidéo, on ne peut pas atteindre exact 0 (si vitesse !=1).
            # Donc il faut décomposer le problème:
            # Pour ramener speed_exp à 0, on doit presser le bouton plusieurs fois sans avancer, ce n'est pas possible car chaque pression agit sur la vitesse à la seconde suivante.
            # Donc, pas possible d'être sur une position correcte sauf si on est vitesse normale.
            return 10**18  # infini éloigné

    if remaining_distance < 0:
        # impossible
        return 10**18

    # vitesse réelle
    speed = pow(3, speed_exp)

    res = 10**18

    # On peut prendre 1 seconde à la vitesse actuelle (avancer d'une distance speed)
    # Puis, au moment suivant, on peut choisir d'appuyer sur [3x], [1/3x] ou rien.
    # Mais si on divise la vitesse par 3 alors qu'on est à vitesse normale, ça ne change rien.

    # Option 1: ne rien changer (garder speed_exp)
    temp = dfs(remaining_distance - speed, speed_exp)
    if temp != 10**18:
        res = min(res, 1 + temp)

    # Option 2: appuyer sur [3x] -> vitesse *=3 => speed_exp + 1
    temp = dfs(remaining_distance - speed, speed_exp + 1)
    if temp != 10**18:
        res = min(res, 1 + temp)

    # Option 3: appuyer sur [1/3x] -> vitesse /=3 sauf si vitesse normale (speed_exp==0)
    if speed_exp > 0:
        temp = dfs(remaining_distance - speed, speed_exp - 1)
        if temp != 10**18:
            res = min(res, 1 + temp)
    elif speed_exp == 0:
        # vitesse normale, diviser par 3 ne change rien, on peut essayer
        # mais c'est inutile, le problème dit que on ne change pas vitesse si la vitesse normale
        # donc ne rien faire est équivalent
        pass

    return res

print(dfs(t, 0))