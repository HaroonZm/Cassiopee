class SeatingRequirement:
    def __init__(self, desks: int, chairs_per_desk: int):
        self._desks = desks
        self._chairs_per_desk = chairs_per_desk

    @property
    def desks(self) -> int:
        return self._desks

    @property
    def chairs_per_desk(self) -> int:
        return self._chairs_per_desk

    def total_chairs(self) -> int:
        return self.desks * self.chairs_per_desk


class EventSetupInterface:
    def get_seating_requirement(self) -> SeatingRequirement:
        raise NotImplementedError("Must implement get_seating_requirement")


class ConsoleInputEventSetup(EventSetupInterface):
    def get_seating_requirement(self) -> SeatingRequirement:
        user_input = input().strip()
        parts = user_input.split()
        if len(parts) != 2:
            raise ValueError("Input must contain exactly two integers.")
        desks, chairs_per_desk = map(int, parts)
        if not (1 <= desks <= 100 and 1 <= chairs_per_desk <= 10):
            raise ValueError("Input values out of constraints.")
        return SeatingRequirement(desks, chairs_per_desk)


class SeatingRequirementCalculator:
    def __init__(self, setup: EventSetupInterface):
        self.setup = setup

    def calculate_total_chairs(self) -> int:
        seating_requirement = self.setup.get_seating_requirement()
        return seating_requirement.total_chairs()


def main():
    calculator = SeatingRequirementCalculator(ConsoleInputEventSetup())
    total = calculator.calculate_total_chairs()
    print(total)


if __name__ == "__main__":
    main()