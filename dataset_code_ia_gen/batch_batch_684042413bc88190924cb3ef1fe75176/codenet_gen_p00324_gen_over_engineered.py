class TradeBalanceAnalyzer:
    """
    Abstract base class for analyzing trade balance data streams.
    Designed for extensibility to support multiple analysis strategies.
    """

    def __init__(self, data_stream):
        """
        Initialize with data stream representing net inflow per nanosecond
        Args:
            data_stream (List[int]): List of integers indicating net data flow per nanosecond.
        """
        self.data_stream = data_stream

    def analyze(self):
        """
        Analyze the data stream to find the longest interval with zero sum.
        This method must be overridden by subclasses.
        Returns:
            int: Length of the longest subinterval with sum zero.
        """
        raise NotImplementedError("Subclasses should implement this!")


class PrefixSumBalanceAnalyzer(TradeBalanceAnalyzer):
    """
    Implements zero-sum longest subarray detection using prefix sums and hashing.
    """

    def analyze(self):
        # Dictionary to store earliest index of each prefix sum encountered
        prefix_index_map = dict()
        prefix_index_map[0] = -1  # prefix sum zero before array start

        max_len = 0
        prefix_sum = 0

        for i, val in enumerate(self.data_stream):
            prefix_sum += val
            if prefix_sum in prefix_index_map:
                # Calculate subarray length between previous occurrence and current
                subarray_len = i - prefix_index_map[prefix_sum]
                if subarray_len > max_len:
                    max_len = subarray_len
            else:
                prefix_index_map[prefix_sum] = i

        return max_len


class TradeDataInputParser:
    """
    Parses input according to the problem specification from standard input.
    Encapsulates input parsing for easier future input source extensions.
    """

    @staticmethod
    def parse():
        import sys
        input = sys.stdin.readline
        N_raw = input()
        while N_raw.strip() == '':
            N_raw = input()
        N = int(N_raw.strip())

        data = []
        read_count = 0
        while read_count < N:
            line = input()
            if line.strip() == '':
                continue
            data.append(int(line.strip()))
            read_count += 1

        return data


class LongestZeroSumIntervalSolution:
    """
    Orchestrates the full solution pipeline:
        input parsing -> analysis -> output
    """

    def __init__(self):
        self.data_stream = []

    def run(self):
        self._parse_input()
        analyzer = PrefixSumBalanceAnalyzer(self.data_stream)
        result = analyzer.analyze()
        self._output_result(result)

    def _parse_input(self):
        parser = TradeDataInputParser()
        self.data_stream = parser.parse()

    def _output_result(self, longest_length: int):
        print(longest_length)


if __name__ == "__main__":
    solution = LongestZeroSumIntervalSolution()
    solution.run()