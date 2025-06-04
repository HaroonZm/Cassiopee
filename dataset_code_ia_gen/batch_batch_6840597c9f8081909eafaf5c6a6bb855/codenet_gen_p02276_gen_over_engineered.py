class ArrayPartitionerInterface:
    def partition(self):
        raise NotImplementedError

class PivotSelectorInterface:
    def select_pivot_index(self, array, start, end):
        raise NotImplementedError

class ExchangeStrategyInterface:
    def exchange(self, array, i, j):
        raise NotImplementedError

class ArrayPrinterInterface:
    def print_array(self, array, pivot_index):
        raise NotImplementedError

class LastElementPivotSelector(PivotSelectorInterface):
    def select_pivot_index(self, array, start, end):
        return end

class DefaultExchangeStrategy(ExchangeStrategyInterface):
    def exchange(self, array, i, j):
        array[i], array[j] = array[j], array[i]

class BracketArrayPrinter(ArrayPrinterInterface):
    def print_array(self, array, pivot_index):
        output = []
        for idx, val in enumerate(array):
            if idx == pivot_index:
                output.append(f'[{val}]')
            else:
                output.append(str(val))
        print(' '.join(output))

class Partitioner(ArrayPartitionerInterface):
    def __init__(self, pivot_selector=None, exchange_strategy=None):
        self.pivot_selector = pivot_selector or LastElementPivotSelector()
        self.exchange_strategy = exchange_strategy or DefaultExchangeStrategy()

    def partition(self, array, p, r):
        x_index = self.pivot_selector.select_pivot_index(array, p, r)
        x = array[x_index]
        # per problem statement pivot is always last element, so if not, swap
        if x_index != r:
            self.exchange_strategy.exchange(array, x_index, r)
            x = array[r]

        i = p - 1
        for j in range(p, r):
            if array[j] <= x:
                i += 1
                self.exchange_strategy.exchange(array, i, j)
        self.exchange_strategy.exchange(array, i + 1, r)
        return i + 1

class QuickSortController:
    def __init__(self, partitioner, output_printer):
        self.partitioner = partitioner
        self.output_printer = output_printer
        self._pivot_index = None

    def quicksort(self, array, p, r):
        if p < r:
            q = self.partitioner.partition(array, p, r)
            self._pivot_index = q
            # After partitioning first, print as per problem to show pivot positioning of this call
            # But the problem wants final partition print after first partition only
            # So only print once after first partition in main flow
            self.quicksort(array, p, q - 1)
            self.quicksort(array, q + 1, r)

    def single_partition_and_print(self, array, p, r):
        q = self.partitioner.partition(array, p, r)
        self._pivot_index = q
        self.output_printer.print_array(array, q)

def main():
    import sys

    class InputReader:
        def read_int(self):
            return int(sys.stdin.readline())

        def read_int_list(self):
            return list(map(int, sys.stdin.readline().split()))

    reader = InputReader()
    n = reader.read_int()
    array = reader.read_int_list()

    partitioner = Partitioner()
    printer = BracketArrayPrinter()
    controller = QuickSortController(partitioner, printer)
    # According to problem statement output is after single partition call, not full quicksort
    controller.single_partition_and_print(array, 0, n - 1)

if __name__ == "__main__":
    main()