from typing import List, Tuple, Dict, Optional
import sys
import heapq


class BusEdge:
    """
    Représente un trajet de bus entre deux arrêts,
    avec l'heure de départ t et la durée c.
    """
    __slots__ = ('to', 'depart_time', 'duration')

    def __init__(self, to: int, depart_time: int, duration: int):
        self.to = to
        self.depart_time = depart_time
        self.duration = duration

    def arrival_time(self) -> int:
        return self.depart_time + self.duration


class BusStop:
    """
    Représente un arrêt de bus avec sa liste d'itinéraires sortants.
    """
    __slots__ = ('index', 'edges')

    def __init__(self, index: int):
        self.index = index
        self.edges: List[BusEdge] = []

    def add_edge(self, edge: BusEdge):
        self.edges.append(edge)

    def prepare(self):
        """
        Trie les trajets par heure de départ pour optimisation.
        Utile pour des recherches futures, extensions ou optimisations.
        """
        self.edges.sort(key=lambda e: e.depart_time)


class RainExposureState:
    """
    Représente l'état de l'exposition à la pluie lors du parcours.
    stocke le temps min de pluie accumulé et le temps d'arrivée.
    """
    __slots__ = ('rain_time', 'arrival_time')

    def __init__(self, rain_time: int, arrival_time: int):
        self.rain_time = rain_time
        self.arrival_time = arrival_time

    def __lt__(self, other: 'RainExposureState'):
        """
        Priorité basée sur le temps d'exposition à la pluie minimal.
        En cas d'égalité, on privilégie l'arrivée plus tôt.
        """
        if self.rain_time == other.rain_time:
            return self.arrival_time < other.arrival_time
        return self.rain_time < other.rain_time


class RainyBusRoutePlanner:
    """
    Planificateur d'itinéraire sous la pluie, minimisant le temps d'exposition.
    Implémente une version sophistiquée adaptée à la montée en complexité.
    """

    def __init__(self, n: int, m: int, start: int, goal: int):
        self.n = n
        self.m = m
        self.start = start
        self.goal = goal
        self.bus_stops: List[BusStop] = [BusStop(i) for i in range(n + 1)]
        # Utilisé pour stocker le minimum de temps de pluie pour chaque arrêt
        self.min_rain_time: List[Optional[int]] = [None] * (n + 1)
        # Stocke le meilleur temps d'arrivée pour dédramatiser les égalités
        self.best_arrival_time: List[Optional[int]] = [None] * (n + 1)

    def add_route(self, u: int, v: int, t: int, c: int):
        self.bus_stops[u].add_edge(BusEdge(v, t, c))

    def prepare(self):
        for stop in self.bus_stops:
            stop.prepare()

    def plan(self) -> int:
        """
        Applique une forme modifiée de Dijkstra où le coût est la durée sous la pluie.
        Chaque noeud stocke la meilleure exposition à la pluie déjà calculée.
        """
        # Initialisation: au départ, on commence à temps 0 et aucun temps sous pluie
        self.min_rain_time[self.start] = 0
        self.best_arrival_time[self.start] = 0
        queue: List[Tuple[int, int, int]] = []
        # (rain_time, arrival_time, bus_stop_index)
        heapq.heappush(queue, (0, 0, self.start))

        while queue:
            curr_rain, curr_time, u = heapq.heappop(queue)
            # Si on a déjà une meilleure solution connue, on continue
            if (self.min_rain_time[u] is not None and curr_rain > self.min_rain_time[u]) or \
               (self.min_rain_time[u] == curr_rain and curr_time > self.best_arrival_time[u]):
                continue
            if u == self.goal:
                # Nous sommes arrivés au but: le temps sous pluie minimal est trouvé
                return curr_rain

            stop = self.bus_stops[u]
            for edge in stop.edges:
                # Calcul du temps d'attente (temps sous la pluie)
                wait_time = max(0, edge.depart_time - curr_time)
                # Temps total sous la pluie accumulé
                new_rain = curr_rain + wait_time
                # Temps d'arrivée à l'arrêt suivant
                arrival = edge.depart_time + edge.duration

                # Si nous n'avons encore aucune meilleure solution ou une pire que celle-ci
                if (self.min_rain_time[edge.to] is None) or \
                   (new_rain < self.min_rain_time[edge.to]) or \
                   (new_rain == self.min_rain_time[edge.to] and arrival < self.best_arrival_time[edge.to]):
                    self.min_rain_time[edge.to] = new_rain
                    self.best_arrival_time[edge.to] = arrival
                    heapq.heappush(queue, (new_rain, arrival, edge.to))

        # Dans l'énoncé, on est assuré d'atteindre l'objectif, mais en cas d'erreur:
        return -1


def main():
    input = sys.stdin.readline
    N, M, S, G = map(int, input().split())
    planner = RainyBusRoutePlanner(N, M, S, G)
    for _ in range(M):
        u, v, t, c = map(int, input().split())
        planner.add_route(u, v, t, c)
    planner.prepare()
    print(planner.plan())


if __name__ == '__main__':
    main()