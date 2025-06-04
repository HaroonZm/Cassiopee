from __future__ import annotations
from typing import List, Dict, Tuple, Optional, Iterator
import sys
import re

class Polynomial:
    """
    Represents a polynomial with nonnegative coefficients, where index is the degree.
    Supports addition and max (pointwise max of coefficients).
    Polynomials are immutable.
    """
    def __init__(self, coefficients: Optional[List[int]] = None):
        # coefficients[i] = coefficient for x^i
        if coefficients is None:
            self.coeffs = []
        else:
            # remove trailing zeros
            self.coeffs = coefficients[:]
            self._trim()
    
    @classmethod
    def zero(cls) -> Polynomial:
        return cls([0])

    @classmethod
    def from_string(cls, s: str) -> Polynomial:
        """
        Parse polynomial from input format:
        Examples:
         - 2x^3+x  ->  deg 3 coeffs: [0,0,0,2], with x term coeff 1
         - x+2     ->  deg 1 coeffs: [2,1]
         - 5       ->  deg 0 coeffs: [5]
        """
        terms = s.split("+")
        coeff_dict: Dict[int,int] = {}
        for term in terms:
            term = term.strip()
            if 'x' not in term:
                # constant term
                coeff_dict[0] = int(term)
            else:
                # term contains x
                # regex: possible patterns:
                #  x^d  => implicit 1 coefficient
                #  3x^d
                #  x
                #  3x
                m = re.fullmatch(r'(?:(\d+))?x(?:\^(\d+))?', term)
                if m is None:
                    raise ValueError(f"Invalid term in polynomial: {term}")
                a, d = m.group(1), m.group(2)
                coeff = int(a) if a is not None else 1
                degree = int(d) if d is not None else 1
                coeff_dict[degree] = coeff_dict.get(degree,0) + coeff
        max_degree = max(coeff_dict.keys()) if coeff_dict else 0
        coeffs = [0]*(max_degree+1)
        for deg, val in coeff_dict.items():
            coeffs[deg] = val
        return cls(coeffs)

    def _trim(self):
        # remove trailing zeros to keep canonical form, but keep zero polynomial as [0]
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()
        if not self.coeffs:
            self.coeffs = [0]

    def degree(self) -> int:
        return len(self.coeffs)-1

    def __add__(self, other: Polynomial) -> Polynomial:
        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = []
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len(self.coeffs) else 0
            c2 = other.coeffs[i] if i < len(other.coeffs) else 0
            new_coeffs.append(c1 + c2)
        return Polynomial(new_coeffs)

    def __lt__(self, other: Polynomial) -> bool:
        """
        Defines lex order reversed for max:
        highest degree checked first:
        returns True if self < other in degree-wise comparison,
        i.e. when other is lexicographically larger in highest degree coefficients.
        """
        max_deg = max(self.degree(), other.degree())
        for d in range(max_deg, -1, -1):
            c1 = self.coeffs[d] if d <= self.degree() else 0
            c2 = other.coeffs[d] if d <= other.degree() else 0
            if c1 != c2:
                return c1 < c2
        return False  # equal means self not < other

    def max_coefficients(self, other: Polynomial) -> Polynomial:
        """
        Compute polynomial with coef[i] = max(self.coeffs[i], other.coeffs[i])
        """
        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = []
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len(self.coeffs) else 0
            c2 = other.coeffs[i] if i < len(other.coeffs) else 0
            new_coeffs.append(max(c1,c2))
        return Polynomial(new_coeffs)

    def __repr__(self):
        return f"Polynomial({self.coeffs})"

    def __str__(self) -> str:
        # Output polynomial format as specified
        # constant zero polynomial -> "0"
        if self.degree() == 0 and self.coeffs[0] == 0:
            return "0"
        terms = []
        for d in range(self.degree(), -1, -1):
            c = self.coeffs[d]
            if c == 0:
                continue
            if d == 0:
                terms.append(str(c))
            elif d == 1:
                # linear term
                if c == 1:
                    terms.append("x")
                else:
                    terms.append(f"{c}x")
            else:
                # d >= 2
                if c == 1:
                    terms.append(f"x^{d}")
                else:
                    terms.append(f"{c}x^{d}")
        return "+".join(terms)

