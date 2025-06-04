import sys
from abc import ABC, abstractmethod
from typing import List, Set, Tuple, Dict, Optional, Iterator


class Vertex:
    def __init__(self, id_: int):
        self.id = id_
        self.adjacent: Set['Vertex'] = set()

    def connect(self, other: 'Vertex') -> None:
        self.adjacent.add(other)
        other.adjacent.add(self)

    def neighbors_ids(self) -> Set[int]:
        return {v.id for v in self.adjacent}


class Graph:
    def __init__(self, vertex_count: int):
        self.vertices: Dict[int, Vertex] = {i: Vertex(i) for i in range(1, vertex_count + 1)}

    def add_edge(self, a: int, b: int) -> None:
        self.vertices[a].connect(self.vertices[b])

    def edges(self) -> List[Tuple[int, int]]:
        recorded = set()
        result = []
        for v in self.vertices.values():
            for u in v.adjacent:
                if (u.id, v.id) not in recorded:
                    result.append((v.id, u.id))
                    recorded.add((v.id, u.id))
        return result

    def all_vertex_ids(self) -> List[int]:
        return list(self.vertices.keys())


class Question(ABC):
    @abstractmethod
    def query(self, guess: int) -> str:
        pass


class GameSession:
    def __init__(self, graph: Graph, input_stream= sys.stdin, output_stream=sys.stdout):
        self.graph = graph
        self.inp = input_stream
        self.out = output_stream

    def flush(self) -> None:
        self.out.flush()

    def ask(self, vertex: int) -> str:
        print(vertex, file=self.out)
        self.flush()
        response = self.inp.readline().strip()
        return response


class AbstractSolver(ABC):
    def __init__(self, graph: Graph, games_count: int):
        self.graph = graph
        self.K = games_count
        self.N = len(graph.vertices)

    @abstractmethod
    def solve(self, session: GameSession) -> None:
        pass


class VertexOrderStrategy:
    """
    Abstract strategy to decide order of guesses.
    Here we implement a trivial linear order strategy.
    """
    def __init__(self, graph: Graph):
        self.graph = graph
        self.order: List[int] = []

    def prepare(self) -> None:
        # Example strategy: simple list in ascending order
        self.order = sorted(self.graph.all_vertex_ids())

    def get_order(self) -> List[int]:
        return self.order


class GuessingSolver(AbstractSolver):
    """
    Sophisticated solver:
    Uses a stateful candidate set.
    Queries vertex guesses in order.
    Adapts candidates based on answers.
    The solver is designed to be extensible - multiple strategies, multiple candidate updates.
    """

    def __init__(self, graph: Graph, games_count: int):
        super().__init__(graph, games_count)
        self.strategy = VertexOrderStrategy(graph)

    def update_candidates(self, candidates: Set[int], guess: int, response: str) -> Set[int]:
        """
        Update remaining candidate set after guess and response
        'Yes' means guess is the correct vertex => only guess remains
        'Near' means answer is adjacent => candidates intersect neighbors of guess
        'No' means guess is neither correct nor adjacent => remove guess and neighbors
        """
        if response == "Yes":
            return {guess}
        elif response == "Near":
            neighbors = self.graph.vertices[guess].neighbors_ids()
            return candidates.intersection(neighbors)
        else:  # "No"
            excluded = self.graph.vertices[guess].neighbors_ids()
            excluded.add(guess)
            return candidates.difference(excluded)

    def solve_one_game(self, session: GameSession) -> None:
        candidates: Set[int] = set(self.graph.vertices.keys())
        self.strategy.prepare()
        order = self.strategy.get_order()

        questions_asked = 0

        # For complex updates, attempt adaptive querying up to 10 times.
        while questions_asked < 10 and len(candidates) > 1:
            # choose guess from candidates using the order list
            guess = next((v for v in order if v in candidates), None)
            if guess is None:
                # fallback: pick any candidate
                guess = next(iter(candidates))
            response = session.ask(guess)
            questions_asked += 1
            if response == "Yes":
                return
            candidates = self.update_candidates(candidates, guess, response)

        # If reduced candidates to single candidate but no "Yes" yet, guess it until success or probing exhausted
        for _ in range(10 - questions_asked):
            if len(candidates) == 0:
                # no candidates - fallback guess arbitrary vertex 1
                guess = 1
            else:
                guess = next(iter(candidates))
            response = session.ask(guess)
            if response == "Yes":
                return

    def solve(self, session: GameSession) -> None:
        for _ in range(self.K):
            self.solve_one_game(session)


class GraphGenerator:
    """
    Generates a connected graph optimized to help win within 10 queries.
    For simplicity, generates a simple chain (path) graph from 1 to N.
    Can be extended to other topologies.
    """

    def __init__(self, N: int):
        self.N = N
        self.graph = Graph(N)

    def generate_chain(self) -> None:
        for i in range(1, self.N):
            self.graph.add_edge(i, i + 1)

    def graph_output(self) -> Tuple[int, List[Tuple[int, int]]]:
        edges = self.graph.edges()
        return len(edges), edges


def main():
    # Read N K
    N, K = map(int, sys.stdin.readline().split())

    # Generate graph
    generator = GraphGenerator(N)
    # Use chain connected graph - simple and connected
    generator.generate_chain()
    M, edges = generator.graph_output()

    # Output graph specification
    print(M)
    for a, b in edges:
        print(a, b)
    sys.stdout.flush()

    # Build solver and session
    solver = GuessingSolver(generator.graph, K)
    session = GameSession(generator.graph, sys.stdin, sys.stdout)

    # Run solver to play K games
    solver.solve(session)


if __name__ == '__main__':
    main()