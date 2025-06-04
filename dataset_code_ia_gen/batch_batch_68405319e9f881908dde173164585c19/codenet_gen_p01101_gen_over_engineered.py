class Dataset:
    def __init__(self, n: int, m: int, prices: list[int]):
        self.n = n
        self.m = m
        self.prices = prices

    def __str__(self):
        return f'Dataset(n={self.n}, m={self.m}, prices={self.prices})'


class ShoppingCatalogue:
    def __init__(self, prices: list[int]):
        self._prices = prices
        self._sorted_prices = sorted(prices)

    def find_best_pair_sum(self, max_amount: int) -> int | None:
        left = 0
        right = len(self._sorted_prices) - 1
        best_sum = None
        while left < right:
            current_sum = self._sorted_prices[left] + self._sorted_prices[right]
            if current_sum <= max_amount:
                if (best_sum is None) or (current_sum > best_sum):
                    best_sum = current_sum
                left += 1
            else:
                right -= 1
        return best_sum


class TaroShoppingSolver:
    def __init__(self):
        self._datasets: list[Dataset] = []

    def add_dataset(self, dataset: Dataset):
        self._datasets.append(dataset)

    def solve_all(self) -> list[str]:
        results = []
        for dataset in self._datasets:
            catalogue = ShoppingCatalogue(dataset.prices)
            best_sum = catalogue.find_best_pair_sum(dataset.m)
            results.append(str(best_sum) if best_sum is not None else 'NONE')
        return results


class InputParser:
    @staticmethod
    def parse_input() -> list[Dataset]:
        datasets = []
        while True:
            line = input().strip()
            if not line:
                continue
            n_str, m_str = line.split()
            n, m = int(n_str), int(m_str)
            if n == 0 and m == 0:
                break
            prices_line = ''
            while len(prices_line.split()) < n:
                prices_line += ' ' + input().strip()
            prices = list(map(int, prices_line.strip().split()))
            datasets.append(Dataset(n, m, prices))
        return datasets


def main():
    parser = InputParser()
    solver = TaroShoppingSolver()
    datasets = parser.parse_input()
    for ds in datasets:
        solver.add_dataset(ds)
    results = solver.solve_all()
    for res in results:
        print(res)


if __name__ == '__main__':
    main()