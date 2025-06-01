import sys
import collections
from typing import List, Tuple, Dict, Set

class Graph:
    """ Représentation abstraite d'un graphe non orienté pour la modélisation des villes et des lignes ferroviaires. """
    def __init__(self, node_count: int):
        self.node_count = node_count
        self.adjacency: List[List[int]] = [[] for _ in range(node_count + 1)]
    
    def add_edge(self, u: int, v: int):
        self.adjacency[u].append(v)
        self.adjacency[v].append(u)
    
    def neighbors(self, node: int) -> List[int]:
        return self.adjacency[node]

class DistanceCalculator:
    """
    Calcule les distances minimales à poids unitaire dans un graphe par une BFS.
    Utilisé pour déterminer la distance initiale (tarif de base à 1 yen).
    """
    def __init__(self, graph: Graph, start_node: int):
        self.graph = graph
        self.start_node = start_node
        self.distances = [-1] * (graph.node_count + 1)
    
    def bfs(self):
        q = collections.deque()
        self.distances[self.start_node] = 0
        q.append(self.start_node)
        while q:
            cur = q.popleft()
            for nxt in self.graph.neighbors(cur):
                if self.distances[nxt] == -1:
                    self.distances[nxt] = self.distances[cur] + 1
                    q.append(nxt)
        return self.distances

class FareNetwork:
    """
    Réseau des lignes ferroviaires avec gestion avancée des hausses de tarifs.
    Chaque ligne a une arête et un prix (1 ou 2).
    On calcule les plus courts chemins dans ce graphe à poids 1 ou 2.
    """
    def __init__(self, n: int, edges: List[Tuple[int, int]]):
        self.n = n
        self.edges = edges
        # Indexation des arêtes pour mapping tarifaire et incréments.
        self.edge_id_map: Dict[Tuple[int,int], int] = {}
        self.graph = Graph(n)
        self.M = len(edges)
        for i, (u,v) in enumerate(edges, start=1):
            self.graph.add_edge(u,v)
            self.edge_id_map[(u,v)] = i
            self.edge_id_map[(v,u)] = i
        # Etat des tarifs: 1 initialement pour toutes les arêtes, 2 si augmentée
        self.fare_increased = [False] * (self.M + 1)
        # Mapping arêtes vers leur extrémité pour accès rapide
        self.edge_pairs = edges
    
    def increase_fare(self, edge_number: int):
        self.fare_increased[edge_number] = True
    
    def current_cost_graph(self):
        """
        Construit un graphe orienté pondéré par les tarifs actuels.
        Utilisé pour recalculer les distances après augmentations.
        """
        # Représentation par adjacency de (voisin, coût)
        adjacency_weighted = [[] for _ in range(self.n + 1)]
        for idx, (u,v) in enumerate(self.edge_pairs, start=1):
            cost = 2 if self.fare_increased[idx] else 1
            adjacency_weighted[u].append((v,cost))
            adjacency_weighted[v].append((u,cost))
        return adjacency_weighted
    
    def shortest_path_costs(self) -> List[int]:
        """
        Calcule les coûts minimums actuel du noeud 1 vers toutes les autres villes du graphe.
        Utilisation d'une Dijkstra efficace adaptée aux poids 1 ou 2, par méthode 0-1 BFS.
        """
        adjacency = self.current_cost_graph()
        INF = 1 << 60
        dist = [INF] * (self.n + 1)
        dist[1] = 0
        from collections import deque
        dq = deque([1])
        while dq:
            u = dq.popleft()
            for v, cost in adjacency[u]:
                nd = dist[u] + cost
                if nd < dist[v]:
                    dist[v] = nd
                    if cost == 1:
                        dq.appendleft(v)
                    else:
                        dq.append(v)
        return dist

class SatisfactionSurvey:
    """
    Module de calcul sophistiqué gérant tous les calculs de satisfaction pour chaque année
    intégrant l'abstraction complète de la planification, calculs de coûts, et analyses d'insatisfaction.
    """
    def __init__(self, n: int, m: int, q: int, edges: List[Tuple[int,int]], increase_plan: List[int]):
        self.n = n
        self.m = m
        self.q = q
        self.edges = edges
        self.increase_plan = increase_plan
        self.fare_network = FareNetwork(n, edges)
        # Calcul initial minimal costs avec coûts à 1 yen partout.
        self.initial_dist = DistanceCalculator(self.fare_network.graph, 1).bfs()
        # Inversion pour accès direction capitale vers les autres: initial_dist[k] correspond à coût minimal de 1 à k au départ (graph non pondéré)
        # Comme tous les tarifs initiaux sont 1, distance en nombre d'arêtes est égal au cout minimum initial.
    
    def compute_satisfaction_per_year(self) -> List[int]:
        """
        Calcule pour chaque année le nombre de villes insatisfaites (dont le coût min a augmenté).
        Procédure optimisée anticipant changements progressifs et mise à jour intelligente.
        """
        # Un compteur des villes insatisfaites par année
        unsatisfied_counts: List[int] = []
        # On stocke les distances précédentes, initialement distance initiale pondérée par 1 yen.
        current_dist = [d if d != -1 else 1 << 60 for d in self.initial_dist]
        
        # On traite chaque année, en augmentant progressivemment les tarifs sur une ligne.
        for year in range(self.q):
            route_to_increase = self.increase_plan[year]
            self.fare_network.increase_fare(route_to_increase)
            # Recalculer le coût minimal après l'augmentation sur la totalité (réseau pondéré à 1 ou 2)
            new_dist = self.fare_network.shortest_path_costs()
            # On compte les villes où la distance a augmenté par rapport à initial
            # On compare à initial_dist qui représente les coûts avant plan
            count_unsatisfied = 0
            for city in range(2, self.n+1):
                if new_dist[city] > self.initial_dist[city]:
                    count_unsatisfied += 1
            unsatisfied_counts.append(count_unsatisfied)
        return unsatisfied_counts

def parse_input() -> Tuple[int,int,int,List[Tuple[int,int]],List[int]]:
    input = sys.stdin.readline
    N,M,Q = map(int, input().split())
    edges = []
    for _ in range(M):
        u,v = map(int, input().split())
        edges.append((u,v))
    increase_plan = []
    for _ in range(Q):
        r = int(input())
        increase_plan.append(r)
    return N,M,Q,edges,increase_plan

def main():
    N,M,Q,edges,increase_plan = parse_input()
    survey = SatisfactionSurvey(N,M,Q,edges,increase_plan)
    results = survey.compute_satisfaction_per_year()
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    main()