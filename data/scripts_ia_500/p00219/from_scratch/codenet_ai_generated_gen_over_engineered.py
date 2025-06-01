class SalesData:
    def __init__(self, total_sales: int, sales_items: list[int]) -> None:
        self.total_sales = total_sales
        self.sales_items = sales_items

    def count_sales(self) -> dict[int, int]:
        counter = {i: 0 for i in range(10)}
        for item in self.sales_items:
            counter[item] += 1
        return counter


class HistogramRenderer:
    def __init__(self, sales_counter: dict[int, int]) -> None:
        self.sales_counter = sales_counter

    def render_line(self, item_number: int) -> str:
        count = self.sales_counter.get(item_number, 0)
        if count == 0:
            return "-"
        return "*" * count

    def render_all(self) -> list[str]:
        return [self.render_line(i) for i in range(10)]


class InputParser:
    def __init__(self) -> None:
        self.datasets: list[SalesData] = []

    def parse(self) -> None:
        while True:
            try:
                n = input()
                if n == '0':
                    break
                total_sales = int(n)
                sales_items = [int(input()) for _ in range(total_sales)]
                self.datasets.append(SalesData(total_sales, sales_items))
            except EOFError:
                break  # Graceful termination on EOF


class SalesHistogramApp:
    def __init__(self) -> None:
        self.parser = InputParser()

    def execute(self) -> None:
        self.parser.parse()
        for dataset in self.parser.datasets:
            sales_counter = dataset.count_sales()
            renderer = HistogramRenderer(sales_counter)
            output_lines = renderer.render_all()
            for line in output_lines:
                print(line)


if __name__ == "__main__":
    app = SalesHistogramApp()
    app.execute()