class PizzaComponent:
    def __init__(self, calories: int, price: int):
        self.calories = calories
        self.price = price

    def calorie_per_dollar(self) -> float:
        if self.price == 0:
            return 0
        return self.calories / self.price


class Dough(PizzaComponent):
    pass


class Topping(PizzaComponent):
    pass


class Pizza:
    def __init__(self, dough: Dough, toppings: list[Topping]):
        self.dough = dough
        self.toppings = toppings

    def total_calories(self) -> int:
        return self.dough.calories + sum(t.calories for t in self.toppings)

    def total_price(self) -> int:
        return self.dough.price + sum(t.price for t in self.toppings)

    def calorie_per_dollar(self) -> float:
        return self.total_calories() / self.total_price()


class PizzaFactory:
    def __init__(self, dough: Dough, topping_price: int, topping_calories: list[int]):
        self.dough = dough
        self.topping_price = topping_price
        self.toppings = [Topping(c, topping_price) for c in topping_calories]

    def generate_best_pizza(self) -> Pizza:
        # Because toppings cannot be duplicated, subsets need to be checked
        # To be excessively sophisticated: use a generator with a combinatorial iterator
        from itertools import combinations

        best_pizza = Pizza(self.dough, [])
        best_ratio = best_pizza.calorie_per_dollar()

        n = len(self.toppings)
        # Enumerate all subset sizes from 0 to n
        for k in range(n + 1):
            # For further sophistication: use a generator expression to lazily evaluate pizzas
            candidate_pizzas = (Pizza(self.dough, list(combo)) for combo in combinations(self.toppings, k))
            for pizza_candidate in candidate_pizzas:
                # Recalculate ratio
                ratio = pizza_candidate.calorie_per_dollar()
                # Select best (highest) calorie per dollar
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_pizza = pizza_candidate

        return best_pizza


class InputReader:
    @staticmethod
    def read_input() -> tuple[int, int, int, int, list[int]]:
        N = int(input())
        A, B = map(int, input().split())
        C = int(input())
        toppings_calories = [int(input()) for _ in range(N)]
        return N, A, B, C, toppings_calories


class BestPizzaSolver:
    def __init__(self):
        self.N = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.toppings_calories = []

    def load_input(self):
        self.N, self.A, self.B, self.C, self.toppings_calories = InputReader.read_input()

    def solve(self) -> int:
        dough = Dough(calories=self.C, price=self.A)
        factory = PizzaFactory(dough, self.B, self.toppings_calories)
        best_pizza = factory.generate_best_pizza()
        return int(best_pizza.calorie_per_dollar())  # floor by int cast as requested

    def run(self):
        self.load_input()
        answer = self.solve()
        print(answer)


if __name__ == "__main__":
    solver = BestPizzaSolver()
    solver.run()