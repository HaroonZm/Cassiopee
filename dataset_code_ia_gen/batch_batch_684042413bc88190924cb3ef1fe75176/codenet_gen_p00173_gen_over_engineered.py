class ClassEntry:
    def __init__(self, name: str, morning_visitors: int, afternoon_visitors: int):
        self.name = name
        self.morning_visitors = morning_visitors
        self.afternoon_visitors = afternoon_visitors

    def total_visitors(self) -> int:
        return self.morning_visitors + self.afternoon_visitors

class FeeStructure:
    MORNING_FEE = 200
    AFTERNOON_FEE = 300

    @classmethod
    def calculate_income(cls, morning_visitors: int, afternoon_visitors: int) -> int:
        return morning_visitors * cls.MORNING_FEE + afternoon_visitors * cls.AFTERNOON_FEE

class HauntedHouseFestival:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry: ClassEntry):
        self.entries.append(entry)

    def generate_report(self):
        for entry in self.entries:
            total = entry.total_visitors()
            income = FeeStructure.calculate_income(entry.morning_visitors, entry.afternoon_visitors)
            print(entry.name, total, income)

def input_handler() -> HauntedHouseFestival:
    festival = HauntedHouseFestival()
    for _ in range(9):
        data = input().strip().split()
        name = data[0]
        morning_visitors = int(data[1])
        afternoon_visitors = int(data[2])
        festival.add_entry(ClassEntry(name, morning_visitors, afternoon_visitors))
    return festival

def main():
    festival = input_handler()
    festival.generate_report()

if __name__ == "__main__":
    main()