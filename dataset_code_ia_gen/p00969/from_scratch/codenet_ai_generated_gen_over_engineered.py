class ArithmeticProgressionFinder:
    class SequenceElement:
        def __init__(self, value: int, index: int):
            self.value = value
            self.index = index

        def __repr__(self):
            return f"Elem(val={self.value}, idx={self.index})"

    class APDynamicTable:
        def __init__(self, size: int):
            # For each index, map difference -> length of AP ending here with that diff
            self.dp = [{} for _ in range(size)]

        def get(self, idx: int, diff: int) -> int:
            return self.dp[idx].get(diff, 1)

        def set(self, idx: int, diff: int, length: int):
            self.dp[idx][diff] = length

        def max_length(self) -> int:
            max_len = 1
            for d in self.dp:
                if d:
                    max_len = max(max_len, max(d.values()))
            return max_len

    class InputParser:
        @staticmethod
        def parse() -> 'ArithmeticProgressionFinder.InputData':
            n = int(input())
            vals = list(map(int, input().split()))
            return ArithmeticProgressionFinder.InputData(n, vals)

    class InputData:
        def __init__(self, n: int, values: list[int]):
            self.n = n
            self.values = values

    def __init__(self, input_data: 'ArithmeticProgressionFinder.InputData'):
        self.n = input_data.n
        self.values = input_data.values
        self.elements = [self.SequenceElement(v, i) for i, v in enumerate(self.values)]

    def find_longest_ap(self) -> int:
        # Sort elements by value to manage ascending AP easily
        sorted_elements = sorted(self.elements, key=lambda e: e.value)
        val_to_idx = {e.value: i for i, e in enumerate(sorted_elements)}
        dp = self.APDynamicTable(self.n)
        max_len = 1

        # For each pair (j, i) with j < i, try to build AP ending at i with difference d
        for i in range(self.n):
            current = sorted_elements[i]
            for j in range(i):
                prev = sorted_elements[j]
                diff = current.value - prev.value
                # length of AP ending at j with difference diff, default 1 means just prev element
                length = dp.get(j, diff) + 1
                dp.set(i, diff, length)
                if length > max_len:
                    max_len = length

        return max_len

if __name__ == "__main__":
    input_data = ArithmeticProgressionFinder.InputParser.parse()
    finder = ArithmeticProgressionFinder(input_data)
    print(finder.find_longest_ap())