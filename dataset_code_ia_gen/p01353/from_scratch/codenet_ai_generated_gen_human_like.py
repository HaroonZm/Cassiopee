import sys
input = sys.stdin.readline

n = int(input())
h0,a0,d0,s0 = map(int,input().split())
enemies = [tuple(map(int,input().split())) for _ in range(n)]

# Séparer les ennemis selon qu'ils attaquent avant ou après le héros, selon leur agilité
before = []  # ennemis avec s_i > s0 attaquent avant le héros
after = []   # ennemis avec s_i < s0 attaquent après le héros

for h,a,d,s in enemies:
    if s > s0:
        before.append((h,a,d,s))
    else:
        after.append((h,a,d,s))

# Si un ennemi a a <= d0, il ne peut pas blesser le héros
# sinon il inflige max(a_i - d0, 0) de dégâts à chaque fois qu'il attaque
# Mais chaque ennemi attaque tous les tours où il est vivant (avant ou après héros)

# Calcul du nombre d'attaques du héros
# Le héros attaque une fois par tour, toujours après les ennemis with s > s0 (avant) et avant ceux with s < s0 (après)
# Ordre d'attaque par agilité décroissante (si égaux, impossible car s_i distinct)
# Donc dans chaque tour:
#   Ennemis "before" attaquent (au max tous ceux encore vivants)
#   Héros attaque un ennemi vivant (après avoir subi les attaques "before")
#   Ennemis "after" attaquent (avec les HP mis à jour)

# Les dégâts du héros a0-d_i pour chaque ennemi sont fixes
# Si a0 <= d_i on ne peut pas tuer cet ennemi

# L'idée est de trouver une ordre d'élimination des ennemis qui minimise les dégâts subis

# Remarques:
# - Si un ennemi inflige 0 dégâts au héros (a_i <= d0), il n'est pas néfaste pour le héros.
# - Le héros ne perd jamais des points de vie dans une attaque, donc peut tuer tous ces ennemis 0 dégâts sans coût.
# - Les ennemis avec a_i > d0 infligent des dégâts positifs à chaque attaque tant qu'ils ne sont pas morts.
# - Le héros attaque une fois par tour sur un ennemi vivant, réduisant son h_i par (a0 - d_i) dégâts.
# - Pour chaque ennemi, on doit calculer le nombre d'attaques pour le tuer:
#   hits_i = ceil(h_i / (a0 - d_i))

# Approche:
# Calculer damage_i = a_i - d0 si >0, sinon 0
# hits_i = ceil(h_i / (a0 - d_i))
# On veut ordonner l'élimination pour minimiser la somme des dégâts subis.

# L'ordre d'attaque est déterminé par s_i (agilité), et le système de tours est:
# tores:
#   Avant, attaquent "before" vivants --> dégâts du héros: sum damage_i * nombre d'attaques ennemis restants
#   Héros attaque un ennemi choisi (un seul)
#   Après, attaquent "after" vivants

# Le nombre total de tours est le nombre total de coups nécessaires pour tuer tous les ennemis.

# Stratégie simplifiée pour minimiser dégâts: Tuer d'abord les ennemis les plus dangereux qui attaquent avant le héros (car ils attaquent avant chaque attaque)
# Puis les ennemis qui attaquent après, puisque après le coup du héro, ils attaquent, mais le héros les frappent avant leurs attaques

# En fait, on doit ordonner les ennemis "before" dans un ordre qui minimise la somme écoulée de dégâts maximum et les ennemis "after" de la même manière.

# Or les tour sont toujours dans cet ordre fixe:
#   all "before" enemis (dans ordre agilité decroissante)
#   hero
#   all "after" enemis (ordre agilité decroissante)

# Le héros décide la cible du coup à chaque tour: on peut donc choisir l'ordre d'élimination

# On va supposer que l'ordre de sélection des ennemis est dans n'importe quel ordre
# pour minimiser les dégâts subis.

# Calcul minimal scénario:
# Le héro ne peut pas éviter les attaques des ennemis "before" avant d'agir, donc mieux est de tuer les ennemis "before" qui infligent le plus de dégâts le plus rapidement,
# réduisant le nombre d'attaques qu'ils ont avant disparition.

# Pour ces ennemis "before":
# - On calcule le nombre de coups nécessaires pour tuer chacun: hits_i.
# - On doit ordonner la séquence d'attaques hero pour minimiser cout = somme sur i de damage_i * temps de vie residuel.
# En gros, on veut minimiser la somme pondérée des temps de survie, avec poids = damage_i.

# C'est un problème de scheduling où on doit minimiser la somme pondérée des temps d'achèvement: la règle de tri optimale est la règle de Smith, ordonner par p_i / w_i croissant (pour p_i la durée, w_i le poids)

# Ici:
#  p_i = hits_i (nombre de tours pour tuer cet ennemi)
#  w_i = damage_i

# Or pour minimiser la somme w_i * C_i (C_i est completion time en nombre de tours), on ordonne par p_i / w_i croissant.

# Le héros ne peut tuer qu'un ennemi à la fois mais il peut changer la cible à chaque tour.
# Donc en fait, il peut fragmenter les coups, mais attaquer un peu un ennemi, puis un autre, etc.
# Mais comme l'ordre est fixe (en agilité), il faut que les ennemis soient tués par séquences de coups, pas fragmentées.

# Cependant, le héros attaque après tous les ennemis "before", donc pour eux, les attaques d'avant sont fixes.
# On arrive à un problème compliqué.

