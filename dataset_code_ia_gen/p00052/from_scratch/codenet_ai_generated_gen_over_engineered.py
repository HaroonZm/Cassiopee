class FactorialTrailingZeroCounter:
    class InputHandler:
        def __init__(self):
            self._inputs = []
            self._terminated = False

        def read_inputs(self):
            count = 0
            while not self._terminated and count < 20:
                line = input().strip()
                if not line.isdigit():
                    continue
                n = int(line)
                if n == 0:
                    self._terminated = True
                    break
                self._inputs.append(n)
                count += 1
            return self._inputs

    class TrailingZeroCalculator:
        def __init__(self, base_factor=5):
            self.base_factor = base_factor

        def count_trailing_zeros(self, n: int) -> int:
            # Count the number of times base_factor divides n!
            count = 0
            divisor = self.base_factor
            while divisor <= n:
                count += n // divisor
                divisor *= self.base_factor
            return count

    class OutputHandler:
        @staticmethod
        def print_trailing_zeros(results):
            for res in results:
                print(res)

    def __init__(self):
        self.input_handler = self.InputHandler()
        self.calculator = self.TrailingZeroCalculator()
        self.output_handler = self.OutputHandler()

    def process(self):
        inputs = self.input_handler.read_inputs()
        results = []
        for n in inputs:
            zeros = self.calculator.count_trailing_zeros(n)
            results.append(zeros)
        self.output_handler.print_trailing_zeros(results)

if __name__ == "__main__":
    app = FactorialTrailingZeroCounter()
    app.process()