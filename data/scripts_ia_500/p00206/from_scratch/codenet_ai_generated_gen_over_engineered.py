class MonthlyRecord:
    def __init__(self, income: int, expense: int):
        self.income = income
        self.expense = expense

    @property
    def saving(self) -> int:
        return self.income - self.expense


class SavingsPlan:
    def __init__(self, target: int, monthly_records: list[MonthlyRecord]):
        self.target = target
        self.monthly_records = monthly_records

    def months_to_reach_target(self) -> str:
        total_savings = 0
        for i, record in enumerate(self.monthly_records, start=1):
            total_savings += record.saving
            if total_savings >= self.target:
                return str(i)
        return "NA"


class InputParser:
    def __init__(self):
        self._buffer = []

    def parse(self) -> list[SavingsPlan]:
        savings_plans = []
        while True:
            line = input().strip()
            if line == "0":
                break
            target = int(line)

            monthly_records = []
            for _ in range(12):
                parts = input().strip().split()
                income, expense = map(int, parts)
                monthly_records.append(MonthlyRecord(income, expense))

            savings_plans.append(SavingsPlan(target, monthly_records))
        return savings_plans


class SavingsPlanProcessor:
    def __init__(self, plans: list[SavingsPlan]):
        self.plans = plans

    def process(self) -> list[str]:
        results = []
        for plan in self.plans:
            results.append(plan.months_to_reach_target())
        return results


def main():
    parser = InputParser()
    plans = parser.parse()
    processor = SavingsPlanProcessor(plans)
    results = processor.process()
    for r in results:
        print(r)


if __name__ == "__main__":
    main()