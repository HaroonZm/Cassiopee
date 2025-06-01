class AbstractDebtCalculator:
    def calculate(self, weeks: int) -> int:
        raise NotImplementedError("This method should be overridden in subclasses")

class LoanSharkDebtCalculator(AbstractDebtCalculator):
    def __init__(self, principal: int, interest_rate: float, round_to: int):
        self._principal = principal
        self._interest_rate = interest_rate
        self._round_to = round_to

    def _apply_interest(self, amount: int) -> float:
        return amount * (1 + self._interest_rate)

    def _round_up(self, amount: float) -> int:
        remainder = amount % self._round_to
        if remainder == 0:
            return int(amount)
        return int(amount) + (self._round_to - remainder)

    def calculate(self, weeks: int) -> int:
        current_debt = self._principal
        for _ in range(weeks):
            increased = self._apply_interest(current_debt)
            current_debt = self._round_up(increased)
        return current_debt

class DebtCalculationApplication:
    def __init__(self, calculator: AbstractDebtCalculator):
        self.calculator = calculator

    def run(self, weeks: int) -> int:
        return self.calculator.calculate(weeks)

def main():
    import sys

    class InputReader:
        @staticmethod
        def read_int():
            return int(sys.stdin.readline().strip())

    initial_principal = 100000
    weekly_interest_rate = 0.05
    rounding_unit = 1000

    weeks = InputReader.read_int()
    calculator = LoanSharkDebtCalculator(initial_principal, weekly_interest_rate, rounding_unit)
    app = DebtCalculationApplication(calculator)

    result = app.run(weeks)
    print(result)

if __name__ == "__main__":
    main()