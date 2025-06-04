class DeliciousnessCollection:
    def __init__(self, values):
        self._values = values

    def total(self):
        # Sum of all elements, anticipating extensions like weighted sums
        return sum(self._values)

    def __iter__(self):
        return iter(self._values)

    def __len__(self):
        return len(self._values)


class CakeIngredientFactory:
    def __init__(self, cream_values, sponge_values):
        self._creams = DeliciousnessCollection(cream_values)
        self._sponges = DeliciousnessCollection(sponge_values)

    def create_all_cakes(self):
        # Generator of all cakes' deliciousness values, anticipating filtering or modifiers
        for cream_val in self._creams:
            for sponge_val in self._sponges:
                yield cream_val * sponge_val


class MercySanta:
    def __init__(self, cream_values, sponge_values):
        self._factory = CakeIngredientFactory(cream_values, sponge_values)

    def calculate_total_deliciousness(self):
        # Exploiting linearity to avoid O(N*M) iteration in naive way
        # Sum all creams and sponges separately and multiply to get total sum of products
        total_cream = sum(self._factory._creams._values)
        total_sponge = sum(self._factory._sponges._values)
        return total_cream * total_sponge


class InputParser:
    @staticmethod
    def parse_input():
        n, m = map(int, input().split())
        cream_values = list(map(int, input().split()))
        sponge_values = list(map(int, input().split()))
        if len(cream_values) != n or len(sponge_values) != m:
            raise ValueError("Input lengths do not match specified N and M")
        return cream_values, sponge_values


class OutputHandler:
    @staticmethod
    def print_result(value):
        print(value)


def main():
    cream_values, sponge_values = InputParser.parse_input()
    santa = MercySanta(cream_values, sponge_values)
    result = santa.calculate_total_deliciousness()
    OutputHandler.print_result(result)


if __name__ == "__main__":
    main()