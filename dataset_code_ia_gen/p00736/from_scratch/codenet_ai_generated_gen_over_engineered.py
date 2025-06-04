from abc import ABC, abstractmethod
from typing import Tuple, Dict


# Define the three-valued logic domain and helper functions

class TruthValue:
    FALSE = 0
    UNKNOWN = 1
    TRUE = 2
    DOMAIN = (FALSE, UNKNOWN, TRUE)


# Abstract syntax tree for formula

class Formula(ABC):
    @abstractmethod
    def evaluate(self, assignment: Dict[str, int]) -> int:
        pass

    def count_true(self) -> int:
        counter = 0
        # Iterate over all assignments of P,Q,R in domain {0,1,2}
        for p in TruthValue.DOMAIN:
            for q in TruthValue.DOMAIN:
                for r in TruthValue.DOMAIN:
                    assignment = {'P': p, 'Q': q, 'R': r}
                    val = self.evaluate(assignment)
                    if val == TruthValue.TRUE:
                        counter += 1
        return counter


# Constants

class Const(Formula):
    def __init__(self, value: int):
        self.value = value

    def evaluate(self, assignment: Dict[str, int]) -> int:
        return self.value


# Variables

class Var(Formula):
    def __init__(self, name: str):
        self.name = name

    def evaluate(self, assignment: Dict[str, int]) -> int:
        return assignment[self.name]


# Unary operator: Negation

class Negation(Formula):
    # Negation table mapping input => output
    NEG_TABLE = {
        TruthValue.FALSE: TruthValue.TRUE,
        TruthValue.UNKNOWN: TruthValue.UNKNOWN,
        TruthValue.TRUE: TruthValue.FALSE
    }

    def __init__(self, operand: Formula):
        self.operand = operand

    def evaluate(self, assignment: Dict[str, int]) -> int:
        v = self.operand.evaluate(assignment)
        return self.NEG_TABLE[v]


# Binary operators: Conjunction and Disjunction

class BinaryOperator(Formula, ABC):
    def __init__(self, left: Formula, right: Formula):
        self.left = left
        self.right = right

    @abstractmethod
    def op(self, a: int, b: int) -> int:
        pass

    def evaluate(self, assignment: Dict[str, int]) -> int:
        a = self.left.evaluate(assignment)
        b = self.right.evaluate(assignment)
        return self.op(a, b)


class Conjunction(BinaryOperator):
    # AND truth table from Table C-1
    # Rows and columns are from {0,1,2} rows by columns
    # Precompute the table for quick lookup:
    #   0 * anything => 0
    #   1 * 2 = 1
    #   2 * 2 = 2 etc
    AND_TABLE = [
        [0,0,0],
        [0,1,1],
        [0,1,2]
    ]

    def op(self, a: int, b: int) -> int:
        return self.AND_TABLE[a][b]


class Disjunction(BinaryOperator):
    # OR truth table from Table C-1
    OR_TABLE = [
        [0,1,2],
        [1,1,2],
        [2,2,2]
    ]

    def op(self, a: int, b: int) -> int:
        return self.OR_TABLE[a][b]


# Parser for the formula according to BNF grammar

class Parser:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0

    def peek(self) -> str:
        return self.text[self.pos] if self.pos < len(self.text) else ''

    def consume(self, expected: str = None) -> str:
        if self.pos >= len(self.text):
            return ''
        current = self.text[self.pos]
        if expected and current != expected:
            raise ValueError(f"Expected '{expected}' at pos {self.pos} but found '{current}'")
        self.pos += 1
        return current

    def parse_formula(self) -> Formula:
        c = self.peek()
        # Constants
        if c in '012':
            self.consume()
            return Const(int(c))
        # Variables
        if c in 'PQR':
            self.consume()
            return Var(c)
        # Negation
        if c == '-':
            self.consume()
            operand = self.parse_formula()
            return Negation(operand)
        # Binary operations: must start with '('
        if c == '(':
            self.consume()  # skip '('
            left = self.parse_formula()
            op = self.consume()
            # op should be '*' or '+'
            if op not in ['*', '+']:
                raise ValueError(f"Expected '*' or '+' but got '{op}' at pos {self.pos}")
            right = self.parse_formula()
            closing = self.consume()
            if closing != ')':
                raise ValueError(f"Expected ')' but got '{closing}' at pos {self.pos}")
            if op == '*':
                return Conjunction(left, right)
            else:  # op == '+'
                return Disjunction(left, right)
        raise ValueError(f"Unexpected character '{c}' at pos {self.pos}")


def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if line == '.':
            break
        if not line:
            continue
        # Parse
        parser = Parser(line)
        formula = parser.parse_formula()
        # Count triples making the formula true (value 2)
        print(formula.count_true())


if __name__ == '__main__':
    main()