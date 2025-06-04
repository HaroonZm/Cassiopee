import sys
from typing import List, Dict, Optional, Iterator

class Node:
    """Classe représentant un noeud dans une structure chaînée circulaire doublement liée."""
    __slots__ = ['value', 'prev', 'next']
    def __init__(self, value: int):
        self.value: int = value
        self.prev: 'Node' = self
        self.next: 'Node' = self

    def insert_after(self, node: 'Node') -> None:
        """Insère un noeud après celui-ci."""
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

    def remove(self) -> None:
        """Retire ce noeud de la liste chaînée."""
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = self
        self.next = self

class CircularLinkedList:
    """
    Liste chaînée circulaire doublement liée avec un pivot implicite.
    Permet une rotation efficace autour d'un noeud spécifié.
    """
    def __init__(self):
        self.nodes_map: Dict[int, Node] = {}
        self.head: Optional[Node] = None
        self.size: int = 0

    def build_from_list(self, values: List[int]) -> None:
        """Construit la liste circulaire à partir d'une liste d'entiers."""
        prev_node: Optional[Node] = None
        for v in values:
            node = Node(v)
            self.nodes_map[v] = node
            if self.head is None:
                self.head = node
            if prev_node is not None:
                prev_node.next = node
                node.prev = prev_node
            prev_node = node
            self.size += 1
        # Fermer la boucle circulaire
        if self.head and prev_node:
            self.head.prev = prev_node
            prev_node.next = self.head

    def rotate_around_value(self, pivot_value: int) -> None:
        """
        Effectue la rotation suivant la description du problème:
        place le pivot_value au milieu, déplace la partie droite
        devant lui et la partie gauche après lui.
        """
        pivot_node = self.nodes_map[pivot_value]
        # La nouvelle tête sera la première à droite du pivot
        new_head = pivot_node.next
        # Si la liste est de taille 1, inutile de tourner
        if new_head == pivot_node:
            return
        # Fixer le pivot_head comme élément central
        # Le nouveau début est new_head
        # Il faut rebrancher pour que la rotation soit correcte
        # En fait, la rotation revient juste à changer la tête
        # en new_head; l'ordre circulaire reste le même
        self.head = new_head

    def to_list(self) -> List[int]:
        """Retourne la liste des valeurs dans l'ordre actuel débutant à head."""
        result = []
        if self.head is None:
            return result
        current = self.head
        for _ in range(self.size):
            result.append(current.value)
            current = current.next
        return result

class PivotPermutationSolver:
    """
    Classe abstraite englobant la résolution du problème de pivot sur la permutation.
    Encapsule les données, la logique et l'interface d'entrée/sortie.
    """
    def __init__(self, n: int, q: int, permutation: List[int], queries: List[int]):
        self.n = n
        self.q = q
        self.permutation = permutation
        self.queries = queries
        self.circular_list = CircularLinkedList()

    def solve(self) -> List[int]:
        """
        Résout la problématique: traite toutes les requêtes puis retourne la permutation finale.
        """
        self.circular_list.build_from_list(self.permutation)
        for pivot in self.queries:
            self.circular_list.rotate_around_value(pivot)
        return self.circular_list.to_list()

class InputParser:
    """Classe pour l'abstraction de la lecture et parsing des entrées depuis stdin."""
    def __init__(self, input_stream: Optional[Iterator[str]] = None):
        self.input_stream = input_stream or sys.stdin

    def parse(self) -> PivotPermutationSolver:
        line1 = next(self.input_stream).strip()
        n, q = map(int, line1.split())
        perm_line = next(self.input_stream).strip()
        permutation = list(map(int, perm_line.split()))
        query_line = next(self.input_stream).strip()
        queries = list(map(int, query_line.split()))
        return PivotPermutationSolver(n, q, permutation, queries)

class OutputPrinter:
    """Classe dédiée à l'affichage des résultats."""
    @staticmethod
    def print_permutation(permutation: List[int]) -> None:
        print(' '.join(map(str, permutation)))

def main() -> None:
    # Utilisation de l'abstraction d'entrée
    parser = InputParser(iter(sys.stdin.readline, ''))
    solver = parser.parse()
    result = solver.solve()
    OutputPrinter.print_permutation(result)

if __name__ == "__main__":
    main()