# Solution plus simple en tenant compte que le héros attaque une fois par tour:
# - On simule la bataille en attaquant les ennemis "before" dans un ordre optimal (selon ratio p_i / w_i)
#   en tuant entièrement chacun avant de passer au suivant.

# Après avoir tué tous les ennemis before, le héros attaque les ennemis "after" dans un ordre optimal similaire.

# Calcul final des dégâts totaux:
# - Dégâts avant tour du héros = sum pour ennemis before survivants damage_i
# - Dégâts après tour du héros = sum pour ennemis after survivants damage_i

# On résume cela par simulation.

def calc_hits(h,a,d):
    dmg = a0 - d
    if dmg <= 0:
        return None
    return (h + dmg -1)//dmg

def sum_damage(enemies):
    return sum(max(a - d0,0) for h,a,d,s in enemies)

def simulate_order(enemies, s_order):
    # enemies : liste (h,a,d,s)
    # s_order : liste d'indices représentant l'ordre d'élimination (indices dans enemies)
    # On simule en tuant complètement chaque ennemi dans cet ordre, un ennemi tué avant de passer au suivant
    # On calcule le dégâts totaux subis durant la phase

    total_damage = 0
    # liste mutable
    e = list(enemies)
    # pour chaque ennemi on calcule:
    hits = []
    damage = []
    for h,a,d,si in e:
        if a - d0 >0 and a0 - d > 0:
            hits.append((h,a,d,si,calc_hits(h,a,d)))
            damage.append(max(a - d0,0))
        elif a - d0 > 0:
            # ennemi inflige degat mais impossible de le tuer, défaite assurée
            return -1
        else:
            # ennemi 0 dégats, pas important
            hits.append((h,a,d,si,None))
            damage.append(0)

    # On simule les avoir en hp pendant la séquence
    # On suppose qu'on tue un ennemi à la fois en hp parfait

    # Or on ne peut pas attaquer plus d'un ennemi par tour

    # Dégâts subis par tour = somme damage_i des ennemis vivants (non tués)
    # Le temps de vie total correspond au nombre total de tours / coups nécessaires à leur élimination.

    # On calcule la somme pondérée des temps de vie

    # Certes, comme tous attaquent à chaque tour, dégâts subis par tour c'est somme des damages des ennemis vivants

    current_enemies = [list(e[i]) for i in range(len(e))]
    current_alive = [True]*len(e)

    total_damage = 0
    for idx in s_order:
        h,a,d,si = current_enemies[idx][0], current_enemies[idx][1], current_enemies[idx][2], current_enemies[idx][3]
        dmg_to_enemy = a0 - d
        if dmg_to_enemy <=0:
            # impossible à tuer
            return -1
        turns = (h + dmg_to_enemy -1)//dmg_to_enemy
        for _ in range(turns):
            # à chaque tour, ennemis vivants attaquent le héros

            damage_this_turn = 0
            for j in range(len(e)):
                if current_alive[j]:
                    dj = max(e[j][1] - d0,0)
                    damage_this_turn += dj
            total_damage += damage_this_turn
            # hero attaque cet ennemi
            current_enemies[idx][0] -= dmg_to_enemy
            if current_enemies[idx][0] <=0:
                current_alive[idx] = False
                break
        # ennemi idx mort ici

    return total_damage

# Séparer indices before et after
before_idx = []
after_idx = []
e = enemies

for i,(h,a,d,s) in enumerate(e):
    if s > s0:
        before_idx.append(i)
    else:
        after_idx.append(i)

# Calculer hits et damage pour each enemy
def get_hits_damage(idx):
    h,a,d,s = e[idx]
    dmg_to_enemy = a0 - d
    if dmg_to_enemy <=0 and (a - d0 >0):
        # impossible à tuer ennemi qui attaque
        return None,None
    if dmg_to_enemy <=0:
        hits = 0
    else:
        hits = (h + dmg_to_enemy -1)//dmg_to_enemy
    dmg_to_hero = max(a - d0,0)
    return hits,dmg_to_hero

before_list = []
for i in before_idx:
    h,a,d,s = e[i]
    hits,dmg = get_hits_damage(i)
    if hits is None:
        print(-1)
        sys.exit()
    before_list.append((i,h,a,d,s,hits,dmg))

after_list = []
for i in after_idx:
    h,a,d,s = e[i]
    hits,dmg = get_hits_damage(i)
    if hits is None:
        print(-1)
        sys.exit()
    after_list.append((i,h,a,d,s,hits,dmg))

# Ordre optimal pour minimiser somme pondérée des temps d'achèvement = trier par hits/dmg croissant
# Si dmg=0, hits/dmg infini, on met à la fin car sans dégâts ils ne gênent pas

def key_fun(x):
    i,h,a,d,s,hits,dmg = x
    if dmg==0:
        return float('inf')
    return hits/dmg

before_list.sort(key=key_fun)
after_list.sort(key=key_fun)

order_indices = [x[0] for x in before_list] + [x[0] for x in after_list]

res = simulate_order(e,order_indices)
if res == -1:
    print(-1)
else:
    # On enlève les dégâts que le héros subit au tour final après la mort de tous les ennemis,
    # mais dans la simulation on ajoute toujours les dégâts de tous ennemis vivants avant attaque:
    # or, lorsque le dernier ennemi meurt, il y a un tour de trop compté.
    # En notre simulation, on compte les dégâts avant que le héros frappe et tue le dernier ennemi.
    # La dernière attaque tue un ennemi, mais les ennemis attaquent avant la frappe,
    # il est donc correct de prendre les dégâts de ce tour-là.
    print(res)