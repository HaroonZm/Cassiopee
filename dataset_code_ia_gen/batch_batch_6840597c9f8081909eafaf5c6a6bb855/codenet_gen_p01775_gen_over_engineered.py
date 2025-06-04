import sys
import heapq
from typing import List, Tuple, Dict, Optional, Set

# --- Graph Abstractions ---

class Edge:
    def __init__(self, to: int, weight: int):
        self.to = to
        self.weight = weight

class Graph:
    def __init__(self, n_vertices: int):
        self.n = n_vertices
        self.adj = [[] for _ in range(n_vertices + 1)]  # 1-based indexing

    def add_edge(self, u: int, v: int, w: int):
        self.adj[u].append(Edge(v, w))
        self.adj[v].append(Edge(u, w))

    def dijkstra(self, start: int) -> List[Optional[int]]:
        dist = [None] * (self.n + 1)
        dist[start] = 0
        hq = [(0, start)]
        while hq:
            cd, cv = heapq.heappop(hq)
            if dist[cv] is not None and cd > dist[cv]:
                continue
            for e in self.adj[cv]:
                nd = cd + e.weight
                if dist[e.to] is None or nd < dist[e.to]:
                    dist[e.to] = nd
                    heapq.heappush(hq, (nd, e.to))
        return dist

# --- Postal Delivery Problem Interfaces and Implementation ---

class PostalItem:
    def __init__(self, pickup_vertex: int, delivery_vertex: int):
        self.pickup = pickup_vertex
        self.delivery = delivery_vertex

class State:
    def __init__(self, current_vertex: int, picked_mask: int, delivered_mask: int):
        self.current_vertex = current_vertex
        self.picked_mask = picked_mask
        self.delivered_mask = delivered_mask

    def __hash__(self):
        return hash((self.current_vertex, self.picked_mask, self.delivered_mask))

    def __eq__(self, other):
        return (self.current_vertex == other.current_vertex and
                self.picked_mask == other.picked_mask and
                self.delivered_mask == other.delivered_mask)

class PostalRescueSolver:
    def __init__(self, graph: Graph, postal_items: List[PostalItem], start: int):
        self.graph = graph
        self.items = postal_items
        self.start = start
        self.k = len(postal_items)
        # Precompute shortest paths between all relevant vertices for efficiency
        self.vertices_of_interest = self._get_vertices_of_interest()
        self.shortest_paths = self._compute_all_pairs_shortest_paths()

    def _get_vertices_of_interest(self) -> List[int]:
        # Including start, all pickup and delivery points
        verts = {self.start}
        for item in self.items:
            verts.add(item.pickup)
            verts.add(item.delivery)
        return list(verts)

    def _compute_all_pairs_shortest_paths(self) -> Dict[int, List[Optional[int]]]:
        # Map vertex -> distances array
        paths = {}
        for v in self.vertices_of_interest:
            paths[v] = self.graph.dijkstra(v)
        return paths

    def distance(self, from_v: int, to_v: int) -> Optional[int]:
        if from_v not in self.shortest_paths:
            # Should not happen
            return None
        return self.shortest_paths[from_v][to_v]

    def solve(self) -> Optional[int]:
        # State space defined by:
        # current position, bitmask indicating which items have been picked up,
        # bitmask indicating which items have been delivered.
        # Goal: all items delivered

        FULLDELIVER = (1 << self.k) - 1

        dist = dict()
        # Priority queue elements: (cost, State)
        start_state = State(self.start, 0, 0)
        dist[start_state] = 0
        pq = [(0, start_state)]

        # Map for quick vertex check of pickups and deliveries
        pickup_pos = {item.pickup: idx for idx, item in enumerate(self.items)}
        delivery_pos = {item.delivery: idx for idx, item in enumerate(self.items)}

        while pq:
            cost, state = heapq.heappop(pq)
            if dist.get(state, None) != cost:
                continue
            # Check if all delivered
            if state.delivered_mask == FULLDELIVER:
                return cost  # minimal cost found

            # For each possible next action: move to a relevant vertex to pick or deliver
            # We'll consider all vertices of interest: pickups and deliveries
            for v in self.vertices_of_interest:
                d = self.distance(state.current_vertex, v)
                if d is None:
                    continue
                ncost = cost + d
                # At vertex v, can pick up or deliver as possible
                new_picked_mask = state.picked_mask
                new_delivered_mask = state.delivered_mask

                # If v is a pickup location and item not yet picked
                if v in pickup_pos:
                    idx = pickup_pos[v]
                    if (new_picked_mask & (1 << idx)) == 0:
                        # Pick it up
                        new_picked_mask |= (1 << idx)

                # If v is a delivery location and corresponding item picked but not delivered
                if v in delivery_pos:
                    idx = delivery_pos[v]
                    if ((new_picked_mask & (1 << idx)) != 0) and ((new_delivered_mask & (1 << idx)) == 0):
                        # Deliver it
                        new_delivered_mask |= (1 << idx)

                new_state = State(v, new_picked_mask, new_delivered_mask)
                prev_cost = dist.get(new_state, None)
                if prev_cost is None or ncost < prev_cost:
                    dist[new_state] = ncost
                    heapq.heappush(pq, (ncost, new_state))
        return None

# --- Input Parsing and Execution ---

def main():
    input = sys.stdin.readline
    n,m,k,p = map(int, input().split())
    graph = Graph(n)
    for _ in range(m):
        x,y,w = map(int, input().split())
        graph.add_edge(x,y,w)
    postal_items = []
    for _ in range(k):
        s_i, t_i = map(int, input().split())
        postal_items.append(PostalItem(s_i,t_i))

    solver = PostalRescueSolver(graph, postal_items, p)
    ans = solver.solve()
    if ans is None:
        print("Cannot deliver")
    else:
        print(ans)

if __name__ == "__main__":
    main()