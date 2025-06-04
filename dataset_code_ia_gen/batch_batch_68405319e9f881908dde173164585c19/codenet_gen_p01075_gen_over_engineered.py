import sys
import threading
from typing import List, Tuple, Dict, Optional
import heapq

class Edge:
    def __init__(self, from_island: int, to_island: int, tide_time: int):
        self.from_island = from_island
        self.to_island = to_island
        self.tide_time = tide_time

class IslandGraph:
    def __init__(self, num_islands: int):
        self.num_islands = num_islands
        # adjacency list: island -> list of edges
        self.adj: Dict[int, List[Edge]] = {i:[] for i in range(1, num_islands +1)}
    
    def add_bridge(self, from_island: int, to_island: int, tide_time: int):
        edge = Edge(from_island, to_island, tide_time)
        self.adj[from_island].append(edge)

class State:
    """
    Represents the arrival time at an island during the search, 
    facilitating a priority queue ordering by earliest arrival.
    """
    def __init__(self, island: int, arrival_time: int):
        self.island = island
        self.arrival_time = arrival_time
    
    def __lt__(self, other):
        return self.arrival_time < other.arrival_time

class OneTimePathSolver:
    def __init__(self, graph: IslandGraph):
        self.graph = graph
        self.N = graph.num_islands
        # earliest arrival time initialized as None, meaning unreachable yet
        self.earliest_arrival: List[Optional[int]] = [None] * (self.N + 1)
    
    def solve(self) -> int:
        """
        Performs a shortest path style search on the time-labeled edges 
        to find the maximum waiting time at islands before reaching the last island.
        Returns:
            max_wait_time (int) if reachable, else -1
        """
        # Initialize earliest arrival times
        self.earliest_arrival[1] = 0  # start island at time 0
        
        # Priority queue for Dijkstra-like approach pushing (arrival_time, island)
        heap: List[Tuple[int,int]] = []
        heapq.heappush(heap, (0,1))
        
        while heap:
            current_time, island = heapq.heappop(heap)
            if self.earliest_arrival[island] is not None and current_time > self.earliest_arrival[island]:
                continue
            # Explore neighbors
            for edge in self.graph.adj[island]:
                # Wait until bridge tide_time c_i
                if edge.tide_time >= current_time:
                    new_arrival = edge.tide_time
                    # If we can reach to_island earlier, update and push to heap
                    if (self.earliest_arrival[edge.to_island] is None or self.earliest_arrival[edge.to_island] > new_arrival):
                        self.earliest_arrival[edge.to_island] = new_arrival
                        heapq.heappush(heap, (new_arrival, edge.to_island))
        
        # If last island unreachable, return -1
        if self.earliest_arrival[self.N] is None:
            return -1
        
        # Compute max waiting time on islands before last island
        # According to problem, output the max arrival time at any island from 1 to N-1 along the path
        # The path is implicitly given by earliest arrivals that allowed arrival at N
        # Actually, we can safely return earliest_arrival[N], since waiting is max among islands before reaching N
        # Because arrival to N means waiting at previous island until that bridge's tide_time,
        # and arrival times to nodes are non-decreasing (waiting only).
        max_wait_time = -1
        for i in range(1, self.N):
            if self.earliest_arrival[i] is not None:
                if self.earliest_arrival[i] > max_wait_time:
                    max_wait_time = self.earliest_arrival[i]
        return max_wait_time

class InputHandler:
    def __init__(self):
        self.N = 0
        self.M = 0
        self.bridges: List[Tuple[int,int,int]] = []
    
    def read_input(self):
        self.N, self.M = map(int, sys.stdin.readline().split())
        for _ in range(self.M):
            a,b,c = map(int, sys.stdin.readline().split())
            self.bridges.append((a,b,c))

class OutputHandler:
    @staticmethod
    def print_result(result: int):
        print(result)

class OneTimePathApp:
    def __init__(self):
        self.input_handler = InputHandler()
        self.graph: Optional[IslandGraph] = None
        self.solver: Optional[OneTimePathSolver] = None
        self.output_handler = OutputHandler()
    
    def run(self):
        self.input_handler.read_input()
        self.graph = IslandGraph(self.input_handler.N)
        for (a,b,c) in self.input_handler.bridges:
            self.graph.add_bridge(a,b,c)
        self.solver = OneTimePathSolver(self.graph)
        answer = self.solver.solve()
        self.output_handler.print_result(answer)

def main():
    app = OneTimePathApp()
    app.run()

if __name__ == '__main__':
    threading.Thread(target=main,).start()