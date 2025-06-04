class Sentinel:
    def __init__(self):
        self.value = float('inf')

    def __le__(self, other):
        return True

    def __repr__(self):
        return "SENTINEL"

class ComparisonsCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count

class MergeSortStrategy:
    def __init__(self, sentinel, counter):
        self.sentinel = sentinel
        self.counter = counter

    def merge(self, array, left, mid, right):
        n1 = mid - left
        n2 = right - mid

        L = [None] * (n1 + 1)
        R = [None] * (n2 + 1)

        for i in range(n1):
            L[i] = array[left + i]
        for i in range(n2):
            R[i] = array[mid + i]

        L[n1] = self.sentinel
        R[n2] = self.sentinel

        i = 0
        j = 0
        for k in range(left, right):
            self.counter.increment()
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1

    def merge_sort(self, array, left, right):
        if left + 1 < right:
            mid = (left + right) // 2
            self.merge_sort(array, left, mid)
            self.merge_sort(array, mid, right)
            self.merge(array, left, mid, right)

class SortContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, array):
        self.strategy.merge_sort(array, 0, len(array))

def main():
    import sys

    class InputParser:
        def __init__(self, stream):
            self.stream = stream

        def parse(self):
            n = int(self.stream.readline())
            arr = list(map(int, self.stream.readline().split()))
            return n, arr

    input_parser = InputParser(sys.stdin)
    n, array = input_parser.parse()

    sentinel = Sentinel()
    counter = ComparisonsCounter()
    strategy = MergeSortStrategy(sentinel, counter)
    sorter = SortContext(strategy)

    sorter.sort(array)

    print(' '.join(map(str, array)))
    print(counter.value())

if __name__ == "__main__":
    main()