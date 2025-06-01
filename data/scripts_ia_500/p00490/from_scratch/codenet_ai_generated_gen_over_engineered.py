class Ingredient:
    def __init__(self, calories: int, price: int):
        self.calories = calories
        self.price = price

    def calorie_per_dollar(self) -> float:
        if self.price == 0:
            return float('inf')
        return self.calories / self.price

class PizzaBase(Ingredient):
    pass

class Topping(Ingredient):
    pass

class Pizza:
    def __init__(self, base: PizzaBase, toppings=None):
        if toppings is None:
            toppings = []
        self.base = base
        self.toppings = toppings

    def total_calories(self) -> int:
        return self.base.calories + sum(t.calories for t in self.toppings)

    def total_price(self) -> int:
        return self.base.price + sum(t.price for t in self.toppings)

    def calorie_per_dollar(self) -> float:
        if self.total_price() == 0:
            return float('inf')
        return self.total_calories() / self.total_price()

class PizzaBuilder:
    def __init__(self, base: PizzaBase, toppings: list):
        self.base = base
        self.toppings = sorted(toppings, key=lambda t: t.calorie_per_dollar(), reverse=True)

    def build_best_pizza(self) -> Pizza:
        # Greedy selection of toppings by calorie_per_dollar ratio
        selected = []
        current_pizza = Pizza(self.base, selected)
        best_pizza = current_pizza

        for topping in self.toppings:
            new_pizza = Pizza(self.base, selected + [topping])
            if new_pizza.calorie_per_dollar() >= best_pizza.calorie_per_dollar():
                selected.append(topping)
                best_pizza = new_pizza

        return best_pizza

class InputParser:
    @staticmethod
    def parse() -> tuple:
        N = int(input())
        A, B = map(int, input().split())
        C = int(input())
        base = PizzaBase(C, A)
        toppings = [Topping(int(input()), B) for _ in range(N)]
        return base, toppings

class BestPizzaSolver:
    def __init__(self):
        self.base, self.toppings = InputParser.parse()
        self.builder = PizzaBuilder(self.base, self.toppings)

    def solve(self) -> int:
        best_pizza = self.builder.build_best_pizza()
        return int(best_pizza.calorie_per_dollar())

if __name__ == "__main__":
    solver = BestPizzaSolver()
    print(solver.solve())