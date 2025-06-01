class CollatzOperation:
    def apply(self, n: int) -> int:
        raise NotImplementedError("This method should be overridden by subclasses")

class EvenOperation(CollatzOperation):
    def apply(self, n: int) -> int:
        return n // 2

class OddOperation(CollatzOperation):
    def apply(self, n: int) -> int:
        return 3 * n + 1

class OperationSelector:
    def __init__(self):
        self._even_op = EvenOperation()
        self._odd_op = OddOperation()
        
    def select(self, n: int) -> CollatzOperation:
        if n % 2 == 0:
            return self._even_op
        else:
            return self._odd_op

class CollatzSequence:
    def __init__(self, start_value: int):
        self._start_value = start_value
        self._steps = 0
        self._operation_selector = OperationSelector()
        self._current_value = start_value

    def _step(self):
        operation = self._operation_selector.select(self._current_value)
        self._current_value = operation.apply(self._current_value)
        self._steps += 1

    def run_until_one(self) -> int:
        while self._current_value != 1:
            self._step()
        return self._steps

class InputHandler:
    def __init__(self):
        self._inputs = []

    def read_inputs(self):
        while True:
            try:
                line = input()
                if line == "0":
                    break
                n = int(line)
                if n < 1 or n > 1_000_000:
                    raise ValueError("Input out of allowed range")
                self._inputs.append(n)
            except EOFError:
                break

    def get_inputs(self):
        return self._inputs

class OutputHandler:
    def __init__(self):
        pass

    def print_steps(self, steps: int):
        print(steps)

class CollatzSolver:
    def __init__(self):
        self._input_handler = InputHandler()
        self._output_handler = OutputHandler()

    def execute(self):
        self._input_handler.read_inputs()
        for n in self._input_handler.get_inputs():
            sequence = CollatzSequence(n)
            steps = sequence.run_until_one()
            self._output_handler.print_steps(steps)

if __name__ == "__main__":
    solver = CollatzSolver()
    solver.execute()