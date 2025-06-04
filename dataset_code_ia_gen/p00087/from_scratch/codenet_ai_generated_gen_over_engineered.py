from abc import ABC, abstractmethod
from typing import List, Union, Callable, Dict, Optional
import sys
import math

# --- Abstraction for Tokens ---

class Token(ABC):
    @abstractmethod
    def is_operator(self) -> bool:
        pass

class NumberToken(Token):
    def __init__(self, value: float):
        self.value = value

    def is_operator(self) -> bool:
        return False

    def __repr__(self):
        return f"NumberToken({self.value})"

class OperatorToken(Token):
    def __init__(self, symbol: str, func: Callable[[float, float], float]):
        self.symbol = symbol
        self.func = func

    def is_operator(self) -> bool:
        return True

    def __repr__(self):
        return f"OperatorToken('{self.symbol}')"

# --- Tokenizer ---

class Tokenizer:
    def __init__(self, operator_map: Dict[str, Callable[[float, float], float]]):
        self.operator_map = operator_map

    def tokenize(self, expression: str) -> List[Token]:
        tokens: List[Token] = []
        parts = expression.strip().split()
        for part in parts:
            if part in self.operator_map:
                tokens.append(OperatorToken(part, self.operator_map[part]))
            else:
                # Allow int or float parsing
                try:
                    val = float(part)
                except ValueError:
                    raise ValueError(f"Invalid token: {part}")
                tokens.append(NumberToken(val))
        return tokens

# --- Stack With Explicit Interface ---

class Stack:
    def __init__(self):
        self._container: List[float] = []

    def push(self, value: float) -> None:
        self._container.append(value)

    def pop(self) -> float:
        if not self._container:
            raise IndexError("Pop from empty stack")
        return self._container.pop()

    def size(self) -> int:
        return len(self._container)

    def __repr__(self):
        return f"Stack({self._container})"

# --- RPN Evaluator Abstraction ---

class Evaluator(ABC):
    @abstractmethod
    def evaluate(self, tokens: List[Token]) -> float:
        pass

class RPNEvaluator(Evaluator):
    def __init__(self, stack_factory: Callable[[], Stack]):
        self.stack_factory = stack_factory

    def evaluate(self, tokens: List[Token]) -> float:
        stack = self.stack_factory()
        for token in tokens:
            if token.is_operator():
                if stack.size() < 2:
                    raise ValueError("Not enough operands in stack for operator")

                rhs = stack.pop()
                lhs = stack.pop()
                result = token.func(lhs, rhs)
                stack.push(result)
            else:
                stack.push(token.value)
        if stack.size() != 1:
            raise ValueError("Invalid RPN expression: stack should have exactly one element after evaluation")
        return stack.pop()

# --- Factory for operators ---

def get_operator_map() -> Dict[str, Callable[[float, float], float]]:
    return {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

# --- Main Controller to handle multiple datasets ---

class RPNCalculatorController:
    def __init__(self,
                 evaluator: Evaluator,
                 tokenizer: Tokenizer,
                 output_precision: int = 6):
        self.evaluator = evaluator
        self.tokenizer = tokenizer
        self.output_precision = output_precision

    def run(self, input_lines: List[str]) -> List[str]:
        results: List[str] = []
        for line in input_lines:
            if not line.strip():
                continue
            tokens = self.tokenizer.tokenize(line)
            value = self.evaluator.evaluate(tokens)
            # Format result with required precision and absolute tolerance on error
            formatted = f"{value:.{self.output_precision}f}"
            results.append(formatted)
        return results

# --- Main execution logic ---

def main():
    operator_map = get_operator_map()
    tokenizer = Tokenizer(operator_map=operator_map)
    evaluator = RPNEvaluator(stack_factory=Stack)
    controller = RPNCalculatorController(evaluator, tokenizer)

    input_lines = [line.rstrip('\n') for line in sys.stdin if line.strip()]
    results = controller.run(input_lines)

    print("\n".join(results))

if __name__ == "__main__":
    main()