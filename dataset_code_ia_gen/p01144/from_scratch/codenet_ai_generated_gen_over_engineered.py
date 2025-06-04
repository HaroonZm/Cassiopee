from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator


class Segment:
    """Représente un segment entre deux stations avec distance et probabilité d'attaque par unité de distance."""

    __slots__ = ('distance', 'attack_probability')

    def __init__(self, distance: int, attack_probability: float) -> None:
        self.distance = distance
        self.attack_probability = attack_probability

    def maximal_cost(self) -> int:
        """Calcule le coût maximal pour protéger entièrement ce segment."""
        return self.distance

    def maximal_expected_attack(self) -> float:
        """Calcule l'attaque attendue maximale sans protection."""
        return self.distance * self.attack_probability


class Dataset:
    """Encapsule un ensemble de segments ainsi que le budget disponible."""

    def __init__(self, n_segments: int, budget: int, segments: List[Segment]) -> None:
        self.n_segments = n_segments
        self.budget = budget
        self.segments = segments

    def total_distance(self) -> int:
        return sum(segment.distance for segment in self.segments)


class InputParser(ABC):
    """Interface abstraite pour le parsing des entrées."""

    @abstractmethod
    def parse(self) -> Iterator[Dataset]:
        pass


class StdInputParser(InputParser):
    """Parseur qui lit depuis l'entrée standard."""

    def parse(self) -> Iterator[Dataset]:
        import sys

        while True:
            line = sys.stdin.readline()
            if not line:
                break
            n_m = line.strip()
            if not n_m:
                continue
            n, m = map(int, n_m.split())
            if n == 0 and m == 0:
                break
            segments = []
            for _ in range(n):
                d_p_line = sys.stdin.readline().strip()
                d, p = d_p_line.split()
                segments.append(Segment(int(d), float(p)))
            yield Dataset(n, m, segments)


class ProtectorStrategy(ABC):
    """Stratégie pour minimiser les attaques par budget donné."""

    @abstractmethod
    def minimize_expected_attack(self, dataset: Dataset) -> float:
        pass


class GreedyProtectorStrategy(ProtectorStrategy):
    """
    Implémentation sophistiquée avec abstractions.
    Pour minimiser l'attaque : investir budget dans les segments avec la plus forte probabilité d'attaque par unité.
    Le protection coûte 1 unité d'argent par distance protégée, paie une distance partielle sur un segment est possible.
    """

    def minimize_expected_attack(self, dataset: Dataset) -> float:
        budget = dataset.budget
        # Segments triés par probabilité décroissante (car plus P_i élevé, mieux vaut protéger)
        sorted_segments = sorted(dataset.segments, key=lambda s: s.attack_probability, reverse=True)

        total_expected_attack = sum(s.maximal_expected_attack() for s in dataset.segments)
        remaining_budget = budget

        protected_distance = 0

        for segment in sorted_segments:
            if remaining_budget <= 0:
                break
            protectable = min(segment.distance, remaining_budget)
            # Réduction de l'attaque = P_i * distance protégée
            reduction = protectable * segment.attack_probability
            total_expected_attack -= reduction
            remaining_budget -= protectable
            protected_distance += protectable

        return total_expected_attack


class OutputPrinter(ABC):
    """Interface abstraite d'impression des résultats."""

    @abstractmethod
    def print_result(self, result: float) -> None:
        pass


class StdOutputPrinter(OutputPrinter):
    def print_result(self, result: float) -> None:
        # Le résultat est un float mais les exemples montrent un entier => conversion en int
        print(int(result))


class PrincessMarriageSolver:
    """Orchestration complète du problème."""

    def __init__(self,
                 input_parser: InputParser,
                 protector_strategy: ProtectorStrategy,
                 output_printer: OutputPrinter) -> None:
        self.input_parser = input_parser
        self.protector_strategy = protector_strategy
        self.output_printer = output_printer

    def solve_all(self) -> None:
        for dataset in self.input_parser.parse():
            result = self.protector_strategy.minimize_expected_attack(dataset)
            self.output_printer.print_result(result)


def main():
    solver = PrincessMarriageSolver(
        input_parser=StdInputParser(),
        protector_strategy=GreedyProtectorStrategy(),
        output_printer=StdOutputPrinter()
    )
    solver.solve_all()


if __name__ == "__main__":
    main()