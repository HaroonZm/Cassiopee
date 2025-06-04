class HammingNumbers:
    def __init__(self, limit: int = 10**6):
        self.limit = limit
        self.primes = (2, 3, 5)
        self._hamming_numbers = None

    def _generate_hamming_numbers(self):
        # Using a sophisticated abstracted method with priority queues and multiple iterators
        import heapq
        heap = [1]
        seen = set(heap)
        hamming_list = []

        while heap:
            current = heapq.heappop(heap)
            if current > self.limit:
                continue
            hamming_list.append(current)
            for p in self.primes:
                nxt = current * p
                if nxt <= self.limit and nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        hamming_list.sort()
        return hamming_list

    def hamming_numbers(self):
        if self._hamming_numbers is None:
            self._hamming_numbers = self._generate_hamming_numbers()
        return self._hamming_numbers

class HammingNumberCounter:
    def __init__(self, hamming_numbers_obj: HammingNumbers):
        self.hamming_numbers = hamming_numbers_obj.hamming_numbers()

    def count_in_range(self, m: int, n: int) -> int:
        # Abstraction with binary search for counting in range
        from bisect import bisect_left, bisect_right
        left = bisect_left(self.hamming_numbers, m)
        right = bisect_right(self.hamming_numbers, n)
        return right - left

class InputProcessor:
    def __init__(self, counter: HammingNumberCounter):
        self.counter = counter

    def process(self):
        import sys
        for line in sys.stdin:
            line = line.strip()
            if line == '0':
                break
            m, n = map(int, line.split())
            print(self.counter.count_in_range(m, n))

def main():
    hamming_obj = HammingNumbers(limit=10**6)
    counter = HammingNumberCounter(hamming_obj)
    processor = InputProcessor(counter)
    processor.process()

if __name__ == '__main__':
    main()