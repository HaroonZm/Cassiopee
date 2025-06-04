from abc import ABC, abstractmethod
from typing import List, Tuple


class InterestStrategy(ABC):
    """
    Abstract base class for interest calculation strategy.
    """

    def __init__(self, rate: float):
        self.rate = rate

    @abstractmethod
    def calculate_year_end(self, principal: int, accumulated_interest: int) -> Tuple[int, int]:
        """
        Calculate the interest and update principal or accumulated interest accordingly.
        Returns a tuple (new_principal, new_accumulated_interest).
        """
        pass

    def compute_interest(self, principal: int) -> int:
        # Interest rounded down to nearest integer
        return int(principal * self.rate)


class SimpleInterestStrategy(InterestStrategy):
    """
    Implements simple interest calculation.
    """

    def calculate_year_end(self, principal: int, accumulated_interest: int) -> Tuple[int, int]:
        interest = self.compute_interest(principal)
        # The interest does not add to principal but accumulates separately
        return principal, accumulated_interest + interest


class CompoundInterestStrategy(InterestStrategy):
    """
    Implements compound interest calculation.
    """

    def calculate_year_end(self, principal: int, accumulated_interest: int) -> Tuple[int, int]:
        interest = self.compute_interest(principal)
        # Interest is added to principal for next year
        return principal + interest, accumulated_interest


class Operation:
    """
    Represents an operation company offer.
    """

    SIMPLE_INTEREST = '0'
    COMPOUND_INTEREST = '1'

    def __init__(self, interest_type: str, rate: float, annual_charge: int):
        self.interest_type = interest_type
        self.rate = rate
        self.annual_charge = annual_charge
        self.strategy = self._init_strategy()

    def _init_strategy(self) -> InterestStrategy:
        if self.interest_type == self.SIMPLE_INTEREST:
            return SimpleInterestStrategy(self.rate)
        elif self.interest_type == self.COMPOUND_INTEREST:
            return CompoundInterestStrategy(self.rate)
        else:
            raise ValueError(f"Unknown interest type: {self.interest_type}")

    def simulate(self, principal: int, years: int) -> int:
        """
        Simulates the operation over the given years and returns the final amount of fund.
        """
        balance = principal
        accumulated_interest = 0

        for _ in range(years):
            balance, accumulated_interest = self.strategy.calculate_year_end(balance, accumulated_interest)
            balance -= self.annual_charge  # subtract operation charge, always possible as per problem statement

        # Final amount depends on interest type:
        if self.interest_type == self.SIMPLE_INTEREST:
            return balance + accumulated_interest
        else:
            return balance


class Dataset:
    """
    Represents a single dataset with initial conditions and available operations.
    """

    def __init__(self, principal: int, years: int, operations: List[Operation]):
        self.principal = principal
        self.years = years
        self.operations = operations

    def best_final_amount(self) -> int:
        """
        Returns the best possible final amount among operations.
        """
        return max(op.simulate(self.principal, self.years) for op in self.operations)


class OhgasFortuneSolver:
    """
    Orchestrates solutions for multiple datasets.
    """

    def __init__(self, datasets: List[Dataset]):
        self.datasets = datasets

    def solve(self) -> List[int]:
        results = []
        for dataset in self.datasets:
            results.append(dataset.best_final_amount())
        return results


class InputParser:
    """
    Handles parsing input from standard input into domain objects.
    """

    @staticmethod
    def parse_operation(line: str) -> Operation:
        parts = line.strip().split()
        interest_type = parts[0]
        rate = float(parts[1])
        charge = int(parts[2])
        return Operation(interest_type, rate, charge)

    @staticmethod
    def parse_dataset(input_lines: List[str], start_idx: int) -> Tuple[Dataset, int]:
        principal = int(input_lines[start_idx].strip())
        years = int(input_lines[start_idx + 1].strip())
        n_operations = int(input_lines[start_idx + 2].strip())
        operations = []
        cur_line = start_idx + 3
        for _ in range(n_operations):
            operations.append(InputParser.parse_operation(input_lines[cur_line]))
            cur_line += 1
        dataset = Dataset(principal, years, operations)
        return dataset, cur_line


def main():
    import sys

    input_lines = sys.stdin.readlines()
    m = int(input_lines[0].strip())
    datasets = []
    index = 1
    for _ in range(m):
        dataset, index = InputParser.parse_dataset(input_lines, index)
        datasets.append(dataset)

    solver = OhgasFortuneSolver(datasets)
    results = solver.solve()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()