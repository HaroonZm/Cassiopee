class RandomNumberCampaign:
    class DayRandomNumber:
        def __init__(self, day_index: int, value: int):
            self.day_index = day_index
            self.value = value

        def is_happier_than(self, previous_day_random) -> bool:
            if previous_day_random is None:
                return False
            return self.value > previous_day_random.value

    class HappinessEvaluator:
        def __init__(self, random_numbers: list['RandomNumberCampaign.DayRandomNumber']):
            self.random_numbers = random_numbers

        def count_happy_days(self) -> int:
            count = 0
            previous_random = None
            for current_random in self.random_numbers:
                if current_random.is_happier_than(previous_random):
                    count += 1
                previous_random = current_random
            return count

    class InputReader:
        @staticmethod
        def read_int() -> int:
            return int(input())

        @staticmethod
        def read_int_list() -> list[int]:
            return list(map(int, input().split()))

    class OutputWriter:
        @staticmethod
        def write_line(output: int) -> None:
            print(output)

    def __init__(self):
        self.N = 0
        self.random_numbers: list[RandomNumberCampaign.DayRandomNumber] = []

    def read_input(self):
        self.N = self.InputReader.read_int()
        values = self.InputReader.read_int_list()
        self.random_numbers = [
            self.DayRandomNumber(day_index=i+1, value=val)
            for i, val in enumerate(values)
        ]

    def solve(self):
        evaluator = self.HappinessEvaluator(self.random_numbers)
        result = evaluator.count_happy_days()
        self.OutputWriter.write_line(result)

def main():
    campaign = RandomNumberCampaign()
    campaign.read_input()
    campaign.solve()

if __name__ == "__main__":
    main()