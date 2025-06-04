from abc import ABC, abstractmethod
from typing import List, Tuple

class MenuItem(ABC):
    def __init__(self, price: int):
        if not (100 <= price <= 2000):
            raise ValueError("Price must be between 100 and 2000 yen.")
        self.price = price

    @abstractmethod
    def get_price(self) -> int:
        pass

class Pasta(MenuItem):
    def get_price(self) -> int:
        return self.price

class Juice(MenuItem):
    def get_price(self) -> int:
        return self.price

class SetMenuCombination:
    def __init__(self, pasta: Pasta, juice: Juice, discount: int):
        self.pasta = pasta
        self.juice = juice
        self.discount = discount

    def total_price(self) -> int:
        return self.pasta.get_price() + self.juice.get_price() - self.discount

class Menu:
    def __init__(self, pastas: List[Pasta], juices: List[Juice], discount: int = 50):
        if len(pastas) != 3:
            raise ValueError("There must be exactly 3 pastas.")
        if len(juices) != 2:
            raise ValueError("There must be exactly 2 juices.")
        self.pastas = pastas
        self.juices = juices
        self.discount = discount

    def all_combinations(self) -> List[SetMenuCombination]:
        return [SetMenuCombination(pasta, juice, self.discount) for pasta in self.pastas for juice in self.juices]

    def find_min_price(self) -> int:
        combinations = self.all_combinations()
        min_price = min(c.total_price() for c in combinations)
        return min_price

class InputReader:
    @staticmethod
    def read_prices(num: int) -> List[int]:
        prices = []
        for _ in range(num):
            raw = input()
            # Defensive conversion
            try:
                val = int(raw.strip())
            except ValueError:
                raise ValueError(f"Invalid integer input: {raw}")
            prices.append(val)
        return prices

class LunchSetCalculator:
    def __init__(self, pasta_prices: List[int], juice_prices: List[int], discount: int = 50):
        self.menu = Menu([Pasta(p) for p in pasta_prices], [Juice(j) for j in juice_prices], discount)

    def calculate_min_set_price(self) -> int:
        return self.menu.find_min_price()

def main():
    pasta_prices = InputReader.read_prices(3)
    juice_prices = InputReader.read_prices(2)
    calculator = LunchSetCalculator(pasta_prices, juice_prices)
    print(calculator.calculate_min_set_price())

if __name__ == "__main__":
    main()