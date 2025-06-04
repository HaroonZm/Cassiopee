class FingerCountingProblem:
    def __init__(self, n: int):
        self._n = n
        self._finger_counter = FingerCounter()

    def solve(self) -> int:
        # Determine minimum fingers needed to represent n in binary (number of bits)
        return self._finger_counter.count_min_fingers(self._n)


class FingerCounter:
    def count_min_fingers(self, number: int) -> int:
        if number == 0:
            return 0
        return BitLengthCalculator().calculate_bit_length(number)


class BitLengthCalculator:
    def calculate_bit_length(self, value: int) -> int:
        # An abstraction over built-in bit_length method, anticipating alternative implementations
        return self._bit_length_iterative(value)

    def _bit_length_iterative(self, val: int) -> int:
        length = 0
        current = val
        while current > 0:
            current >>= 1
            length += 1
        return length


class InputOutputHandler:
    def __init__(self, input_provider=input, output_provider=print):
        self._input = input_provider
        self._output = output_provider

    def read_int(self) -> int:
        try:
            return int(self._input().strip())
        except Exception as e:
            raise ValueError("Invalid input, expected an integer.") from e

    def write_int(self, value: int) -> None:
        self._output(str(value))


def main():
    io_handler = InputOutputHandler()
    n = io_handler.read_int()
    problem = FingerCountingProblem(n)
    result = problem.solve()
    io_handler.write_int(result)


if __name__ == "__main__":
    main()