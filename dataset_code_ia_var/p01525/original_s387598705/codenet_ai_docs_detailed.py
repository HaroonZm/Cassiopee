from collections import defaultdict

def update_state_for_next_day(day, t0s, t1s, t2s, t3s, restore, t1_cnt_save, t3_cnt_save, t1_cnt, t3_cnt, MAX):
    """
    Met à jour les tableaux de transitions ('t0s', 't1s', 't2s', 't3s', 'restore')
    pour passer au jour suivant.
    Prend en compte les compteurs différés utilisés pour gérer les événements de type 1 et type 2.
    
    Args:
        day (int): Le jour courant.
        t0s, t1s, t2s, t3s (list): Listes de transitions cumulatives pour chaque type d'événement.
        restore (list): Liste représentant l'état restauré au jour 'day'.
        t1_cnt_save, t3_cnt_save (defaultdict): Sauvegardes des événements différés pour type 1 et 2.
        t1_cnt, t3_cnt (int): Compteurs des ajouts en attentes pour les types 1 et 2.
        MAX (int): Le jour maximal traité (limite supérieure).
        
    Returns:
        (int, int): Nouvelles valeurs des compteurs t1_cnt et t3_cnt.
    """
    # Propagation cumulative des effets t0s (Simples) au jour suivant
    t0s[day + 1] += t0s[day]
    
    # Mise à jour du compteur différé pour les effets de type 1
    if day + 1 in t1_cnt_save:
        t1_cnt -= t1_cnt_save[day + 1]
    t1s[day + 1] += t1s[day] + t1_cnt

    # Mise à jour du compteur différé pour les effets de type 2 (qui ont un effet cubique)
    if day + 1 in t3_cnt_save:
        t3_cnt -= t3_cnt_save[day + 1]
    t3s[day + 1] += t3s[day] + 2 * t3_cnt
    
    # Mise à jour cumulative du tableau t2s, qui dépend de t3s (effets quadratiques)
    t2s[day + 1] += t2s[day] + t3s[day + 1]
    
    # Calcul du nombre de restaurations pour le jour suivant
    restore[day + 1] = restore[day] + 1 + t0s[day] + t1s[day] + t2s[day]
    
    return t1_cnt, t3_cnt

def process_event(day, w, t, x, t0s, t1s, t2s, t3s, restore, t1_cnt_save, t3_cnt_save, t1_cnt, t3_cnt):
    """
    Traite un événement donné qui modifie l'état du jour en fonction de son type.
    
    Args:
        day (int): Le jour actuel.
        w (int): Seuil de restauration pour l'événement en question.
        t (int): Type d'événement (0, 1 ou 2).
        x (int): Paramètre associé au type d'événement (durée ou amplitude).
        t0s, t1s, t2s, t3s (list): Listes de transitions cumulatives pour chaque type d'événement.
        restore (list): Liste représentant l'état restauré au jour 'day'.
        t1_cnt_save, t3_cnt_save (defaultdict): Sauvegardes des événements différés pour type 1 et 2.
        t1_cnt, t3_cnt (int): Compteurs des ajouts en attentes pour les types 1 et 2.
        
    Returns:
        tuple: Compteurs t1_cnt, t3_cnt mis à jour.
    """
    # Affiche le jour où l'événement peut s'appliquer
    print(day)
    if t == 0:
        # Effet immédiat: augmentation simple qui dure x jours
        t0s[day] += 1
        t0s[day + x] -= 1
    elif t == 1:
        # Effet linéaire, s'additionne pour x jours
        t1_cnt += 1
        t1_cnt_save[day + x] += 1
        t1s[day] += 1
        t1s[day + x] -= x
    elif t == 2:
        # Effet quadratique/cubique, ajoute et programme compensation
        t3_cnt += 1
        t3_cnt_save[day + x] += 1
        t3s[day] += 1
        t3s[day + x] -= x * 2 - 1
        t2s[day] += 1
        t2s[day + x] -= x ** 2
    return t1_cnt, t3_cnt

