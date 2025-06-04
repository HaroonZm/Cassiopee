from typing import List, Set, Dict, Tuple

class Cell:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value  # -1 if unknown, else digit 1..9
        self.possible_values: Set[int] = set() if value == -1 else {value}

    def is_assigned(self) -> bool:
        return self.value != -1

    def assign(self, val: int):
        self.value = val
        self.possible_values = {val}

    def unassign(self):
        self.value = -1
        self.possible_values = set()

class ArithmeticPuzzle:
    def __init__(self, values: List[int]):
        # Map from cell name to Cell instance
        self.cells: Dict[str, Cell] = {}
        # Cells in order A to I
        names = ['A','B','C','D','E','F','G','H','I']
        for i, name in enumerate(names):
            self.cells[name] = Cell(name, values[i])
        # Set of used digits (from assigned cells)
        self.used_digits: Set[int] = set()
        for cell in self.cells.values():
            if cell.is_assigned():
                self.used_digits.add(cell.value)
        # Will set possible values for unassigned cells
        self.update_possibilities()
        self.solutions_count = 0

    def update_possibilities(self):
        available_digits = set(range(1,10)) - self.used_digits
        for cell in self.cells.values():
            if not cell.is_assigned():
                cell.possible_values = available_digits.copy()

    def check_unique_digits(self) -> bool:
        # Check that assigned digits are unique and in 1..9
        digits = [c.value for c in self.cells.values() if c.is_assigned()]
        return len(set(digits)) == len(digits) and all(1 <= d <= 9 for d in digits)

    def arithmetic_constraints_valid(self) -> bool:
        c = self.cells
        # Columns:
        # units digit: I == (C + F) mod 10
        # tens digit: H == (B + E + carry1) mod 10
        # hundreds digit: G == (A + D + carry2)
        # carry1 = ((C + F) // 10)
        # carry2 = ((B + E + carry1) // 10)
        # Since all inputs and digits are 1..9 or -1, we check consistency only if values assigned
        def val(x):
            return c[x].value if c[x].is_assigned() else None
        C, F, I = val('C'), val('F'), val('I')
        B, E, H = val('B'), val('E'), val('H')
        A, D, G = val('A'), val('D'), val('G')

        # If any digit in sum is missing, can't fully verify, but do partial checks
        # We'll check all possible partial consistencies to prune search space

        # Units place
        if all(v is not None for v in (C,F,I)):
            s = C + F
            if s % 10 != I:
                return False
            carry1 = s // 10
        elif None not in (C,F) and I is not None:
            # I is assigned but sum incomplete? Try all possible carry1
            s = C + F
            if s % 10 != I:
                return False
            carry1 = s // 10
        else:
            carry1 = None

        # Tens place
        if all(v is not None for v in (B,E,H)) and carry1 is not None:
            s = B + E + carry1
            if s % 10 != H:
                return False
            carry2 = s // 10
        elif None not in (B,E,H) and carry1 is not None:
            s = B + E + carry1
            if s % 10 != H:
                return False
            carry2 = s // 10
        else:
            carry2 = None

        # Hundreds place
        if all(v is not None for v in (A,D,G)) and carry2 is not None:
            if A + D + carry2 != G:
                return False
        elif None not in (A,D,G) and carry2 is not None:
            if A + D + carry2 != G:
                return False

        return True

    def is_valid_assignment(self) -> bool:
        if not self.check_unique_digits():
            return False
        if not self.arithmetic_constraints_valid():
            return False
        return True

    def get_unassigned_cell_with_fewest_possibilities(self) -> Cell:
        # Heuristic: choose unassigned cell with least candidates -> reduce branching
        candidates = [c for c in self.cells.values() if not c.is_assigned()]
        candidates.sort(key=lambda c: len(c.possible_values))
        return candidates[0] if candidates else None

    def assign_and_update(self, cell: Cell, value: int) -> bool:
        cell.assign(value)
        self.used_digits.add(value)
        # Update possible digits for others:
        self.update_possibilities()
        return True

    def unassign_cell(self, cell: Cell):
        self.used_digits.discard(cell.value)
        cell.unassign()
        self.update_possibilities()

    def solve(self) -> int:
        # Backtracking search counting number of valid solutions
        if not self.is_valid_assignment():
            return 0
        unassigned_cell = self.get_unassigned_cell_with_fewest_possibilities()
        if unassigned_cell is None:
            # All assigned and valid -> one solution
            return 1
        count = 0
        for val in sorted(unassigned_cell.possible_values):
            # Try assigning val
            self.assign_and_update(unassigned_cell, val)
            if self.arithmetic_constraints_valid():
                count += self.solve()
            self.unassign_cell(unassigned_cell)
        return count

def main():
    import sys
    values = list(map(int, sys.stdin.read().strip().split()))
    puzzle = ArithmeticPuzzle(values)
    print(puzzle.solve())

if __name__ == '__main__':
    main()