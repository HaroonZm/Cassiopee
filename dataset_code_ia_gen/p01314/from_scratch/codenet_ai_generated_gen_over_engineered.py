class SumOfConsecutiveIntegers:
    class InputHandler:
        def __init__(self):
            self._data = []

        def read_input(self):
            while True:
                line = input().strip()
                if not line.isdigit():
                    # Ignore invalid lines, although problem guarantees input format
                    continue
                value = int(line)
                if value == 0:
                    break
                self._data.append(value)

        def get_data(self):
            return self._data

    class ConsecutiveSumCounter:
        def __init__(self, n):
            self.n = n

        def count_ways(self):
            # Using a sliding window approach abstracted as iterator over ranges
            # Instead of direct math formula, do stepwise enumeration for extensibility
            sequences = SumOfConsecutiveIntegers.SequenceGenerator(self.n)
            return sequences.count_sequences()

    class SequenceGenerator:
        def __init__(self, target_sum):
            self.target = target_sum

        def count_sequences(self):
            # We consider sequences of at least length 2
            count = 0
            # Use two pointers to find all sequences
            left = 1
            right = 2
            current_sum = left + right
            while left < right and right <= self.target:
                if current_sum == self.target:
                    count += 1
                    # Move right pointer forward
                    right += 1
                    current_sum += right
                elif current_sum < self.target:
                    right += 1
                    current_sum += right
                else:
                    current_sum -= left
                    left += 1
            return count

    class OutputHandler:
        def __init__(self):
            self._results = []

        def collect_result(self, result):
            self._results.append(result)

        def output_results(self):
            for res in self._results:
                print(res)

def main():
    input_handler = SumOfConsecutiveIntegers.InputHandler()
    input_handler.read_input()
    output_handler = SumOfConsecutiveIntegers.OutputHandler()

    for n in input_handler.get_data():
        counter = SumOfConsecutiveIntegers.ConsecutiveSumCounter(n)
        ways = counter.count_ways()
        output_handler.collect_result(ways)

    output_handler.output_results()

if __name__ == "__main__":
    main()