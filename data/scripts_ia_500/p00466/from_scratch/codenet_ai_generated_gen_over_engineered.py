class ReceiptDataSet:
    def __init__(self, total_price: int, known_prices: list[int]):
        self.total_price = total_price
        self.known_prices = known_prices

    def missing_price(self) -> int:
        return self.total_price - sum(self.known_prices)

class ReceiptProcessor:
    def __init__(self):
        self.datasets = []

    def add_dataset(self, dataset: ReceiptDataSet):
        self.datasets.append(dataset)

    def process_all(self) -> list[int]:
        return [dataset.missing_price() for dataset in self.datasets]

class InputReader:
    def __init__(self, input_stream):
        self.input_stream = input_stream

    def read_datasets(self) -> list[ReceiptDataSet]:
        datasets = []
        while True:
            total_line = self.input_stream.readline()
            if not total_line:
                break
            total_price = int(total_line.strip())
            if total_price == 0:
                break
            known_prices = []
            for _ in range(9):
                price_line = self.input_stream.readline()
                known_prices.append(int(price_line.strip()))
            datasets.append(ReceiptDataSet(total_price, known_prices))
            if len(datasets) >= 5:
                break
        return datasets

class OutputWriter:
    def __init__(self, output_stream):
        self.output_stream = output_stream

    def write_results(self, results: list[int]):
        for missing in results:
            self.output_stream.write(f"{missing}\n")

def main():
    import sys
    reader = InputReader(sys.stdin)
    processor = ReceiptProcessor()
    datasets = reader.read_datasets()
    for dataset in datasets:
        processor.add_dataset(dataset)
    results = processor.process_all()
    writer = OutputWriter(sys.stdout)
    writer.write_results(results)

if __name__ == "__main__":
    main()