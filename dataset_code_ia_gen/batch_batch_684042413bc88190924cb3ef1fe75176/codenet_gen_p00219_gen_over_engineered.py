from abc import ABC, abstractmethod
from typing import List, Iterator, Optional

class InputSource(ABC):
    @abstractmethod
    def next_line(self) -> Optional[str]:
        pass

class StdInputSource(InputSource):
    def __init__(self):
        import sys
        self._iterator = iter(sys.stdin.readline, '')
    def next_line(self) -> Optional[str]:
        try:
            return next(self._iterator).rstrip('\n')
        except StopIteration:
            return None

class DataSetParser:
    def __init__(self, source: InputSource):
        self.source = source

    def __iter__(self) -> Iterator[List[int]]:
        while True:
            line = self.source.next_line()
            if line is None:
                break
            line = line.strip()
            if not line.isdigit():
                continue
            n = int(line)
            if n == 0:
                break
            data = []
            count = 0
            while count < n:
                c_line = self.source.next_line()
                if c_line is None:
                    break
                c_line = c_line.strip()
                if not c_line.isdigit():
                    continue
                c = int(c_line)
                if c < 0 or c > 9:
                    continue
                data.append(c)
                count += 1
            if len(data) == n:
                yield data

class HistogramModel:
    def __init__(self, sales: List[int], flavor_count: int = 10):
        self.flavor_count = flavor_count
        self.sales = sales
        self.counts = [0]*self.flavor_count
        self._calculate()

    def _calculate(self) -> None:
        for flavor in self.sales:
            if 0 <= flavor < self.flavor_count:
                self.counts[flavor] += 1

    def counts_for_flavor(self, flavor: int) -> int:
        if 0 <= flavor < self.flavor_count:
            return self.counts[flavor]
        raise IndexError("Flavor index out of range")

class HistogramView:
    def __init__(self, model: HistogramModel):
        self.model = model

    def render(self) -> List[str]:
        lines = []
        for flavor in range(self.model.flavor_count):
            c = self.model.counts_for_flavor(flavor)
            if c == 0:
                lines.append("-")
            else:
                lines.append("*" * c)
        return lines

class HistogramController:
    def __init__(self, data_iter: Iterator[List[int]]):
        self.data_iter = data_iter

    def process_all(self) -> None:
        for sales_data in self.data_iter:
            model = HistogramModel(sales_data)
            view = HistogramView(model)
            for line in view.render():
                print(line)

def main():
    input_source = StdInputSource()
    parser = DataSetParser(input_source)
    controller = HistogramController(iter(parser))
    controller.process_all()

if __name__ == "__main__":
    main()