def simulate_until_day(target_day, day, t0s, t1s, t2s, t3s, restore, t1_cnt_save, t3_cnt_save, t1_cnt, t3_cnt, MAX):
    """
    Fait avancer la simulation jusqu'à ce que 'day' atteigne 'target_day', en mettant à jour
    tous les tableaux concernés.
    
    Args:
        target_day (int): Le jour jusqu'où il faut simuler.
        day (int): Le jour courant (début de la simulation).
        t0s, t1s, t2s, t3s (list): Listes de transitions cumulatives.
        restore (list): Liste représentant l'état restauré.
        t1_cnt_save, t3_cnt_save (defaultdict): Sauvegardes des événements différés.
        t1_cnt, t3_cnt (int): Compteurs pour les types 1 et 2.
        MAX (int): Limite supérieure du jour à traiter.
        
    Returns:
        tuple: Nouveau jour, t1_cnt, t3_cnt mis à jour.
    """
    # On avance la simulation jusqu'au jour cible
    while day < target_day:
        t1_cnt, t3_cnt = update_state_for_next_day(
            day, t0s, t1s, t2s, t3s, restore, t1_cnt_save, t3_cnt_save, t1_cnt, t3_cnt, MAX
        )
        day += 1
    return day, t1_cnt, t3_cnt

def main():
    """
    Fonction principale du programme.
    Simule un processus incrémental de restauration sur une séquence de jours, en gérant différents types d'événements
    qui affectent la progression de cette restauration. Pour chaque événement, détermine quand celui-ci peut intervenir
    selon l'état actuel, puis applique son effet sur la séquence de futures restaurations. Gère aussi des requêtes
    pour obtenir l'état restauré à un jour donné.
    
    Entrées:
        - Ligne 1: deux entiers n et q.
        - Ensuite n lignes: trois entiers par ligne : w, t, x (paramètres d'événements)
        - Ensuite q lignes: un entier y par requête (jour pour lequel on veut la valeur de restauration)
    
    Sorties:
        - Pour chaque événement : le jour où il s'applique ou "Many years later"
        - Pour chaque requête : la valeur restaurée au jour correspondant
    """
    MAX = 3652425  # Jour maximal ; prévoir assez large selon la contrainte de l'exercice
    n, q = map(int, input().split())
    
    # Lecture des événements
    lst = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Initialisation des tableaux d'état/transitions
    restore = [0] * (MAX + 10010)  # État restauré pour chaque jour
    t0s = [0] * (MAX + 10010)      # Effets de type 0 (constantes sur des intervalles)
    t1s = [0] * (MAX + 10010)      # Effets de type 1 (linéaires)
    t2s = [0] * (MAX + 10010)      # Effets de type 2 (quadratiques)
    t3s = [0] * (MAX + 10010)      # Effets auxiliaires temporaire pour les quadratiques
    
    # Dictionnaires pour les effets différés qui devront être soustraits après x jours
    t1_cnt_save = defaultdict(int)
    t3_cnt_save = defaultdict(int)
    
    # Compteurs d'effets en attente de type 1 et 2
    t1_cnt = 0
    t3_cnt = 0
    
    day = 0  # Jour courant dans la simulation
    
    # Traitement des événements l'un après l'autre
    for i, line in enumerate(lst):
        w, t, x = line
        
        # Simule jusqu'à ce que le nombre de restaurations ait atteint w
        while day < MAX and w > restore[day]:
            t1_cnt, t3_cnt = update_state_for_next_day(
                day, t0s, t1s, t2s, t3s, restore, t1_cnt_save, t3_cnt_save, t1_cnt, t3_cnt, MAX
            )
            day += 1
        
        # Si l'événement peut être restauré (w <= restore[day]), traite l'effet
        if w <= restore[day]:
            t1_cnt, t3_cnt = process_event(
                day, w, t, x, t0s, t1s, t2s, t3s, restore, t1_cnt_save, t3_cnt_save, t1_cnt, t3_cnt
            )
        else:
            # Sinon, impossible sur cette période ("beaucoup plus tard")
            print("Many years later")
    
    # Traitement des requêtes
    for _ in range(q):
        y = int(input())
        # On fait progresser la simulation jusqu'au jour de la requête, si nécessaire
        day, t1_cnt, t3_cnt = simulate_until_day(
            y, day, t0s, t1s, t2s, t3s, restore, t1_cnt_save, t3_cnt_save, t1_cnt, t3_cnt, MAX
        )
        # On affiche le nombre de restaurations à ce jour-là
        print(restore[y])

main()