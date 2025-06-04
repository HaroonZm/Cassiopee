class Token:
    def __init__(self, value):
        self.value = value

class NumberToken(Token):
    def __init__(self, value: int):
        super().__init__(value)

class OperatorToken(Token):
    def __init__(self, symbol: str):
        if symbol not in ['+', '-', '*', '/', '=']:
            raise ValueError(f"Invalid operator: {symbol}")
        super().__init__(symbol)

class TokenStream:
    def __init__(self):
        self._tokens = []
        self._index = 0

    def append(self, token: Token):
        self._tokens.append(token)

    def next(self) -> Token:
        if self._index >= len(self._tokens):
            raise IndexError("Read past end of tokens")
        token = self._tokens[self._index]
        self._index += 1
        return token

    def has_next(self) -> bool:
        return self._index < len(self._tokens)

class CalculatorState:
    def __init__(self):
        self.current_value = None
        self.pending_operator = None

    def reset(self):
        self.current_value = None
        self.pending_operator = None

class CalculatorEngine:
    def __init__(self):
        self.state = CalculatorState()

    def apply_operation(self, left: int, operator: str, right: int) -> int:
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            # Integer division with truncation toward zero
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            # Python's int division truncates towards negative, need truncation toward zero
            sign = (left < 0) ^ (right < 0)
            quotient = abs(left) // abs(right)
            return -quotient if sign else quotient
        else:
            raise ValueError(f"Unknown operator: {operator}")

    def process_tokens(self, token_stream: TokenStream) -> int:
        # Initialize the current value with the first number
        if not token_stream.has_next():
            raise ValueError("Empty input stream")
        first_token = token_stream.next()
        if not isinstance(first_token, NumberToken):
            raise ValueError("First token must be a number")
        self.state.current_value = first_token.value
        
        while token_stream.has_next():
            op_token = token_stream.next()
            if not isinstance(op_token, OperatorToken):
                raise ValueError("Expected operator token")

            if op_token.value == '=':
                # End of expression
                return self.state.current_value

            num_token = token_stream.next()
            if not isinstance(num_token, NumberToken):
                raise ValueError("Expected number token after operator")

            # Apply operation immediately (no precedence)
            self.state.current_value = self.apply_operation(self.state.current_value, op_token.value, num_token.value)

        raise ValueError("Input does not end with '=' operator")

class InputParser:
    def __init__(self, lines):
        self.lines = lines

    def parse(self) -> TokenStream:
        tokens = TokenStream()
        # We expect alternating lines number/operator starting with number.
        expected_number = True
        for line in self.lines:
            stripped = line.strip()
            if expected_number:
                try:
                    val = int(stripped)
                except ValueError:
                    raise ValueError(f"Expected number but got: {stripped}")
                tokens.append(NumberToken(val))
                expected_number = False
            else:
                if stripped not in ['+', '-', '*', '/', '=']:
                    raise ValueError(f"Expected operator but got: {stripped}")
                tokens.append(OperatorToken(stripped))
                expected_number = True
        if expected_number:
            raise ValueError("Expression ended unexpectedly with operator (no trailing number)")
        return tokens

class IOController:
    def __init__(self, input_lines):
        self.input_lines = input_lines

    def execute(self):
        parser = InputParser(self.input_lines)
        tokens = parser.parse()
        engine = CalculatorEngine()
        result = engine.process_tokens(tokens)
        # Output with newline as requested
        print(result)

if __name__ == '__main__':
    import sys
    lines = [line for line in sys.stdin if line.strip() != '']
    io_controller = IOController(lines)
    io_controller.execute()