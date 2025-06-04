class CurrencySeries:
    def __init__(self, rates):
        self.rates = rates

    def __len__(self):
        return len(self.rates)

    def __getitem__(self, idx):
        return self.rates[idx]

class ProfitCalculator:
    def __init__(self, currency_series):
        self.currency_series = currency_series

    def calculate_max_profit(self):
        if len(self.currency_series) < 2:
            raise ValueError("At least two rate entries are required to calculate profit.")
        min_rate = self.currency_series[0]
        max_profit = self.currency_series[1] - self.currency_series[0]
        for t in range(1, len(self.currency_series)):
            current_rate = self.currency_series[t]
            profit = current_rate - min_rate
            if profit > max_profit:
                max_profit = profit
            if current_rate < min_rate:
                min_rate = current_rate
        return max_profit

class InputParser:
    @staticmethod
    def read_integer():
        return int(input().strip())

    @staticmethod
    def read_rate_list(n):
        rates = []
        for _ in range(n):
            rate = int(input().strip())
            rates.append(rate)
        return rates

class OutputFormatter:
    @staticmethod
    def print_result(result):
        print(result)

class MaximumProfitApp:
    def __init__(self):
        self.parser = InputParser()
        self.formatter = OutputFormatter()

    def run(self):
        n = self.parser.read_integer()
        rates = self.parser.read_rate_list(n)
        currency_series = CurrencySeries(rates)
        calculator = ProfitCalculator(currency_series)
        max_profit = calculator.calculate_max_profit()
        self.formatter.print_result(max_profit)

if __name__ == "__main__":
    app = MaximumProfitApp()
    app.run()