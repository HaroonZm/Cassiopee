class InterestCalculator:
    def __init__(self, principal: float, years: int):
        self.principal = principal
        self.years = years

    def calculate(self, rate_percent: float) -> float:
        raise NotImplementedError("Subclasses should implement this method.")


class SimpleInterestCalculator(InterestCalculator):
    def calculate(self, rate_percent: float) -> float:
        # Simple interest formula: P * (1 + r * t)
        r = rate_percent / 100
        return self.principal * (1 + r * self.years)


class CompoundInterestCalculator(InterestCalculator):
    def calculate(self, rate_percent: float) -> float:
        # Compound interest formula: P * (1 + r) ** t
        r = rate_percent / 100
        return self.principal * ((1 + r) ** self.years)


class Bank:
    def __init__(self, bank_id: int, rate_percent: int, interest_type: int):
        self.bank_id = bank_id
        self.rate_percent = rate_percent
        self.interest_type = interest_type
        self.calculator = self._select_calculator()

    def _select_calculator(self) -> InterestCalculator:
        # Assuming principal is always 100 for normalization sake
        principal = 100.0
        # Interest type: 1 = simple, 2 = compound
        if self.interest_type == 1:
            return SimpleInterestCalculator(principal, None)  # years will be set later
        elif self.interest_type == 2:
            return CompoundInterestCalculator(principal, None)
        else:
            raise ValueError(f"Unknown interest type {self.interest_type}")

    def calculate_total(self, years: int) -> float:
        self.calculator.years = years
        return self.calculator.calculate(self.rate_percent)


class InterestCalculationSystem:
    def __init__(self):
        self.banks = []
        self.years = 0

    def load_data(self, n: int, y: int, bank_info: list):
        self.banks.clear()
        self.years = y
        for info in bank_info:
            b, r, t = info
            self.banks.append(Bank(b, r, t))

    def find_best_bank(self) -> int:
        # Returns bank_id with highest total amount
        best_bank_id = None
        best_total = float('-inf')
        for bank in self.banks:
            total = bank.calculate_total(self.years)
            if total > best_total:
                best_total = total
                best_bank_id = bank.bank_id
        return best_bank_id


class InputParser:
    def __init__(self):
        pass

    @staticmethod
    def parse():
        while True:
            line = input()
            if not line.strip():
                continue
            n = int(line)
            if n == 0:
                break
            y = int(input())
            bank_info = []
            for _ in range(n):
                b, r, t = map(int, input().split())
                bank_info.append((b, r, t))
            yield n, y, bank_info


def main():
    system = InterestCalculationSystem()
    parser = InputParser()
    for n, y, banks_data in parser.parse():
        system.load_data(n, y, banks_data)
        print(system.find_best_bank())


if __name__ == '__main__':
    main()