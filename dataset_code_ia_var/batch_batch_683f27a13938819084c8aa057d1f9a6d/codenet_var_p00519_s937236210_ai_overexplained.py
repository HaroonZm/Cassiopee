from heapq import heappop as pop  # Importer la fonction heappop du module heapq et la renommer en 'pop'
from heapq import heappush as push  # Importer la fonction heappush du module heapq et la renommer en 'push'

INF = 10 ** 20  # Définir une constante pour représenter l'infini (une très grande valeur)

def main():  # Définir la fonction principale du programme
    # Lire deux entiers depuis l'entrée standard et les assigner à n et k
    # 'n' représente le nombre de sommets (ou nœuds), 'k' le nombre d'arêtes (ou liaisons)
    n, k = map(int, input().split())
    
    clst = []  # Créer une liste vide pour stocker les coûts de chaque sommet
    rlst = []  # Créer une liste vide pour stocker la portée (range) de chaque sommet
    
    # Boucle pour lire les valeurs de chaque sommet, une ligne à la fois
    for i in range(n):  # Répéter n fois, pour chaque sommet
        # Lire deux entiers : c pour le coût du sommet, r pour la portée
        c, r = map(int, input().split())
        clst.append(c)  # Ajouter le coût c à la liste clst
        rlst.append(r)  # Ajouter la portée r à la liste rlst
    
    # Initialiser la liste des arêtes (ou voisins) pour chaque sommet.
    # Chaque sous-liste représente les sommets adjacents à un sommet donné.
    edges = [[] * n for i in range(n)]  # Cela crée n listes vides 
    # Correction : [[] * n for i in range(n)] crée n listes vides car [] * n reste [].
    # Mais le code initial a cette erreur volontaires, donc à documenter :
    # Cela crée n listes identiques (toutes sont '[]') - ceci est techniquement équivalent à [ [] for i in range(n) ] ici
    
    # Pour chaque arête donnée, lire ses extrémités et remplir la liste d'adjacence
    for i in range(k):  # Répéter k fois pour chaque arête
        a, b = map(int, input().split())  # Lire deux entiers : les indices des sommets reliés
        a -= 1  # Décrémenter de 1 pour passer à l'indexation à partir de zéro (Python : listes commencent à 0)
        b -= 1
        edges[a].append(b)  # Ajouter b à la liste d'adjacence de a
        edges[b].append(a)  # Ajouter a à la liste d'adjacence de b (graphe non orienté)
    
    # Initialiser une liste des coûts pour atteindre chaque sommet ; tous à l'infini, sauf le début
    costs = [INF for i in range(n)]  # Liste de taille n, initialisée à 'infini'
    costs[0] = 0  # Coût pour atteindre le premier sommet (sommet 0) est 0
    
    # Initialiser une liste de booléens pour marquer si un sommet a été utilisé (visité)
    used = [False for i in range(n)]  # Tous faux au départ
    
    # Définir une fonction interne qui génère l'ensemble de sommets accessibles
    # à partir d'un sommet donné (s_num) selon sa portée (rlst[s_num])
    def make_to_lst(s_num):
        loop = rlst[s_num]  # La variable 'loop' contient la portée (range) de propagation
        temp = set(edges[s_num])  # 'temp' est un ensemble contenant les voisins directs du sommet courant
        ret = set()  # 'ret' rassemblera tous les sommets atteints
        while loop:  # Répéter tant qu'il reste de la portée
            new = set()  # Ensemble pour stocker temporairement les nouveaux sommets trouvés cette itération
            for p in temp:  # Pour chaque sommet accessible à cette distance
                pto = set(edges[p])  # Trouver ses voisins
                new = new | pto  # Ajouter ces voisins à 'new' (union d'ensembles)
            ret = ret | temp  # Ajouter tous les sommets découverts cette itération à 'ret'
            temp = new - ret  # Pour l'itération suivante, prendre les nouveaux inconnus seulement
            if not temp:  # Si aucun nouveau sommet n'est découvert
                break  # Arrêter la boucle
            loop -= 1  # Réduire la portée restante
        return ret  # Retourner l'ensemble des sommets accessibles
    
    used[0] = True  # Marquer le sommet de départ (0) comme utilisé (visité)
    costs[0] = 0  # Coût pour atteindre le sommet 0 est 0 (répété pour confirmation)
    break_flag = 0  # Drapeau utilisé pour sortir de la boucle principale en cas de succès
    que = [(clst[0], 0)]  # Initialiser la file de priorité (min-heap) avec un tuple : (coût, numéro de sommet)
    
    # Boucle principale (style Dijkstra étendu) : tant qu'il reste des éléments dans la file et qu'on n'a pas atteint la fin
    while que and not break_flag:
        next_cost, s_num = pop(que)  # Retirer le sommet avec le coût le plus faible de la file
        to_lst = make_to_lst(s_num)  # Trouver tous les sommets atteignables depuis s_num selon sa portée
        
        for num in to_lst:  # Pour chaque sommet accessible
            costs[num] = next_cost  # Mettre à jour le coût d'accès à ce sommet (au coût courant)
            if num == n - 1:  # Si ce sommet est le dernier sommet (objectif)
                break_flag = 1  # Déclencher le drapeau d'arrêt
                break  # Sortir de la boucle for
            if not used[num]:  # Si ce sommet n'a pas encore été visité
                push(que, (costs[num] + clst[num], num))  # Placer dans la file avec son coût cumulé
                used[num] = True  # Marquer comme visité
    
    # Une fois la boucle (algorithme terminé), afficher le coût pour atteindre le dernier sommet
    print(costs[n - 1])

# Appeler la fonction principale pour lancer le programme depuis le début
main()