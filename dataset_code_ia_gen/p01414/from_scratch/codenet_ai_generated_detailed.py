# Solution pour le problème "Rectangular Stamps"
# 
# Approche :
# Le problème demande de colorier une grille 4x4 avec le minimum de pressions de tampons rectangulaires.
# Chaque tampon peut être placé n'importe où, même en débordant la grille, et peint la zone couverte d'une unique couleur choisie.
# On peut utiliser n'importe quel tampon plusieurs fois, et changer la couleur à chaque utilisation.
# L'objectif est de couvrir chaque case avec la bonne couleur (R, G, B) avec le nombre minimal de tampons.
#
# Observons que:
# - Les tampons ont un nombre limité de tailles (max 16 avec h,w ≤ 4).
# - La grille est petite (4x4).
# 
# Cette petite taille suggère une recherche exhaustive avec mémoïsation :
# - On peut représenter l'état actuel de la grille avec (4x4)=16 cases.
# - Chaque case peut être R/G/B ou encore non peintée au cours de la recherche.
# - Mais les cases déjà peintes partiellement ne gênent pas car l'encre d'un tampon recouvre totalement la couleur précédente.
# - On cherche donc le nombre minimal de tampons à poser pour arriver à la cible à partir d'un état initial vide.
#
# Représentation:
# - On codera l'état actuel de la grille avec un tuple de 16 caractères.
#
# Stratégie:
# - BFS ou DFS+mémo sur les états de la grille.
# - Depuis l'état actuel, on tente toutes les poses possibles (tampon i, position (x,y), couleur c).
# - On applique le tampon, obtenant un nouvel état.
# - On répète jusqu'à l'état final.
# 
# optimisation:
# - La taille de l'espace d'état est grosse (3^16 ~ 43 millions), mais la recherche sera réduite par mémoïsation et pruning.
# - On évite de refaire les états déjà rencontrés.
# - On peut stopper dès qu'on trouve le premier résultat (car recherche en BFS).
#
# Implementation:
# - Lecture entrée
# - Préparation des tampons
# - BFS sur états, stockage via dictionnaire (état -> nb tapes)
# - Calcul du minimal au final

from collections import deque

def main():
    N = int(input())
    stamps = []
    for _ in range(N):
        h,w = map(int, input().split())
        stamps.append((h,w))
    target = [input().strip() for _ in range(4)]

    # Convert target to a tuple for comparison
    target_flat = tuple(''.join(row) for row in target)
    # We'll flatten to length 16 string for states
    target_state = tuple(c for row in target for c in row)

    # initial state: all '.'
    empty_state = tuple('.' for _ in range(16))

    # Precompute all possible stamp placements with all colors R, G, B
    colors = ['R','G','B']

    # Function pour appliquer un tampon sur un état et retourner le nouvel état
    def apply_stamp(state, stamp_h, stamp_w, top, left, color):
        # state est un tuple 16 caractères
        new_state = list(state)
        for i in range(stamp_h):
            for j in range(stamp_w):
                x = top + i
                y = left + j
                if 0 <= x < 4 and 0 <= y < 4:
                    idx = x*4 + y
                    new_state[idx] = color
        return tuple(new_state)

    # BFS
    visited = dict()
    queue = deque()

    visited[empty_state] = 0
    queue.append(empty_state)

    while queue:
        state = queue.popleft()
        dist = visited[state]
        # Si état atteint, finir
        if state == target_state:
            print(dist)
            return
        # sinon essayer toutes les poses possibles
        for (h,w) in stamps:
            for top in range(-h+1, 4):
                for left in range(-w+1, 4):
                    for color in colors:
                        new_state = apply_stamp(state, h, w, top, left, color)
                        # Pruning rapide: on ne garde que les états qui sont un "progrès" vers la cible
                        # C'est délicat, mais on peut regarder que le nouvel état doit être au moins aussi proche
                        # i.e. pour chaque case, si la couleur est correcte ou progressée vers la cible.
                        # Mais ce sera compliqué. 
                        # On se contente d'enregistrer si non visité.
                        if new_state not in visited:
                            visited[new_state] = dist + 1
                            queue.append(new_state)

main()