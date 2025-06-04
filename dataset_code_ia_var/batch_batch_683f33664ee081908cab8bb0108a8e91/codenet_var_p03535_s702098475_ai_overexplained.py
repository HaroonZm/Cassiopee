# Demander à l'utilisateur de saisir un entier qui sera assigné à la variable N.
# La fonction input() lit une ligne de texte en entrée, que l'on convertit ensuite en entier avec int().
N = int(input())

# Demander une deuxième ligne de saisie à l'utilisateur qui doit contenir des entiers séparés par des espaces.
# On utilise input().split() pour diviser cette chaîne en une liste de sous-chaînes correspondant aux nombres.
# Ensuite, on convertit chaque sous-chaîne en entier à l'aide d'une compréhension de liste.
D = [int(d) for d in input().split()]

# Créer une liste de 13 zéros, une pour chaque index de 0 à 12 inclus.
# Cette liste servira à compter combien de fois chaque valeur de 0 à 12 apparaît dans D.
Dcount = [0] * 13

# Pour chaque indice i de 0 à 12 (inclus),
# on utilise la méthode count() de la liste D pour connaître le nombre de fois que la valeur i apparaît dans D,
# et on stocke ce nombre dans Dcount au même indice i.
for i in range(13):
    Dcount[i] = D.count(i)

# Conditions d'arrêt immédiat (cas non valides) :
# Si Dcount[0] > 0, cela signifie que le nombre 0 apparaît au moins une fois, ce qui est interdit.
# Si Dcount[12] > 1, cela veut dire que la valeur 12 apparaît plus d'une fois, ce qui est également interdit.
# Dans l'un ou l'autre de ces cas, on affiche 0 puis on stoppe le programme (car aucune solution n'est possible).
if Dcount[0] > 0 or Dcount[12] > 1:
    print(0)
else:
    # Si nous sommes ici, alors 0 n'apparaît pas dans D, et 12 y apparaît tout au plus une fois.
    # À présent, nous vérifions si une valeur parmi 1 à 11 (Dcount[1:12]) apparaît trois fois ou plus.
    # Si c'est le cas, ce n'est pas autorisé et on arrête tout de suite avec print(0).
    for i in Dcount[1:12]:
        if i >= 3:
            print(0)
            break  # On quitte la boucle for car la condition d'arrêt est remplie
    else:
        # Ce qui suit s'exécutera seulement si le for précédent n'a PAS rencontré de break (c-à-d, tous les i < 3)
        
        # On commence par établir une liste 'base' contenant les valeurs 0 et 24.
        # Ces deux valeurs représentent deux points fixes du cercle horaire (0h et 24h, soit minuit).
        base = [0, 24]
        
        # Si la valeur 12 apparaît exactement une fois, on l'ajoute à base, car 12h et son point symétrique sont identiques sur l'horloge.
        if Dcount[12] == 1:
            base.append(12)
        
        # On prépare une liste vide 'Single' qui servira à stocker les valeurs dont la fréquence dans D est exactement de 1.
        Single = []
        
        # Pour chaque valeur i de 1 à 11 (inclus):
        for i in range(1, 12):
            if Dcount[i] == 2:
                # Si la valeur i apparaît deux fois, on ajoute i et son symétrique (24-i) à base.
                # Cela correspond à placer deux aiguilles à ces deux positions opposées sur l'horloge.
                base.append(i)
                base.append(24 - i)
            elif Dcount[i] == 1:
                # Si la valeur i apparaît une seule fois, on mémorise cette valeur dans Single pour un traitement ultérieur.
                Single.append(i)
        
        # Calculer le nombre d'éléments dans Single, c'est-à-dire le nombre de positions uniques à distribuer d'un côté ou de l'autre du cercle.
        lensingle = len(Single)
        
        # Initialiser la variable 'minmax' à 0, qui retiendra la longueur maximale du plus petit segment obtenu après chaque configuration possible.
        minmax = 0
        
        # Il y a 2^lensingle façons d'assigner à chaque élément de Single soit la valeur x, soit la valeur 24-x.
        # On itère donc sur toutes ces possibilités en générant tous les entiers de 0 à 2^lensingle - 1.
        for i in range(2**lensingle):
            # Copier la liste de base dans une nouvelle liste 'Clock' qui contiendra la configuration actuelle d'aiguilles sur l'horloge.
            Clock = base.copy()
            
            # 'i' représente une configuration binaire.
            # On la convertit en une chaîne binaire de longueur lensingle, complétée par des zéros si nécessaire (à gauche) pour que la longueur corresponde.
            bit = format(i, "b").zfill(lensingle)
            
            # Pour chaque index j de 0 à lensingle-1 :
            # Si le j-ème bit est "0", on ajoute Single[j] à Clock (donc côté direct),
            # sinon (bit "1"), on ajoute 24-Single[j] à Clock (le côté opposé du cercle).
            for j in range(lensingle):
                if bit[j] == "0":
                    Clock.append(Single[j])
                else:
                    Clock.append(24 - Single[j])
            
            # On trie la liste Clock pour mettre toutes les aiguilles dans l'ordre croissant,
            # ce qui facilite le calcul des intervalles horaires entre chaque aiguille.
            Clock.sort()
            
            # On initialise minsub à 24, la différence maximale possible (le tour complet du cercle).
            # minsub retiendra la plus petite différence (l'intervalle minimal entre deux aiguilles consécutives sur le cercle).
            minsub = 24
            
            # On parcourt Clock du 2ème élément jusqu'au dernier inclus, en comparant chaque élément à son précédent.
            # On calcule la différence entre deux positions consécutives, et on garde la différence la plus petite trouvée.
            for j in range(1, len(Clock)):
                minsub = min(minsub, Clock[j] - Clock[j-1])
            
            # Pour chaque configuration, on compare la plus petite différence (minsub) à la plus grande obtenue jusqu'ici (minmax).
            # On mémorise la plus grande (donc le meilleur cas parmi toutes les configurations testées).
            minmax = max(minmax, minsub)
        
        # Après avoir testé toutes les configurations possibles, afficher le résultat final.
        print(minmax)