def cv(t):
    # Définition d'une fonction appelée 'cv' qui prend un argument entier 't'.
    # Cette fonction convertit un temps sous la forme HHMM en un nombre total de minutes.
    # Par exemple, 1230 signifie 12 heures et 30 minutes.
    
    # La division entière par 100 (t//100) permet d'isoler la partie 'heure' du temps.
    # La multiplication par 60 convertit ces heures en minutes.
    # La partie modulo 100 (t % 100) donne les minutes.
    # L'addition des deux donne le temps total en minutes depuis minuit.
    
    return t // 100 * 60 + t % 100  # Conversion de HHMM en minutes

while True:
    # Boucle infinie permettant de traiter plusieurs cas jusqu'à une condition d'arrêt.
    
    # raw_input() lit une ligne de texte depuis l'entrée standard.
    # split() découpe cette ligne en parties séparées par des espaces.
    # map(int, ...) convertit chaque partie en entier.
    # n, p, q reçoivent ces trois entiers.
    
    n, p, q = map(int, raw_input().split())
    
    if n == 0:
        # Condition d'arrêt de la boucle.
        # Lorsque n vaut 0, cela signifie qu'il n'y a plus de données à traiter.
        break
    
    # Création d'une liste 'v' de 1440 éléments initialisés à 0.
    # 1440 correspond au nombre total de minutes dans une journée (24*60).
    # Cette liste sert à compter le nombre d'objectifs utilisés pour chaque minute de la journée.
    
    v = [0] * 1440
    
    for i in range(n):
        # Boucle qui parcourt chaque objectif.
        
        k = int(raw_input())
        # Lecture du nombre de plages horaires pour cet objectif.
        
        a = map(int, raw_input().split())
        # Lecture des plages horaires sous forme d'une liste d'entiers.
        # Chaque plage est donnée par deux entiers consécutifs : début et fin, au format HHMM.
        
        for j in range(k):
            # Boucle sur chaque plage horaire de l'objectif courant.
            
            # a[::2] est la sous-liste des horaires de début (indices pairs).
            # a[1::2] est la sous-liste des horaires de fin (indices impairs).
            # j parcourt donc chaque plage de temps.
            
            start_minute = cv(a[2 * j])    # Conversion de l'heure de début en minutes depuis minuit.
            end_minute = cv(a[2 * j + 1])  # Conversion de l'heure de fin en minutes depuis minuit.
            
            for l in range(start_minute, end_minute):
                # Pour chaque minute l de cette plage, on incrémente le compteur dans v.
                # Cela marque qu'à cette minute, cet objectif est actif.
                v[l] += 1
    
    # Initialisation de variables pour la recherche d'un intervalle maximal.
    # m stockera la longueur maximale d'un intervalle où toutes les conditions sont remplies.
    # c est un compteur temporaire pour la longueur courante.
    
    m = 0
    c = 0
    
    # Parcours des minutes entre p et q (convertis en minutes).
    start_period = cv(p)  # Conversion du début de période
    end_period = cv(q)    # Conversion de la fin de période
    
    for i in range(start_period, end_period):
        # Si le nombre d'objectifs actifs à la minute i est strictement inférieur à n,
        # alors l'intervalle peut être allongé (c incrementé).
        # Sinon, l'intervalle est interrompu, on remet c à 0.
        
        if v[i] < n:
            c += 1
            # On met à jour m si c dépasse sa valeur précédente.
            if c > m:
                m = c
        else:
            c = 0
    
    # Affichage du résultat : la longueur maximale (en minutes) de l'intervalle où
    # il y a au moins une plage horaire non couverte par tous les objectifs.
    
    print m