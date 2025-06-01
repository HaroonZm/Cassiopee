class BMI:
    STANDARD_VALUE = 22.0

    def __init__(self, height_cm: int, weight_kg: int):
        self.height_m = height_cm / 100
        self.weight_kg = weight_kg
        self._value = self._calculate_bmi()

    def _calculate_bmi(self) -> float:
        return self.weight_kg / (self.height_m ** 2)

    @property
    def value(self) -> float:
        return self._value

    def deviation_from_standard(self) -> float:
        return abs(self._value - self.STANDARD_VALUE)


class Person:
    def __init__(self, registration_number: int, height_cm: int, weight_kg: int):
        self.registration_number = registration_number
        self.bmi = BMI(height_cm, weight_kg)

    def deviation_from_ideal(self) -> float:
        return self.bmi.deviation_from_standard()


class IdealBodyShapeSelector:
    def __init__(self, people: list):
        self.people = people

    def select_most_ideal(self) -> Person:
        # Sort by deviation then by registration number
        sorted_people = sorted(
            self.people,
            key=lambda person: (person.deviation_from_ideal(), person.registration_number)
        )
        return sorted_people[0]


class InputParser:
    def __init__(self, input_lines: list):
        self.input_lines = input_lines
        self.index = 0

    def _read_line(self) -> str:
        if self.index < len(self.input_lines):
            line = self.input_lines[self.index]
            self.index += 1
            return line
        return ''

    def parse_next_dataset(self):
        n_line = self._read_line()
        if not n_line or n_line.strip() == '0':
            return None
        n = int(n_line.strip())
        people = []
        for _ in range(n):
            line = self._read_line().strip()
            p_str, h_str, w_str = line.split()
            p, h, w = int(p_str), int(h_str), int(w_str)
            people.append(Person(p, h, w))
        return people


class OutputFormatter:
    @staticmethod
    def format_person(person: Person) -> str:
        return str(person.registration_number)


class BMIAnalyzerApplication:
    def __init__(self, input_lines: list):
        self.parser = InputParser(input_lines)
        self.formatter = OutputFormatter()

    def run(self):
        results = []
        while True:
            dataset = self.parser.parse_next_dataset()
            if dataset is None:
                break
            selector = IdealBodyShapeSelector(dataset)
            ideal_person = selector.select_most_ideal()
            results.append(self.formatter.format_person(ideal_person))
        return results


def main():
    import sys
    input_lines = [line.rstrip('\n') for line in sys.stdin]
    app = BMIAnalyzerApplication(input_lines)
    results = app.run()
    for res in results:
        print(res)


if __name__ == "__main__":
    main()