class Coin:
    def __init__(self, denomination: int, count: int):
        self.denomination = denomination
        self.count = count

    def total_value(self) -> int:
        return self.denomination * self.count


class Wallet:
    def __init__(self, coins):
        if not all(isinstance(c, Coin) for c in coins):
            raise TypeError("All elements must be instances of Coin")
        self.coins = coins

    def total_coin_value(self) -> int:
        return sum(coin.total_value() for coin in self.coins)

    def can_exchange_for_bill(self) -> bool:
        return self.total_coin_value() >= 1000


class InputParser:
    @staticmethod
    def parse(input_line: str) -> Wallet:
        try:
            counts = list(map(int, input_line.strip().split()))
            if len(counts) != 6:
                raise ValueError("Input must have exactly 6 numbers.")
            for c in counts:
                if not (0 <= c <= 50):
                    raise ValueError("Coin counts must be between 0 and 50 inclusive.")
            denominations = [1, 5, 10, 50, 100, 500]
            coins = [Coin(d, cnt) for d, cnt in zip(denominations, counts)]
            return Wallet(coins)
        except Exception as e:
            raise ValueError(f"Invalid input format: {e}")


class OutputHandler:
    @staticmethod
    def output(can_exchange: bool):
        print(1 if can_exchange else 0)


def main():
    import sys
    input_line = sys.stdin.readline()
    wallet = InputParser.parse(input_line)
    result = wallet.can_exchange_for_bill()
    OutputHandler.output(result)


if __name__ == "__main__":
    main()