class PencilSet:
    def __init__(self, quantity: int, price: int):
        self.quantity = quantity
        self.price = price

    def min_cost_for(self, required: int) -> int:
        # nombre de paquets nécessaires pour atteindre au moins required
        packages_needed = -(-required // self.quantity)  # division plafond
        return packages_needed * self.price

class PencilsPurchase:
    def __init__(self, required: int, set_x: PencilSet, set_y: PencilSet):
        self.required = required
        self.set_x = set_x
        self.set_y = set_y

    def compute_min_cost(self) -> int:
        cost_x = self.set_x.min_cost_for(self.required)
        cost_y = self.set_y.min_cost_for(self.required)
        return min(cost_x, cost_y)

class InputParser:
    @staticmethod
    def parse() -> PencilsPurchase:
        # lecture et extraction des valeurs
        import sys
        data = sys.stdin.read().strip().split()
        N, A, B, C, D = map(int, data)
        set_x = PencilSet(A, B)
        set_y = PencilSet(C, D)
        return PencilsPurchase(N, set_x, set_y)

def main():
    purchase = InputParser.parse()
    result = purchase.compute_min_cost()
    print(result)

if __name__ == "__main__":
    main()