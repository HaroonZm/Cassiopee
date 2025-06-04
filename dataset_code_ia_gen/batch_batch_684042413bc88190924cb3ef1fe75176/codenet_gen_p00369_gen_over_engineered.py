from typing import List, Tuple, Protocol, runtime_checkable

@runtime_checkable
class Segmenter(Protocol):
    def segment(self, number_str: str) -> List[int]:
        ...

class AbstractSegmenter:
    def __init__(self, number_str: str):
        self.number_str = number_str
        self.length = len(number_str)

    def segment(self) -> List[int]:
        raise NotImplementedError()

class RecursiveSegmenter(AbstractSegmenter):
    def __init__(self, number_str: str):
        super().__init__(number_str)
        self.memo = {}

    def segment(self) -> int:
        # Find the minimal difference over all valid partitions of the string into at least two parts.
        # Returns minimal difference (int)
        return self._min_difference(0, [])

    def _min_difference(self, index: int, segments: List[int]) -> int:
        if index == self.length:
            if len(segments) > 1:
                return max(segments) - min(segments)
            else:
                return float('inf')

        key = (index, tuple(segments))
        if key in self.memo:
            return self.memo[key]

        min_diff = float('inf')
        # To avoid super long segments that are large numbers, impose a max segment length?
        # But problem states up to length 100000, so max segment length can be entire string.
        # However, long segments convert to int might be huge, Python can still handle it.

        # Try every possible cut from index+1 to end
        for end in range(index + 1, self.length + 1):
            segment_str = self.number_str[index:end]
            # All digits between 1-9 so no check for zero digit needed
            segment_val = int(segment_str)
            min_diff = min(min_diff, self._min_difference(end, segments + [segment_val]))
            # To prevent useless computations, if min_diff is zero already, return immediately
            if min_diff == 0:
                break

        self.memo[key] = min_diff
        return min_diff

class IterativeSegmenter(AbstractSegmenter):
    # Dynamic programming based approach to handle large inputs efficiently.
    # DP: dp[i] = minimal difference for substring number_str[0:i], storing min and max segments in tuple
    
    def segment(self) -> int:
        # We need to find min diff over partitions into at least two parts.
        # Since numbers can be large (length up to 100000), we cannot store all segment values.
        # Instead, we'll keep track for each position i:
        # dp[i] = set of tuples (min_segment_val, max_segment_val) reachable from 0 to i
        # We update dp[i] from dp[j] and segment number_str[j:i]
        # To limit memory and runtime, we can prune states by keeping only minimal differences.

        from collections import defaultdict
        dp = [dict() for _ in range(self.length + 1)] 
        # dp[0] = {None: None} no segments chosen yet
        dp[0][(float('inf'), float('-inf'))] = True  # min_val, max_val

        for i in range(1, self.length + 1):
            for j in range(max(0, i-10), i): 
                # Limit max segment length to 10 digits for performance (since digits 1-9 only, fits int easily)
                segment_str = self.number_str[j:i]
                segment_val = int(segment_str)
                for (min_v, max_v) in dp[j]:
                    # create new state
                    new_min = min(min_v, segment_val)
                    new_max = max(max_v, segment_val)
                    # update dp[i]
                    if (new_min, new_max) not in dp[i]:
                        dp[i][(new_min, new_max)] = True

        # find minimal difference with at least two parts
        # That means dp[length] with min_val != inf and max_val != -inf and segments count > 1
        # Our dp does not track segment counts, so we backtrack segment counts via a bit more complex approach,
        # or instead, note that dp[0] state start is (inf, -inf), that we count segments as transitions
        # So instead, we filter for (min_v, max_v) where min_v != inf and max_v != -inf and that resulted from at least one segment

        # To check segments count, a trick: initial dp[0] min=max=inf/-inf, next steps update these.
        # So any min=max=some val means one segment, else >1 segments.

        # Actually min=max after the first segment:
        # So difference == 0 means one segment => only one segment invalid
        # So minimum difference > 0 means at least two segments

        min_diff = float('inf')
        for (min_v, max_v) in dp[self.length]:
            diff = max_v - min_v
            if diff > 0 and diff < min_diff:
                min_diff = diff

        return min_diff if min_diff != float('inf') else 0

class FortuneYearsPredictor:
    def __init__(self, number_str: str, strategy: Segmenter = None):
        self.number_str = number_str
        if strategy is None:
            # Choose strategy based on length of the string
            if len(number_str) <= 20:
                self.segmenter = RecursiveSegmenter(number_str)
            else:
                self.segmenter = IterativeSegmenter(number_str)
        else:
            self.segmenter = strategy

    def predict_min_years(self) -> int:
        return self.segmenter.segment()

class IOHandler:
    def __init__(self):
        pass

    def read_input(self) -> str:
        # read single line input string
        return input().strip()

    def output(self, result: int) -> None:
        print(result)

def main():
    io = IOHandler()
    number_str = io.read_input()
    predictor = FortuneYearsPredictor(number_str)
    result = predictor.predict_min_years()
    io.output(result)

if __name__ == "__main__":
    main()