class Edge:
    """
    Represents a bidirectional edge with a polynomial bandwidth
    """
    def __init__(self, u: int, v: int, bandwidth: Polynomial):
        self.u = u
        self.v = v
        self.bandwidth = bandwidth

    def other(self, node: int) -> int:
        if node == self.u:
            return self.v
        elif node == self.v:
            return self.u
        else:
            raise ValueError(f"Node {node} not in edge {self.u}-{self.v}")

class BaseStationGraph:
    """
    Graph abstraction representing the network of base stations.
    Nodes labeled 1..N
    Uses adjacency list: node -> List[Edge]
    """
    def __init__(self, n: int):
        self.n = n
        self.adj: Dict[int, List[Edge]] = {i: [] for i in range(1,n+1)}

    def add_edge(self, u: int, v: int, bandwidth: Polynomial):
        edge = Edge(u,v,bandwidth)
        self.adj[u].append(edge)
        self.adj[v].append(edge)

    def max_bandwidth_path(self, start:int, end:int) -> Polynomial:
        """
        Computes the maximal bandwidth polynomial path from start to end base stations.
        Since bandwidths are polynomials, the 'max' between two bandwidth polynomials is defined coefficient-wise max,
        and path bandwidth is sum of bandwidth polynomials on edges.

        The problem reduces to finding a path between start and end maximizing the sum polynomial in lex order.

        We use a variant of Dijkstra-like algorithm customized for polynomial "weights"
        with relaxation using polynomial addition and lex max comparison.

        Since polynomials are nonnegative coefficients, no negative cycles.
        """
        dist: Dict[int, Polynomial] = {i: Polynomial.zero() for i in range(1,self.n+1)}
        dist[start] = Polynomial.zero()
        visited = set()
        # Priority queue with (negated polynomial dist for max), node
        # We implement using a binary heap with negated polynomial => inverted compare, so invert __lt__ for Polynomial
        # Instead we implement a custom priority queue keyed by a tuple which uses lex order on coefficients reversed
        import heapq

        class PrioritizedItem:
            def __init__(self, poly: Polynomial, node: int):
                self.poly = poly
                self.node = node
            def __lt__(self, other: PrioritizedItem) -> bool:
                # invert order because heapq is min-heap, but we want max polynomial
                # so self < other means self.poly > other.poly for max heap effect
                return other.poly < self.poly

        heap: List[PrioritizedItem] = [PrioritizedItem(Polynomial.zero(), start)]
        heapq.heapify(heap)

        while heap:
            current = heapq.heappop(heap)
            u = current.node
            if u in visited:
                continue
            visited.add(u)
            if u == end:
                return dist[u]
            from_u = dist[u]
            for edge in self.adj[u]:
                v = edge.other(u)
                if v in visited:
                    continue
                new_poly = from_u + edge.bandwidth
                if dist[v] < new_poly:
                    dist[v] = new_poly
                    heapq.heappush(heap, PrioritizedItem(new_poly, v))
        # no path
        return Polynomial.zero()

class InputParser:
    def __init__(self, input_stream: Iterator[str]):
        self.stream = input_stream

    def __iter__(self) -> Iterator[Tuple[int,int,List[Tuple[int,int,str]]]]:
        return self

    def __next__(self) -> Tuple[int,int,List[Tuple[int,int,str]]]:
        while True:
            line = next(self.stream).strip()
            if line == "":
                continue
            N,M = map(int,line.split())
            if N == 0 and M == 0:
                raise StopIteration
            edges = []
            for _ in range(M):
                line = next(self.stream).strip()
                u,v,p = self._parse_edge_line(line)
                edges.append((u,v,p))
            return (N,M,edges)

    def _parse_edge_line(self, line: str) -> Tuple[int,int,str]:
        # line looks like: u v polynomial_string (polynomial has no spaces)
        # Separate first two ints then the rest as polynomial string
        parts = line.split(maxsplit=2)
        u = int(parts[0])
        v = int(parts[1])
        p_str = parts[2] if len(parts) > 2 else ""
        return (u,v,p_str)

def main():
    parser = InputParser(iter(sys.stdin))
    for N,M,edges in parser:
        graph = BaseStationGraph(N)
        for (u,v,p_str) in edges:
            p = Polynomial.from_string(p_str)
            graph.add_edge(u,v,p)
        max_bw = graph.max_bandwidth_path(1, N)
        print(str(max_bw))

if __name__ == "__main__":
    main()