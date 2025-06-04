from typing import List, Optional, Tuple, Set, Iterator
from abc import ABC, abstractmethod

class ChopsticksRecord(ABC):
    @abstractmethod
    def possible_counts(self, previous_counts: Set[int]) -> Set[int]:
        pass

class InitialCountRecord(ChopsticksRecord):
    def __init__(self, initial_count: int):
        self.initial_count = initial_count

    def possible_counts(self, previous_counts: Set[int] = None) -> Set[int]:
        # At day 0, count is fixed and known
        return {self.initial_count}

class ModuloConstraintsRecord(ChopsticksRecord):
    def __init__(self, moduli: List[int], remainders: List[Optional[int]]):
        self.moduli = moduli
        self.remainders = remainders

    def possible_counts(self, previous_counts: Set[int]) -> Set[int]:
        if not previous_counts:
            return set()
        # The day count is less or equal to previous day's counts
        max_prev = max(previous_counts)
        candidates = set()
        # We limit search space from 0 to max_prev because count never increases
        for candidate in range(max_prev + 1):
            if all(
                (r == -1 or candidate % m == r)
                for m, r in zip(self.moduli, self.remainders)
            ):
                candidates.add(candidate)
        # Intersect with previous_counts range: candidate must be <= max previous count
        return candidates

class ChopsticksState:
    def __init__(self, day: int, record: ChopsticksRecord):
        self.day = day
        self.record = record
        self.possible_counts: Set[int] = set()

    def update_possible_counts(self, previous_state: Optional['ChopsticksState']):
        if previous_state is None:
            # Day 0
            self.possible_counts = self.record.possible_counts()
        else:
            self.possible_counts = self.record.possible_counts(previous_state.possible_counts)

class ChopsticksSystem:
    def __init__(self, N: int, M: int, D: int, moduli: List[int], records_remainders: List[List[int]]):
        self.N = N
        self.M = M
        self.D = D
        self.moduli = moduli
        self.records_remainders = records_remainders
        self.states: List[ChopsticksState] = []

    def run_analysis(self) -> int:
        # Initialize day 0 state
        initial_record = InitialCountRecord(self.N)
        day0_state = ChopsticksState(0, initial_record)
        day0_state.update_possible_counts(None)
        self.states.append(day0_state)

        # For days 1..D, create states with modulo constraints and update possible counts
        for day in range(1, self.D + 1):
            record = ModuloConstraintsRecord(self.moduli, self.records_remainders[day-1])
            state = ChopsticksState(day, record)
            state.update_possible_counts(self.states[day-1])
            if not state.possible_counts:
                # No possible counts means contradiction - output -1 immediately
                return -1
            self.states.append(state)

        # Return maximal possible count on day D
        return max(self.states[-1].possible_counts)

def parse_input() -> Tuple[int,int,int,List[int],List[List[int]]]:
    N, M, D = map(int, input().split())
    moduli = list(map(int, input().split()))
    records = [list(map(int, input().split())) for _ in range(D)]
    return N, M, D, moduli, records

def main():
    N, M, D, moduli, records = parse_input()
    system = ChopsticksSystem(N, M, D, moduli, records)
    result = system.run_analysis()
    print(result)

if __name__ == "__main__":
    main()