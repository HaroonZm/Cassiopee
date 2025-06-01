from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Iterator

class StoreSales:
    def __init__(self, name: str, morning_sales: int, afternoon_sales: int):
        self.name = name
        self.morning_sales = morning_sales
        self.afternoon_sales = afternoon_sales

    @property
    def total_sales(self) -> int:
        return self.morning_sales + self.afternoon_sales

class SalesDataSet:
    def __init__(self, stores: List[StoreSales]):
        self.stores = stores

    def get_top_store(self) -> StoreSales:
        # Assumes no tie as per problem statement
        return max(self.stores, key=lambda store: store.total_sales)

class InputParser(ABC):
    @abstractmethod
    def parse(self) -> Iterator[SalesDataSet]:
        pass

class ConsoleInputParser(InputParser):
    def __init__(self):
        self._store_names = ['A', 'B', 'C', 'D', 'E']

    def parse(self) -> Iterator[SalesDataSet]:
        while True:
            morning_line = input()
            if morning_line == "0 0":
                break
            morning_sales_values = list(map(int, morning_line.strip().split()))
            # If length doesn't match, try to read until we get all five
            while len(morning_sales_values) < 5:
                morning_sales_values.extend(map(int,input().strip().split()))
            afternoon_line = input()
            afternoon_sales_values = list(map(int, afternoon_line.strip().split()))
            while len(afternoon_sales_values) < 5:
                afternoon_sales_values.extend(map(int,input().strip().split()))
            stores = []
            for i, name in enumerate(self._store_names):
                stores.append(StoreSales(name, morning_sales_values[i], afternoon_sales_values[i]))
            yield SalesDataSet(stores)

class OutputFormatter(ABC):
    @abstractmethod
    def output(self, dataset: SalesDataSet) -> None:
        pass

class ConsoleOutputFormatter(OutputFormatter):
    def output(self, dataset: SalesDataSet) -> None:
        top_store = dataset.get_top_store()
        print(f"{top_store.name} {top_store.total_sales}")

class MarketSalesAnalyzer:
    def __init__(self, parser: InputParser, formatter: OutputFormatter):
        self.parser = parser
        self.formatter = formatter

    def run(self):
        for dataset in self.parser.parse():
            self.formatter.output(dataset)

if __name__ == "__main__":
    analyzer = MarketSalesAnalyzer(ConsoleInputParser(), ConsoleOutputFormatter())
    analyzer.run()