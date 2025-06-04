class WaterCompany:
    def calculate_fee(self, usage_liters: int) -> int:
        raise NotImplementedError("Subclasses must implement calculate_fee method")

class XCompany(WaterCompany):
    def __init__(self, rate_per_liter: int):
        self._rate_per_liter = rate_per_liter

    def calculate_fee(self, usage_liters: int) -> int:
        return self._rate_per_liter * usage_liters

class YCompany(WaterCompany):
    def __init__(self, base_fee: int, threshold_liters: int, additional_fee_per_liter: int):
        self._base_fee = base_fee
        self._threshold_liters = threshold_liters
        self._additional_fee_per_liter = additional_fee_per_liter

    def calculate_fee(self, usage_liters: int) -> int:
        if usage_liters <= self._threshold_liters:
            return self._base_fee
        else:
            extra_liters = usage_liters - self._threshold_liters
            return self._base_fee + self._additional_fee_per_liter * extra_liters

class WaterUsage:
    def __init__(self, usage_liters: int):
        self._usage_liters = usage_liters

    @property
    def usage_liters(self) -> int:
        return self._usage_liters

class WaterRateSelector:
    def __init__(self, companies: list[WaterCompany], usage: WaterUsage):
        self._companies = companies
        self._usage = usage

    def select_minimum_fee(self) -> int:
        fees = [company.calculate_fee(self._usage.usage_liters) for company in self._companies]
        return min(fees)

def main():
    class InputReader:
        def __init__(self):
            self._inputs = []

        def read_input(self):
            for _ in range(5):
                self._inputs.append(int(input()))
            return self._inputs

    reader = InputReader()
    A, B, C, D, P = reader.read_input()

    x_company = XCompany(rate_per_liter=A)
    y_company = YCompany(base_fee=B, threshold_liters=C, additional_fee_per_liter=D)
    usage = WaterUsage(usage_liters=P)

    selector = WaterRateSelector(companies=[x_company, y_company], usage=usage)
    min_fee = selector.select_minimum_fee()
    print(min_fee)

if __name__ == "__main__":
    main()