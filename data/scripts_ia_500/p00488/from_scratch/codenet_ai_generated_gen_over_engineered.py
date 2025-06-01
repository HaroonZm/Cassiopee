class MenuComponent:
    def __init__(self, price: int):
        self.price = price

    def get_price(self) -> int:
        return self.price

class Pasta(MenuComponent):
    pass

class Juice(MenuComponent):
    pass

class MenuCollection:
    def __init__(self, items: list[MenuComponent]):
        self.items = items

    def get_min_price(self) -> int:
        if not self.items:
            raise ValueError("MenuCollection is empty")
        return min(item.get_price() for item in self.items)

class LunchSet:
    DISCOUNT = 50

    def __init__(self, pastas: MenuCollection, juices: MenuCollection):
        self.pastas = pastas
        self.juices = juices

    def calculate_min_set_price(self) -> int:
        min_price = float('inf')
        for pasta in self.pastas.items:
            for juice in self.juices.items:
                total = pasta.get_price() + juice.get_price() - self.DISCOUNT
                if total < min_price:
                    min_price = total
        return min_price

class InputHandler:
    def __init__(self):
        self.raw_values = []

    def read_input(self):
        for _ in range(5):
            value = int(input())
            if not (100 <= value <= 2000):
                raise ValueError("Price must be between 100 and 2000")
            self.raw_values.append(value)

    def get_pastas_and_juices(self) -> tuple[MenuCollection, MenuCollection]:
        pastas = [Pasta(price) for price in self.raw_values[:3]]
        juices = [Juice(price) for price in self.raw_values[3:]]
        return MenuCollection(pastas), MenuCollection(juices)

def main():
    handler = InputHandler()
    handler.read_input()
    pastas, juices = handler.get_pastas_and_juices()
    lunch_set = LunchSet(pastas, juices)
    print(lunch_set.calculate_min_set_price())

if __name__ == "__main__":
    main()