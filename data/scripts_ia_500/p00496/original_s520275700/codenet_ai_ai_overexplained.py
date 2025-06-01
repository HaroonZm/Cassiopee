def solve():
    # Lecture de la ligne d'entrée contenant trois entiers séparés par des espaces
    # N : nombre d'activités disponibles à choisir
    # T : temps total maximal disponible
    # S : seuil de temps particulier pour lequel une règle spéciale s'applique
    N, T, S = map(int, input().split())
    
    # Lecture des N lignes suivantes, chacune contenant deux entiers
    # Ces entiers représentent les caractéristiques d'une activité :
    # fun : le facteur de plaisir ou de score associé à l'activité
    # mise_time : le temps nécessaire pour réaliser cette activité
    # La compréhension de liste crée une liste de tuples (fun, mise_time)
    # [0]*N crée une liste de N éléments nuls, utilisé ici uniquement pour répéter l'action N fois
    a = [tuple(map(int, input().split())) for _ in [0]*N]
    
    # Initialisation d'un tableau dp (programmation dynamique) pour stocker les meilleurs scores fun atteignables
    # L'indice i de dp représente le temps total déjà utilisé
    # Chaque valeur dp[i] est la valeur maximale de fun obtenue en utilisant exactement i unités de temps
    # On initialise toutes les valeurs à moins l'infini (-inf) pour indiquer que ces états ne sont pas atteignables initialement
    dp = [float("-inf")] * (T+1)
    
    # Il est toujours possible de ne rien faire, donc la valeur de dp à 0 temps utilisé est 0 fun
    dp[0] = 0
    
    # On va parcourir chaque activité disponible, représentée par ses caractéristiques (fun, mise_time)
    for fun, mise_time in a:
        # Pour chaque activité, on effectue une mise à jour du tableau dp à l'envers (top-down)
        # Ceci évite de réutiliser plusieurs fois la même activité dans la même itération
        # zip permet de parcourir simultanément des plages et des sous-listes de dp dans le bon ordre
        # range(T-mise_time, -1, -1) itère sur les temps déjà atteignables avant d'ajouter cette activité
        # dp[T-mise_time::-1] correspond aux valeurs "from_fun", soit les scores atteints pour ces temps, parcourus à l'envers
        # dp[::-1] correspond aux valeurs "to_fun", les scores actuels pour le temps futur, dans l'ordre inverse
        for prev_time, from_fun, to_fun in zip(range(T-mise_time, -1, -1), dp[T-mise_time::-1], dp[::-1]):
            # Calcul du nouveau temps total une fois l'activité ajoutée
            new_time = prev_time + mise_time
            # Calcul du nouveau score fun total une fois l'activité ajoutée
            new_fun = fun + from_fun
            
            # Condition spéciale : si l'on dépasse le seuil S entre prev_time et new_time
            if prev_time < S < new_time:
                # Adaptation du temps considéré : le nouveau temps est décalé en ajoutant mise_time à S
                new_time = S + mise_time
                # Si ce nouveau temps dépasse le temps maximal T, on ignore cette mise à jour
                if new_time > T:
                    continue
                # on récupère le score déjà enregistré dans dp pour ce nouveau temps spécifique
                to_fun = dp[new_time]
            
            # Si la nouvelle valeur de fun calculée dépasse la valeur déjà présente pour ce nouveau temps,
            # on met à jour la valeur dp[new_time] avec ce nouveau score plus élevé
            if new_fun > to_fun:
                dp[new_time] = new_fun
    
    # Imprime le score fun maximal atteignable en utilisant au plus T unités de temps
    # max(dp) retourne la plus grande des valeurs dans la liste dp
    print(max(dp))

# Point d'entrée du script : si ce fichier est exécuté directement (pas importé),
# on appelle la fonction solve() pour démarrer l'algorithme
if __name__ == "__main__":
    solve()