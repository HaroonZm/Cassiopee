import sys
import math

# Constantes pour résoudre les problèmes de précision flottante
EPS = 1e-12

class Gate:
    def __init__(self, X, L, F, D, UD):
        self.X = X         # Position du seuil (km)
        self.L = L         # Volume d'eau à déplacer (L)
        self.F = F         # Max injection d'eau par heure (L/h)
        self.D = D         # Max vidage d'eau par heure (L/h)
        self.UD = UD       # 0 : est plus haut que ouest, 1 : est plus bas que ouest

        # Initialisation du niveau du sas: départ au niveau le plus bas entre les deux côtés
        # hauteur relative aux eaux du côté ouest ou est: on modélise: 0 = bas, 1 = haut
        # Si UD=0 => est est haut, donc sas initial au bas (0)
        # Si UD=1 => est est bas, donc sas initial au bas (0)
        # On considère que niveau 0 = niveau le plus bas
        # Nous utilisons True/False pour indiquer si sas est au niveau haut (True) ou bas (False)
        # mais sachant que sas commence toujours au niveau le plus bas:
        if UD == 0:
            # Ouest plus bas, Est plus haut
            # Sas initial = bas (niveau 0)
            self.level = False
        else:
            # Ouest plus haut, Est plus bas
            # Sas initial = bas (niveau 0)
            self.level = False

        # L'Etat du sas est simple: actuellement au niveau bas ou haut
        # On aura besoin d'une méthode pour simuler le changement entre ces états selon la présence de bateau
        # et la direction du flux

    def level_is_high(self):
        return self.level

    def high_level_rate(self):
        # quantité d'eau à injecter ou vidanger pour passer du bas au haut
        # ou du haut au bas.
        # En L/h (taux max)
        return self.F if not self.level else self.D

    def time_to_switch(self, to_high):
        # Calcule le temps nécessaire pour passer du niveau actuel au niveau 'to_high' (bool)
        # Bas => Haut = injection d'eau => taux F
        # Haut => Bas = vidange d'eau => taux D
        if self.level == to_high:
            return 0.0
        # Volume à deplacer
        volume = self.L
        if to_high:
            # injection eau
            rate = self.F
        else:
            # vidage eau
            rate = self.D
        return volume / rate


class Ship:
    def __init__(self, max_speed, position):
        self.Vmax = max_speed  # vitesse max (km/h)
        self.pos = position    # position actuelle (km)
        self.speed = 0.0       # vitesse actuelle (km/h)
        self.done = False      # si le bateau a dépassé le bord est du pays
        self.waiting = False   # s'il est arrêté

    def __repr__(self):
        return f'Ship(pos={self.pos:.6f}, speed={self.speed:.6f}, vmax={self.Vmax}, done={self.done})'


