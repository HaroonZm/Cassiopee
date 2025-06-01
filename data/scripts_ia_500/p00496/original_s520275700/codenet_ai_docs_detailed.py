def solve():
    """
    Résout un problème d'optimisation combinatoire basé sur un temps total et une contrainte de seuil.

    L'objectif est de maximiser le "fun" total accumulé en choisissant un sous-ensemble d'activités,
    chacune ayant un niveau de "fun" et un "temps" requis.
    
    Contraintes spécifiques :
    - Il existe un temps total maximal T.
    - Un seuil critique S qui affecte la manière dont le temps est comptabilisé lors de la somme.

    Le programme utilise une programmation dynamique pour calculer la valeur maximale de "fun" 
    possible pour chaque temps jusqu'à T.
    
    Entrée :
    - N : le nombre d'activités
    - T : le temps total disponible
    - S : le seuil critique du temps
    - Une liste de N paires (fun, mise_time) pour chaque activité
    
    Sortie :
    - Un entier correspondant à la valeur maximale de "fun" que l'on peut obtenir dans les contraintes données.
    """
    # Lecture de l'entrée standard : nombre d'activités, temps total et seuil
    N, T, S = map(int, input().split())
    # Lecture des activités : chacune représentée par un tuple (fun, mise_time)
    a = [tuple(map(int, input().split())) for _ in range(N)]

    # Initialisation de la liste dp où dp[t] représente le meilleur score "fun" pour un temps total t
    # On utilise -inf pour représenter les temps non atteignables initialement
    dp = [float("-inf")] * (T + 1)
    dp[0] = 0  # Le fun maximum pour un temps de 0 est 0 (aucune activité choisie)

    # Parcours de chaque activité pour mise à jour progressive de dp
    for fun, mise_time in a:

        # On itère sur les temps possibles en partant de T - mise_time jusqu'à 0 inclus, 
        # dans l'ordre décroissant pour éviter de réutiliser plusieurs fois une même activité
        # Les trois listes sont parcourues en parallèle :
        #  - prev_time parcourt les temps précédents possibles
        #  - from_fun extrait dp[prev_time], représentant le fun accumulé avant d'ajouter l'activité actuelle
        #  - to_fun extrait dp[new_time], représentant le fun déjà enregistré pour le nouveau temps total possible
        for prev_time, from_fun, to_fun in zip(
            range(T - mise_time, -1, -1),   # temps avant d'ajouter l'activité
            dp[T - mise_time::-1],          # dp pour ces temps, parcouru en sens inverse
            dp[::-1]                       # dp pour nouveaux temps possibles, également en sens inverse
        ):
            # Calcul du nouveau temps total après ajout de l'activité
            new_time = prev_time + mise_time
            # Calcul du nouveau fun total après ajout de l'activité
            new_fun = fun + from_fun

            # Condition spéciale : si le précédent temps est < S mais que le nouveau temps dépasse S,
            # il faut ajuster le temps total en décalant l'ajout de mise_time au-delà du seuil S
            if prev_time < S < new_time:
                new_time = S + mise_time
                # Si ce nouveau temps dépasse la limite T, on ignore cette combinaison
                if new_time > T:
                    continue
                # On récupère le fun déjà accumulé pour ce temps ajusté
                to_fun = dp[new_time]

            # Mise à jour de dp[new_time] si on obtient un fun supérieur en choisissant cette activité
            if new_fun > to_fun:
                dp[new_time] = new_fun

    # Affiche le maximum dans dp : le maximum de "fun" total réalisable sous les contraintes
    print(max(dp))


if __name__ == "__main__":
    # Exécution de la fonction solve() uniquement lorsque ce script est exécuté en tant que programme principal
    solve()