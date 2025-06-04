from typing import List, Tuple, Dict, Optional, Any, Iterable
from collections import deque, defaultdict
from abc import ABC, abstractmethod
import sys

# --- Abstractions for Edges and Graphs ---

class Edge:
    __slots__ = ['frm', 'to', 'score']
    def __init__(self, frm: int, to: int, score: int):
        self.frm = frm
        self.to = to
        self.score = score

    def __repr__(self):
        return f"Edge({self.frm} -> {self.to}, score={self.score})"

class Graph(ABC):
    @abstractmethod
    def edges_from(self, node: int) -> Iterable[Edge]: ...
    @abstractmethod
    def nodes(self) -> Iterable[int]: ...

class DenseGraph(Graph):
    def __init__(self, V: int):
        self.V = V
        self.adj: List[List[Edge]] = [[] for _ in range(V)]

    def add_edge(self, frm:int, to:int, score:int) -> None:
        e = Edge(frm,to,score)
        self.adj[frm].append(e)

    def edges_from(self, node: int) -> Iterable[Edge]:
        return self.adj[node]

    def nodes(self) -> Iterable[int]:
        return range(self.V)

# --- Abstract base class for the solver ---

class SportsDaysSolver(ABC):
    def __init__(self, graph: Graph, target_score: int):
        self.graph = graph
        self.K = target_score

    @abstractmethod
    def solve(self) -> Optional[Tuple[int, List[int]]]:
        """
        Solve for optimal path:
        Returns None if impossible,
        else tuple of (number_of_edges, path as list of node indices)
        """
        ...

# --- Concrete solver implementation ---

class LayeredScoreSolver(SportsDaysSolver):
    """
    Uses a multi-layer BFS / dynamic programming approach:
    Layer represents the number of edges used so far (distance).
    At each layer, we track the max score reachable for each node.
    We track predecessors and edges used to support path reconstruction.
    We truncate search after 200 steps to avoid infinite loops and memory blowups.

    Since K can be up to 10^6 and edges add up small increments,
    and E can be large, this needs pruning cleverness.

    To ensure sophistication:
    - We keep layers as separate dicts mapping node -> max_score achievable at that distance.
    - Prune to keep only best score per node per layer.
    - We stop as soon as any score >= K is found, and choose minimal layer,
      if tie, maximal score.
    """

    MAX_EDGES_PATH_OUTPUT = 100
    MAX_SEARCH_DEPTH = 200  # max edges to consider in search to prevent explosion

    def solve(self) -> Optional[Tuple[int, List[int]]]:
        V = self.graph.V
        K = self.K

        # State per layer: node -> max score achievable at distance layer
        layers: List[Dict[int,int]] = [defaultdict(lambda: -1) for _ in range(self.MAX_SEARCH_DEPTH+1)]
        # predecessor trace: layer, node -> (prev_node, edge_score)
        predecessors: List[Dict[int, Tuple[int,int]]] = [{} for _ in range(self.MAX_SEARCH_DEPTH+1)]

        # Initialization: we can start at any cone with score 0 and 0 edges used
        for node in self.graph.nodes():
            layers[0][node] = 0  # start from node without moving, score=0

        # Search forward layer by layer
        best_result = None  # (edges_count, score, node, layer)
        for dist in range(self.MAX_SEARCH_DEPTH):
            current_layer = layers[dist]
            next_layer = layers[dist+1]
            next_predecessors = predecessors[dist+1]
            # For each node at current layer:
            for u, score_u in current_layer.items():
                if score_u < 0:
                    continue
                # Early check if best_result found and dist > best_result_edges, stop
                if best_result is not None and dist > best_result[0]:
                    break

                # Try all outgoing edges
                for e in self.graph.edges_from(u):
                    newscore = score_u + e.score
                    v = e.to
                    if newscore > next_layer[v]:
                        next_layer[v] = newscore
                        next_predecessors[v] = (u, e.score)
                        # Check if we reached the goal:
                        if newscore >= K:
                            # Candidate solution
                            if best_result is None:
                                best_result = (dist+1, newscore, v, dist+1)
                            else:
                                # Prioritize minimal edges, then max score
                                if dist+1 < best_result[0] or (dist+1 == best_result[0] and newscore > best_result[1]):
                                    best_result = (dist+1, newscore, v, dist+1)
            # Stop early if best result found
            if best_result is not None:
                break

        if best_result is None:
            # No path found reaching score>=K
            return None

        # Reconstruct path
        edges_count, final_score, end_node, end_layer = best_result

        # Backtrack nodes along predecessor chain
        path_nodes = []
        current_node = end_node
        current_layer = end_layer
        while current_layer > 0:
            path_nodes.append(current_node)
            pred_node, pred_edge_score = predecessors[current_layer][current_node]
            current_node = pred_node
            current_layer -= 1
        # add starting node (layer 0)
        path_nodes.append(current_node)
        path_nodes.reverse()

        # If edges_count > 100, do not output path nodes as per problem statement
        if edges_count > self.MAX_EDGES_PATH_OUTPUT:
            return (edges_count, [])
        return (edges_count, path_nodes)

# --- Interfaces for I/O and solving ---

class SportsDaysApplication:
    def __init__(self, input_stream=sys.stdin, output_stream=sys.stdout):
        self.input_stream = input_stream
        self.output_stream = output_stream

    def read_input(self) -> Tuple[int,int,int,List[Tuple[int,int,int]]]:
        input_iter = iter(self.input_stream.read().strip().split())
        V = int(next(input_iter))
        E = int(next(input_iter))
        K = int(next(input_iter))
        edges = []
        for _ in range(E):
            v1 = int(next(input_iter))
            v2 = int(next(input_iter))
            c = int(next(input_iter))
            edges.append((v1,v2,c))
        return V,E,K,edges

    def run(self):
        V,E,K,edges = self.read_input()
        graph = DenseGraph(V)
        for (frm,to,score) in edges:
            graph.add_edge(frm,to,score)
        solver = LayeredScoreSolver(graph,K)
        ans = solver.solve()
        if ans is None:
            print(-1,file=self.output_stream)
        else:
            edges_count, path_nodes = ans
            print(edges_count,file=self.output_stream)
            if path_nodes:
                print(*path_nodes,file=self.output_stream)

if __name__=="__main__":
    app = SportsDaysApplication()
    app.run()