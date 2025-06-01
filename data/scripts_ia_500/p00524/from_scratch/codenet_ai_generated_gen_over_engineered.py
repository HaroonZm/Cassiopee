import sys
import heapq
from collections import defaultdict, namedtuple
from abc import ABC, abstractmethod

class AbstractGraph(ABC):
    @abstractmethod
    def add_edge(self, u: int, v: int, cost: int) -> None:
        pass

    @abstractmethod
    def neighbors(self, u: int):
        pass

class Graph(AbstractGraph):
    Edge = namedtuple('Edge', ['to', 'cost'])
    
    def __init__(self, n_nodes: int):
        self.n = n_nodes
        self.adj = [[] for _ in range(n_nodes)]
    
    def add_edge(self, u: int, v: int, cost: int) -> None:
        self.adj[u].append(self.Edge(v, cost))
    
    def neighbors(self, u: int):
        return self.adj[u]

class Position:
    __slots__ = ['node', 'height']
    def __init__(self, node: int, height: int):
        self.node = node
        self.height = height
    
    def __eq__(self, other):
        return self.node == other.node and self.height == other.height
    
    def __hash__(self):
        return hash((self.node, self.height))

class State:
    __slots__ = ['time', 'node', 'height']
    def __init__(self, time: int, node: int, height: int):
        self.time = time
        self.node = node
        self.height = height
    
    def __lt__(self, other):
        return self.time < other.time

class HeightManager:
    def __init__(self, max_height: int):
        self.max_height = max_height
    
    def upward_cost(self, from_h: int, to_h: int) -> int:
        if to_h < from_h or to_h > self.max_height:
            return None
        return to_h - from_h
    
    def downward_cost(self, from_h: int, to_h: int) -> int:
        if to_h > from_h or to_h < 0:
            return None
        return from_h - to_h

class SugarGliderSolver:
    def __init__(self, n, m, x, heights, edges):
        self.N = n
        self.M = m
        self.initial_height = x
        self.heights = heights
        self.graph = Graph(n)
        for (a, b, t) in edges:
            self.graph.add_edge(a - 1, b - 1, t)
            self.graph.add_edge(b - 1, a - 1, t)
        self.height_managers = [HeightManager(heights[i]) for i in range(n)]
        
        # For optimization purposes, we'll discretize heights only on demand within search.
        # But since height can vary 0..H_i, we must think carefully.
        # Here we implement a best-first search on states (node, height).
        # We will store dist as dict of dict: dist[node][height] = time
        # But height up to 1e9 is huge, so we must avoid storing for all heights.
        # Observing allowed moves, and cost, we'll use a Dijkstra on minimal states.
        
    def solve(self):
        # Distance dict keyed by (node, height)
        dist = {}
        # priority queue: (time, node, height)
        # start at node=0 (tree 1), height=initial_height, time=0
        heap = []
        start_state = (0, 0, self.initial_height)
        heapq.heappush(heap, start_state)
        dist[(0, self.initial_height)] = 0
        
        target_node = self.N - 1
        target_height = self.heights[target_node]
        
        while heap:
            cur_t, cur_node, cur_h = heapq.heappop(heap)
            if dist.get((cur_node, cur_h), float('inf')) < cur_t:
                continue
            if cur_node == target_node and cur_h == target_height:
                return cur_t
            
            # 1) Vertical moves on the same tree: up/down by 1 meter with cost 1 second
            # Check up
            if cur_h < self.heights[cur_node]:
                next_h = cur_h + 1
                next_time = cur_t + 1
                key = (cur_node, next_h)
                if dist.get(key, float('inf')) > next_time:
                    dist[key] = next_time
                    heapq.heappush(heap, (next_time, cur_node, next_h))
            # Check down
            if cur_h > 0:
                next_h = cur_h - 1
                next_time = cur_t + 1
                key = (cur_node, next_h)
                if dist.get(key, float('inf')) > next_time:
                    dist[key] = next_time
                    heapq.heappush(heap, (next_time, cur_node, next_h))
            
            # 2) Jumping to other trees directly connected
            # jumping takes T seconds, height decreases by T meters
            # after jump: new height = cur_h - T
            # must satisfy 0 <= new height <= height of destination tree
            for edge in self.graph.neighbors(cur_node):
                to_node = edge.to
                jump_t = edge.cost
                new_h = cur_h - jump_t
                if new_h < 0 or new_h > self.heights[to_node]:
                    continue
                # time cost: jump_t seconds (height falls simultaneously)
                next_time = cur_t + jump_t
                key = (to_node, new_h)
                if dist.get(key, float('inf')) > next_time:
                    dist[key] = next_time
                    heapq.heappush(heap, (next_time, to_node, new_h))
        
        return -1

def main():
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    heights = [int(input()) for _ in range(N)]
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    solver = SugarGliderSolver(N, M, X, heights, edges)
    print(solver.solve())

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    main()