def simulate(N, M, K, gates_data, ship_speeds):
    # Construction des gates
    gates = []
    for data in gates_data:
        g = Gate(*data)
        gates.append(g)

    # Initial positions des bateaux:
    # Enoncé : bateaux placés à l'origine 0 km (premier bateau), puis espacés de 1km en arrière (vers l'ouest)
    # Donc le i-esime bateau a position = -i km (car 1er à 0, 2eme à -1, 3eme à -2, ...)
    ships = []
    for i in range(M):
        ship = Ship(ship_speeds[i], position = -i)
        ships.append(ship)

    # Vitesse initiale: uniquement le premier bateau peut partir rapidement, les autres doivent respecter la règle:
    # Chaque bateau atteint instantanément sa vitesse max, mais si il est à moins de 1km du bateau devant, il doit réduire sa vitesse
    # à la vitesse du bateau de devant.
    # Au départ, tous arrêtés (speed=0), mais dès que possible, avancent.
    # On modélisera le mouvement par évènements

    # Points à simuler:
    # Evènements à gérer :
    # - bateau arrive à devant/suivant à un endroit où il faut modifier vitesse pour respecter contrainte 1km
    # - bateau arrive à un seuil : il doit pouvoir passer seulement si le niveau du sas correspond au niveau d'eau amont
    #   (ceci nécessite de modéliser le sas: quand changer le niveau, et la durée)
    # - changement niveau sas de bas à haut ou haut à bas
    # - bateau peut sortir du sas si les conditions sont bon (niveau de sas = eau aval)
    # - fin de simulation quand le dernier bateau dépasse K

    # Pour modéliser on procède en évènements chronologiques
    # Chaque évènement a un temps, on avance de temps en temps et on met à jour vitesse et position des bateaux

    # Evènements possibles (avec leurs traitements):
    # - bateau atteint position d'un gate depuis ou vers le sas (entrée/sortie)
    # - sas change de niveau (requis pour que bateau entre ou sorte)
    # - bateau atteint position du bateau devant (doit s'adapter)

    # Pour simplifier, on utilisera une approche par pas de temps glissant à partir d'évènements à gérer
    # Les évènements sont pushés dans une file prioritaire
    # Initialement, tous les bateaux démarrent à vitesse maximale (pour le premier),
    # puis vitesse adaptées selon espacements initiaux (ships espacés de 1 km donc vitesse max peut être initialement donnée)

    import heapq

    # Position des gates plus une porte virtuelle finale après K (à K)
    gate_positions = [g.X for g in gates]
    gate_positions_set = set(gate_positions)

    # Evènement contient
    # (temps, ev_type, param)
    # ev_type:
    # 1: bateau atteint position cible (param=(ship_index, position))
    # 2: gate sas niveau changement fini (param=gate_index)
    # 3: bateau sort du sas (param=ship_index, gate_index)
    # 4: bateau commence à bouger ou ralentir (param=ship_index)
    # On se limitera a evenement 1 et 2, en prenant soin d gérer tout le reste dans la simulation des évènements

    # Etat des sas: pour chaque sas:
    # level: False ou True (bas ou haut)
    # target_level: si sas doit changer d'etat (True/False/None)
    # boat_inside: None ou index bateau (on peut gérer l'état avec une variable supplémentaire)
    sas_inside = [None] * N  # None ou i bateau
    sas_target_level = [None] * N  # None si pas de changement en cours
    sas_level = [g.level for g in gates]

    # Etat des bateaux:
    # position en float
    # vitesse en float
    # done booléen si sortie
    # on ajoute index de gate où le bateau est (si dans sas), sinon None
    ship_in_sas = [None] * M

    # On définit un heap d'évènements
    event_queue = []

    # Certains outils pour avancer un bateau à une position donnée en vitesse donnée
    def schedule_ship_arrival(i, pos, current_time):
        # Calcule temps pour que bateau i atteigne pos à vitesse courante, si possible (pos > pos courante)
        # Si vitesse=0 ou pos <= position actuelle, pas d'évènement généré
        s = ships[i]
        if s.done:
            return
        if pos < s.pos + EPS:
            return
        dist = pos - s.pos
        if s.speed < EPS:
            return
        t = dist / s.speed
        heapq.heappush(event_queue, (current_time + t, 1, (i, pos)))

    # Ajuster les vitesses des bateaux selon la contrainte d'espacement
    def adjust_speeds(current_time):
        # On parcourt les bateaux dans l'ordre, du premier (plus à l'est) au dernier (plus à l'ouest)
        # Rappel: bateau 0 plus en amont (position la plus élevée) au départ
        # les bateaux sont en positions croissantes (position -i)
        # Il faut que le bateau suivant ne soit jamais a moins d'1 km derrière
        # règle: si bateau j rattrape bateau i (j>i), alors V_j = V_i
        # sinon V_j = Vmax_j

        # On commence par le premier bateau: vitesse max
        # mais s'il est dans sas, vitesse = 0 car il doit attendre
        # ou s'il est "bloqué" devant un bateau arrêté

        # On recompute aussi les évènements d'arrivé après changement vitesse

        # On traite les bateaux dans l'ordre croissant des positions (donc ordre index)
        # important: bateau avec plus haut index a position initiale plus faible

        # Rien ne nous dit que index i < j => vi est devant vj, car position peuvent bouger,
        # donc on trie par position actuelle décroissante (plus grand pos est devant)
        # Mais positions peuvent être égales ou proches, on gère

        # Nous allons trier les bateaux par position décroissante (bords est à l'ouest)
        idx_order = sorted(range(M), key=lambda x: ships[x].pos, reverse=True)

        # Pour la vitesse, on parcourt de l'avant à l'arrière, on fixe viteesses

        speeds = [0.0]*M
        # Premier bateau devant à sa vitesse max ou 0 s’il est dans sas ou fini
        front_i = idx_order[0]
        if ships[front_i].done:
            speeds[front_i] = 0.0
        elif ship_in_sas[front_i] is not None:
            # dans un sas, bateau doit attendre, vitesse=0
            speeds[front_i] = 0.0
        else:
            speeds[front_i] = ships[front_i].Vmax

        # Puis pour les autres:
        for posi in range(1, M):
            i = idx_order[posi]
            # On cherche le bateau supposé devant
            # On calcule position du bateau devant dans order
            front = idx_order[posi-1]

            # Contrainte: bateau i doit garder distance >= 1km du bateau devant
            # Cas vitesse max du i et vitesse du devant si i rattrape -> i réduit sa vitesse

            # distance actuelle
            dist = ships[front].pos - ships[i].pos

            # Si distance < 1, i doit rouler à vitesse du devant si Vmax_i > speed_front

            if dist < 1 - EPS:
                # on force vitesse <= vitesse du devant
                speeds[i] = min(ships[i].Vmax, speeds[front])
            else:
                # distance ok, peut aller à sa vitesse max
                speeds[i] = ships[i].Vmax

            # Mais si devant est arrêté (vitesse=0) et distance <=1, vitesse=0, sinon vitesse max
            if speeds[front] < EPS and dist < 1 + EPS:
                speeds[i] = 0.0

        # On applique dans l'ordre original des boats
        changed = False
        for i in range(M):
            if abs(speeds[i] - ships[i].speed) > EPS:
                ships[i].speed = speeds[i]
                changed = True

        return changed

    # On doit gérer aussi les appels pour recaler les évènements de arrivée
    def reschedule_all_arrivals(current_time):
        # On enlève tous les événements existants, ici on reconstruit event queue à partir des bateaux+équipements
        # mais ce n’est pas trivial, car évènements gates doivent être conservés
        # On va juste ajouter les évènements arrivés à partir d'aujourd'hui afin d’éviter des conflits

        # Pour simplifier, on ne supprime pas les évènements, mais on ne programme que les prochains évènements d'arrivée bateaux
        # Ils seront ajoutés si on detecte que la position a été modifiés ou vitesse a changé

        # Cette fonction sera appelée seulement après ajustement vitesse.

        # On programme l'arrivée du bateau à la prochaine position importante: gate ou fin de K +1 (au delà de K)
        # ou position du bateau devant -1 pour respecter distance

        # Pour chaque bateau, on calcule sa prochaine position cible

        for i in range(M):
            if ships[i].done:
                continue
            s = ships[i]
            # Position suivante possible: gate la plus proche à l'est > s.pos
            next_pos = K + 10  # quelques km après fin pour sortir
            for g in gates:
                if g.X > s.pos + EPS and g.X < next_pos:
                    next_pos = g.X
            # Ensuite, si ce n'est pas le premier bateau, on doit s'arreter avant bateau devant
            # pour un garde fou, position bateau devant -1

            # on trouve bateau devant
            candidates = []
            for j in range(M):
                if ships[j].pos > s.pos + EPS:
                    candidates.append((ships[j].pos, j))
            if candidates:
                candidates.sort()
                pos_front, idx_front = candidates[0]
                # distance doit être au moins 1km
                pos_limit = pos_front - 1.0
                if pos_limit < next_pos:
                    next_pos = pos_limit

            # Enfin si la vitesse est > 0 on programme arrivée à next_pos
            if s.speed > EPS and next_pos > s.pos + EPS:
                schedule_ship_arrival(i, next_pos, current_time)
    # Méthode: on procède par itérations d'évènements:

    # Initialisation:
    current_time = 0.0
    # Tous les bateaux démarrent immobiles, on met vitesse max possible en ajustant constraints
    # Ils sont espacés de 1km, plus lentes propagées

    # mets vitesse max pour tous (le premier le max, les autres sont plus lents donc peuvent aller direct a leur vitesse max)
    for i in range(M):
        ships[i].speed = ships[i].Vmax

    # Adjuste vitesses pour respecter distances initiales:
    adjust_speeds(current_time)
    reschedule_all_arrivals(current_time)

    # On garde l'etat d'evènements de sas:
    # sas_target_level[i], None si pas de changement, sinon True/False

    # Procéder par boucle d'évènements
    while True:
        # Si aucun bateau n'a fini on break si pas d'évènements ?

        # Condition finale : tous les bateaux sont au-delà de K (fin du pays)
        done_all = True
        for i in range(M):
            if not ships[i].done:
                done_all = False
                break
        if done_all:
            # Fin de simulation, afficher temps actuel
            return current_time

        if not event_queue:
            # Plus d'évènements => on peut avancer le temps au prochain changement imaginaire (on a bouclé)
            # Cela ne devrait pas arriver car on a toujours des évènements pour les bateaux
            # ou sas.
            # Pour éviter un blocage, on avance un petit pas
            dt = 1e-4
            for i in range(M):
                s = ships[i]
                if s.done:
                    continue
                s.pos += s.speed * dt
            current_time += dt
            continue

        # Prendre évènement suivant
        time_ev, ev_type, param = heapq.heappop(event_queue)

        # Avancer le temps...
        dt = time_ev - current_time
        if dt < -EPS:
            # Evènement antérieur au temps actuel => bug dans la file, on ignore
            continue
        # Déplacer les bateaux en fonction de leur vitesse et dt
        for i in range(M):
            if ships[i].done:
                continue
            ships[i].pos += ships[i].speed * dt
        current_time = time_ev

        if ev_type == 1:
            # Bateau i arrive à position pos cible
            i, pos = param
            s = ships[i]
            # Corriger position exacte possible à cause erreurs flottantes:
            s.pos = pos

            # Vérifier si fin atteint --> s.pos >= K
            if s.pos >= K - EPS:
                s.done = True
                s.speed = 0.0
                ship_in_sas[i] = None
                # Quand bateau fini, on doit laisser le suivant accélérer s'il peut
                # Re-ajuster vitesses et réordonner evènements
                adjust_speeds(current_time)
                reschedule_all_arrivals(current_time)
                continue

            # Vérifier s'il a atteint un gate X

            if pos in gate_positions_set:
                # C'est une position de sas
                gate_i = gate_positions.index(pos)
                g = gates[gate_i]

                # Scénarios:

                # 1) Si bateau est devant sas (juste arrive dessus) et dans sens d'entree, 
                # il ne peut entrer que si sas niveau = niveau coté ouest

                # Determinons si bateau est à l'entrée (ou sortie) ou côté sas
                # Cas entree sas:
                # Si bateau n'est pas dans sas, il essaie d'entrer si sas_level = côté ouest du gate
                # Il doit s'arreter devant sas sinon

                if ship_in_sas[i] is None:
                    # Bateau devant sas
                    # sas_level vs niveau ouest
                    # niveau ouest est le plus haut ou bas selon UD et sas_level booléen

                    # Niveau ouest: si UD=0 => est haut, ouest bas
                    # UD=0 => ouest bas (False), est haut (True)
                    # UD=1 => ouest haut (True), est bas (False)
                    if g.UD == 0:
                        west_level = False
                    else:
                        west_level = True

                    # Le bateau peut entrer dans sas que si sas_level == niveau ouest
                    if sas_level[gate_i] == west_level and sas_inside[gate_i] is None:
                        # Bateau entre dans sas
                        ship_in_sas[i] = gate_i
                        sas_inside[gate_i] = i
                        # Bateau s'arrête dans sas, vitesse=0
                        ships[i].speed = 0.0

                        # Début de changement niveau