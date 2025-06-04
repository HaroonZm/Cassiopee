from heapq import heappop as pop  # Importe la fonction 'heappop' depuis le module 'heapq' et la renomme en 'pop'
from heapq import heappush as push  # Importe la fonction 'heappush' depuis le module 'heapq' et la renomme en 'push'

def main():
    # Lis les deux premiers entiers de l'entrée standard, qui seront n (nombre de sommets) et k (nombre d'arêtes)
    n, k = map(int, input().split())
    
    clst = []  # Liste qui stockera les coûts associés à chaque sommet
    rlst = []  # Liste qui stockera les portées/ranges pour chaque sommet
    
    # Pour chaque sommet, on lit sa valeur de coût et de portée depuis l'entrée
    for i in range(n):
        c, r = map(int, input().split())  # On lit deux entiers pour un sommet : c (coût), r (portée)
        clst.append(c)  # Ajoute le coût du sommet à la liste des coûts
        rlst.append(r)  # Ajoute la portée du sommet à la liste des portées
    
    # Création des listes d'adjacence pour chaque sommet
    # 'edges' est une liste de listes, où edges[i] contient la liste des voisins du sommet i
    edges = [[] * n for i in range(n)]  # Initialisation incorrecte (explication volontaire)
    # La méthode [[] * n for i in range(n)] donne n listes vides, car [] * n vaut []  
    # Cela crée une liste de n listes vides pour stocker les voisins de chaque sommet
    
    # Pour chaque arête, on lit les extrémités et on ajoute l’information aux listes d’adjacence
    for i in range(k):
        a, b = map(int, input().split())  # Lit les deux sommets connectés par l’arête (a, b)
        a -= 1  # Transformation de l’index en compte à partir de zéro (en Python, les listes commencent à l’indice 0)
        b -= 1
        edges[a].append(b)  # Ajoute b comme voisin de a
        edges[b].append(a)  # Ajoute a comme voisin de b (le graphe est non orienté)
    
    costs = [None] * n  # Liste pour stocker le coût minimum pour atteindre chaque sommet ; initialisée à None
    used = [False] * n  # Liste de booléens pour indiquer si un sommet a déjà été traité ; initialisé à False
    
    def make_to_lst(s_num):
        # Fonction pour déterminer les sommets accessibles depuis s_num grâce à sa portée
        loop = rlst[s_num]  # Nombre d'itérations égales à la portée du sommet courant (combien de bonds on peut faire)
        temp = set(edges[s_num])  # Ensemble des voisins immédiats du sommet actuel
        ret = set()  # Ensemble pour stocker tous les sommets atteints dans la portée
        
        # On va propager dans le graphe jusqu'à atteinte de la portée ou absence de nouveaux voisins
        while loop and temp:  # On continue tant qu’on a des étapes à parcourir et des voisins à explorer
            new = set()  # Ensemble temporaire pour stocker les nouveaux sommets trouvés à cette itération
            for p in temp:  # Pour chaque sommet dans le front courant
                pto = set(edges[p])  # On prend ses voisins
                new = new | pto  # On ajoute ses voisins à l'ensemble 'new'
            ret = ret | temp  # Ajoute tous les sommets du front courant à l’ensemble des déjà trouvés
            temp = new - ret  # Met à jour temp avec uniquement les nouveaux sommets non déjà atteints
            loop -= 1  # On décrémente le nombre d’étapes restantes dans la portée
        return ret  # Retourne l'ensemble de tous les sommets atteints depuis s_num dans la portée donnée
    
    used[0] = True  # On marque le sommet 0 comme déjà utilisé (point de départ)
    costs[0] = 0  # Le coût minimal pour atteindre le sommet de départ est 0
    que = [(clst[0], 0)]  # On initialise la file de priorité (le "tas") avec un tuple (coût, sommet initial)
    
    # Boucle principale de l'algorithme, semblable à Dijkstra, utilisant un tas/min-heap
    while que:  # Tant que la file de priorité n'est pas vide
        next_cost, s_num = pop(que)  # Extrait le sommet avec le coût le plus faible (priorité la plus haute)
        to_lst = make_to_lst(s_num)  # Détermine les sommets accessibles depuis s_num grâce à sa portée
        
        for num in to_lst:  # Boucle sur tous les sommets accessibles nouvellement
            if num == n - 1:  # Si on atteint le dernier sommet (but du problème)
                print(next_cost)  # On affiche le coût minimal pour l’atteindre
                return  # Fin de la fonction, donc du programme
            
            costs[num] = next_cost  # On enregistre le coût pour atteindre ce sommet
            
            if not used[num]:  # Si ce sommet n'a pas encore été traité
                push(que, (next_cost + clst[num], num))  # On l’ajoute à la file de priorité avec son coût
                used[num] = True  # On marque le sommet comme traité pour ne pas le retraiter
                

main()  # Appelle la fonction principale pour lancer le programme