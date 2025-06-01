class ProductOrder:
    def __init__(self, name: str, quantity: int):
        self._validate_name(name)
        self.name = name
        self.quantity = quantity

    @staticmethod
    def _validate_name(name: str):
        if not (1 <= len(name) <= 5):
            raise ValueError("Product name length must be 1 to 5 characters.")
        if not all('A' <= ch <= 'Z' for ch in name):
            raise ValueError("Product name must contain only uppercase A-Z letters.")

    def __add__(self, other):
        if not isinstance(other, ProductOrder):
            return NotImplemented
        if self.name != other.name:
            raise ValueError("Cannot add ProductOrder with different names.")
        return ProductOrder(self.name, self.quantity + other.quantity)

    def __repr__(self):
        return f"{self.name} {self.quantity}"

class ProductOrderRepository:
    def __init__(self):
        self._orders = {}

    def add_order(self, product_order: ProductOrder):
        if product_order.name in self._orders:
            self._orders[product_order.name] = self._orders[product_order.name] + product_order
        else:
            self._orders[product_order.name] = product_order

    def aggregate(self):
        # returns a copy dictionary of product_name -> total_quantity (ProductOrder)
        return dict(self._orders)

    def sorted_orders(self):
        # sort by length ascending, then lex ascending
        return sorted(
            self._orders.values(),
            key=lambda po: (len(po.name), po.name)
        )

class OrderProcessor:
    def __init__(self, input_lines):
        self.input_lines = input_lines
        self.repository = ProductOrderRepository()
        self._parse_input()

    def _parse_input(self):
        try:
            n = int(self.input_lines[0].strip())
        except Exception as e:
            raise ValueError("First line must be an integer count of orders.") from e
        if n != len(self.input_lines) - 1:
            raise ValueError("Number of orders does not match given n.")
        for line in self.input_lines[1:]:
            parts = line.strip().split()
            if len(parts) != 2:
                raise ValueError(f"Invalid order line: '{line}'")
            name, quantity_str = parts
            quantity = int(quantity_str)
            order = ProductOrder(name, quantity)
            self.repository.add_order(order)

    def get_sorted_aggregated_orders(self):
        return self.repository.sorted_orders()

def main():
    import sys
    input_lines = sys.stdin.read().splitlines()
    processor = OrderProcessor(input_lines)
    sorted_aggregates = processor.get_sorted_aggregated_orders()
    for order in sorted_aggregates:
        print(order.name, order.quantity)

if __name__ == "__main__":
    main()