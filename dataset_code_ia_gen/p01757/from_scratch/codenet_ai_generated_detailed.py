import sys
sys.setrecursionlimit(10**7)

def main():
    # Lecture des entrées
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    size = 2**n

    # Construire le tableau des rangs reçus initialement selon a et b
    rank_received = [0] * size
    for i in range(m):
        for idx in range(a[i], a[i+1]):
            rank_received[idx] = b[i]

    # Le problème demande de transformer ce classement reçu en un classement valide (sans contradictions)
    # selon la construction de tournoi décrite.

    # Observation clé:
    # - Un tournoi à élimination directe avec 2^n équipes a n tours.
    # - Chaque équipe gagne un certain nombre de tours (de 0 à n).
    # - Le rang d'une équipe est 2^n - nombre_de_victoires.
    #
    # Par conséquent, chaque équipe a un nombre de victoires entre 0 et n,
    # et le rang est strictement déterminé par ce nombre de victoires.
    #
    # Le classement possible est en fait une configuration d'éléments où la distribution des victoires suit la structure du tournoi:
    #
    # La structure du tournoi est hiérarchique : à chaque étape, on divise le tableau en blocs de taille 2^k,
    # on sélectionne les gagnants de chacun des sous-blocs et ils s'affrontent au tour suivant.
    #
    # L'objectif est donc de modifier le moins possible les rangs pour obtenir un classement compatible avec un arbre binaire parfait.
    #
    # On peut considérer une DP récursive qui, pour chaque segment [l, r),
    # essaie de construire une configuration de résultats sans contradiction
    # en regradant les sous-intervalles et mélangeant les résultats.
    #
    # On note dp(l, r) : 
    #   retourne la configuration minimale de victoires sur [l,r) et le nombre minimal de modifications requis.
    #
    # Ici cependant on veut limiter l'utilisation mémoire et temps :
    # On peut mémoriser pour chaque intervalle [l,r) tous les effets possibles pour le nombre de victoires remportés dans ce match final,
    # et le nombre minimal de modifications.
    #
    # Etant donné la taille pouvant aller jusqu'à 2^30 (très grande),
    # on ne peut pas traiter directement à cette échelle.
    #
    # Heureusement, le problème nous donne m (<=10000) segments consécutifs d'équipes avec le même rang.
    # On peut donc travailler avec des segments et les fusionner.
    #
    # On traite le problème par une approche bottom-up:
    # - Chaque segment de longueur 1 correspond à une équipe, possible nombre de victoires = n - rang_i
    # - On fusionne par paires de segments contigus
    #
    # Pour deux segments A et B avec leurs sets possibles de victoires (et coûts),
    # on calcule la fusion en choisissant qui gagne ce match, en augmentant de 1 le nombre de victoires.
    #
    # Implémentation:
    # - Représenter chaque segment par une liste de minimal cost pour chaque nombre de victoires possible
    #   - coût = nombre minimal de changements pour forcer les équipes de ce segment avec ce nombre de victoires final
    # - Pour segment singleton, le coût = 0 si on corrige le rang reçu pour correspondre, sinon 1
    # - Pour fusion, pour chaque choix du vainqueur et du perdant,
    #   on combine les coûts et choisit le min.
    #
    # Enfin, on retourne le minimal sur les victoires possibles dans le segment global.

    INF = 10**15

    # On commence par initialiser les segments de taille 1
    # Chaque segment est représenté par un tableau cost_victoires[v] = coût min avec v victoires attribuées aux équipes dans ce segment.
    # Pour taille 1 segment, une seule équipe, elle gagne 0 à 0 victoires (rangs possible entre 1 et 2^n)
    # Mais d'après le problème, rang = 2^n - victoires, donc victoires = 2^n - rang.
    # Cette équipe doit avoir des victoires entre 0 et n (car maximal n tours possible)
    # Si le rang reçu est rank_received[i], on calcule victoire=candid=2^n-rank_received[i]
    # Mais en réalité, le rang possible est de 1 à 2^n, donc victoires varies de 0 à n.
    # Donc victoires = n - (rank_received[i]-1) ??? Non, depuis rang_i= 2^n - victoires
    # => victoires = 2^n - rang_i, mais victoires <= n, ici 2^n peut être très grand,
    # ce qui est contradictoire.
    #
    # En fait, le problème dit:
    # Rang_i = 2^n - nombre_victoires_i
    # Donc
    # nombre_victoires_i = 2^n - rang_i
    #
    # Puisque nombre_victoires_i <= n, this implies that rang_i >= 2^n - n.
    # Mais le rang_i dans l'input est entre 0 et n. Il faut attention.
    #
    # En fait, les rangs donnés dans l'entrée varient entre 0 et n, ce n'est pas possible:
    # L'énoncé dit:
    # b_i <= n (les rangs dans l'entrée)
    #
    # "b_i (0 ≤ b_i ≤ n)" mais selon l'énoncé original, b_i est un rang, non victoires.
    # De plus, dans l'exemple:
    # Sample input 2:
    # b = [0,1,2]
    #
    # Donc il faut étudier ce que représente b_i:
    #
    # Dans le problème, ils disent que b_i est une valeur de rang, mais ils sont entre 0 et n.
    # Donc il s'agit d'une autre codification des rangs.
    #
    # En fait:
    # Le rang dans la sortie est entre 1 et 2^n
    # Mais dans l'entrée, les b_i peuvent être entre 0 et n (le problème le dit).
    #
    # On doit interpréter b_i comme le nombre de victoires.
    # Car dans le sample 1:
    # 1 1
    # 0 2
    # 1
    # signifie que les équipes 0 à 2 ont rang 1 (ou victoires 1?)
    #
    # Conclusion très probable:
    # Le b_i est le nombre de victoires dans l'entrée.
    #
    # En somme, "b_i" correspond au "nombre de victoires" pour toutes les équipes dans [a_i, a_{i+1}).
    #
    # Donc b_i est le nombre de victoires que toutes ces équipes ont d'après le manager.
    #
    # Ce qui simplifie la manipulation et la compréhension!
    #
    # On veut modifier le nombre de victoires des équipes pour obtenir une configuration valide minimisant le nombre de modifications.
    #
    # Donc rank_received[i] = b_j où i appartient à [a_j, a_(j+1))
    #
    # On peut alors initialiser un segment par :
    # cost[v] = nombre de modifications nécessaires pour que tous les éléments du segment aient v victoires
    # Ici, pour un segment constitué d'une unique équipe,
    # cost[v] = 0 si v == b[i], 1 sinon.
    #
    # Puis, en fusionnant 2 segments de même taille (2^k), on calcule le dp pour un segment de taille 2^{k+1} :
    # L'étape de fusion correspond à un match entre 2 blocs de taille 2^k, dont les meilleurs joueurs s'affrontent.
    #
    # Dans ce match:
    # On choisit un nombre de victoires w pour le vainqueur : il augmente de 1 victoires par rapport au bloc précédent.
    # Le perdant garde le nombre de victoires précédent.
    #
    # On doit tester toutes combinaisons possibles : 
    # (w pour vainqueur) x (v pour perdant) avec w = v + 1
    #
    # On ajoute 1 aux victoires pour le vainqueur dans le segment fusionné.
    #
    # On doit minimiser coût total.
    #
    # On répète jusqu'à fusionner tous les segments en un seul.

    # Initialisation des segments unitaires
    segments = []
    for i in range(size):
        cost = [INF]*(n+1)
        # b_i = le nombre de victoires selon l'entrée
        v = rank_received[i]
        for vic in range(n+1):
            cost[vic] = 1
        cost[v] = 0
        segments.append(cost)

    # Fonction pour fusionner deux segments
    # Chaque segment est une liste de coûts par nombre de victoires
    # On veut produire un segment fusionné de taille double.
    def merge(left, right):
        new_cost = [INF]*(n+1)
        # On teste toutes combinaisons possible des victoires des sous-segments
        # La règle du tournoi stipule que dans la fusion, les victoires du vainqueur augmentent de 1
        # Donc si left segment a victoires v1 et right segment v2,
        # soit left gagne => le nombre de victoires dans fusionné est v1+1
        # soit right gagne => c'est v2+1
        # Le perdant garde nombre de victoires non augmenté.
        for v_left in range(n+1):
            for v_right in range(n+1):
                # left gagne
                winner_victory = v_left + 1
                loser_victory = v_right
                if winner_victory <= n:
                    cost_val = left[v_left] + right[v_right]
                    if cost_val < new_cost[winner_victory]:
                        new_cost[winner_victory] = cost_val
                # right gagne
                winner_victory = v_right + 1
                loser_victory = v_left
                if winner_victory <= n:
                    cost_val = left[v_left] + right[v_right]
                    if cost_val < new_cost[winner_victory]:
                        new_cost[winner_victory] = cost_val
        return new_cost

    # Fusionner récursivement tous les segments par paires
    length = 1
    while length < size:
        new_segments = []
        for i in range(0, len(segments), 2):
            new_segments.append(merge(segments[i], segments[i+1]))
        segments = new_segments
        length *= 2

    # Le segment final contient les coûts pour toute la compétition
    # Le minimal des coûts pour toutes victoires possibles correspond au nombre minimal de modifications
    result = min(segments[0])
    print(result)

if __name__ == "__main__":
    main()