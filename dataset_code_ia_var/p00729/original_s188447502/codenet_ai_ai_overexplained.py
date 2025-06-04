def main():
    # Initialise une liste vide qui contiendra toutes les réponses
    ans_list = []

    # Cette boucle while tourne indéfiniment jusqu'à ce qu'on rencontre un signal d'arrêt
    while True:
        # On appelle la fonction solve(), qui retourne soit une liste de résultats, soit -1 pour signaler la fin
        ans = solve()
        # Si la réponse est -1, cela signifie qu'il faut arrêter la boucle
        if ans == -1:
            break
        # Sinon, on ajoute tous les résultats retournés par solve à ans_list
        ans_list += ans

    # Une fois que toutes les entrées ont été traitées,
    # on parcourt chaque élément de ans_list pour l'afficher
    for ans in ans_list:
        print(ans)

def solve():
    # Initialise une liste vide pour stocker les résultats de chaque requête
    res_list = []
    # Prend une ligne d'entrée et convertit les deux valeurs saisies (séparées par un espace) en entiers
    # Ces valeurs sont affectées à N et M respectivement
    N, M = map(int, input().split())
    # Si N et M valent tous les deux 0, cela indique la fin des données à traiter, on retourne -1
    if (N, M) == (0, 0):
        return -1

    # On construit une table sh (sheet) qui sera une liste de M sous-listes
    # Chaque sous-liste représente un objet/machine/salle et comporte un nombre d'éléments égal à la plage horaire en minutes (de 540 à 1260 inclus, soit 721 minutes)
    sh = [[0] * (1260 - 540 + 1) for _ in range(M)]
    
    # Prend un entier r qui indique le nombre d'enregistrements suivants
    r = int(input())
    # On lit r lignes de saisie, chacune décrivant un événement (ajout ou retrait d'occupation durant une minute particulière)
    for _ in range(r):
        # On lit t (minute absolue, de 0 à 1439), n, m (indice de l'objet, de 1 à M), s (état: 1=ajout, 0=suppression)
        t, n, m, s = map(int, input().split())
        # On convertit t pour qu'il commence à 0 à partir de 9h00 (540)
        t -= 540
        # On convertit m de base 1 (utilisateur) à base 0 (indice de la liste Python)
        m -= 1
        # Si s vaut 1, on augmente le compteur à la minute t pour l'objet m de 1
        if s == 1:
            sh[m][t] += 1
        # Si s vaut 0 (libération), on diminue le compteur à la minute t pour l'objet m de 1
        elif s == 0:
            sh[m][t] -= 1

    # Cette variable va accumuler l'état d'occupation (pour la propagate)
    acc = 0
    # On parcourt chaque sous-liste de la table (c'est-à-dire chaque objet/machine/salle) à travers l'index i
    for i, line in enumerate(sh):
        # Pour chaque minute (j) de l'objet m (ligne i), on tient compte de la variation des états
        for j, bit in enumerate(line):
            # On additionne le bit courant au compteur d'accumulation acc
            acc += bit
            # Si acc est supérieur ou égal à 1, cela indique qu'au moins une occupation est active à cette minute
            if acc >= 1:
                sh[i][j] = 1
            # Sinon, il n'y a pas d'occupation active, on met 0
            else:
                sh[i][j] = 0

    # Cette variable q contiendra le nombre de requêtes à traiter (par exemple demander le nombre d'occupations durant certains intervalles)
    q = int(input())
    # On lit q requêtes
    for _ in range(q):
        # Pour chaque requête, on lit ts (temps de début), te (temps de fin), m (indice de l'objet), tous en base 1
        ts, te, m = map(int, input().split())
        # On convertit ts et te de minutes totales à l'index dans la table sh (commence à 540)
        ts -= 540
        te -= 540
        # M passe de base 1 à base 0 pour l'accès à la liste Python
        m -= 1
        # On additionne tous les bits de sh[m][ts:te] pour obtenir le nombre d'occupations dans l'intervalle demandé pour l'objet m
        res = sum(sh[m][ts:te])
        # On ajoute ce résultat à la liste des résultats pour cette session solve
        res_list.append(res)
    # On retourne la liste des résultats
    return res_list

# Point d'entrée du programme principal
main()