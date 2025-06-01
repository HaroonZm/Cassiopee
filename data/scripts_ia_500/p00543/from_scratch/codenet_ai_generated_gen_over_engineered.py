class Student:
    def __init__(self, initial_bib_number: int):
        self._bib_number = initial_bib_number

    @property
    def bib_number(self) -> int:
        return self._bib_number

    @bib_number.setter
    def bib_number(self, value: int):
        self._bib_number = value

    def remainder(self, k: int) -> int:
        return self._bib_number % k


class LineOfStudents:
    def __init__(self, students_bibs):
        self.students = [Student(bib) for bib in students_bibs]

    def perform_baton_pass(self, baton_number: int):
        # The baton always starts from student at index 0
        i = 0
        while i < len(self.students) - 1:
            current = self.students[i]
            next_student = self.students[i + 1]
            if current.remainder(baton_number) > next_student.remainder(baton_number):
                # Swap bib numbers between the two students
                current.bib_number, next_student.bib_number = next_student.bib_number, current.bib_number
            # Pass baton to next student
            i += 1

    def get_bibs(self):
        return [student.bib_number for student in self.students]


class BatonRelaySimulation:
    def __init__(self, n_students: int, m_batons: int, bibs_initial_state):
        self.n_students = n_students
        self.m_batons = m_batons
        self.line = LineOfStudents(bibs_initial_state)

    def run_simulation(self):
        # Baton 1 operation is trivial and does nothing (as implied by the statement)
        # Start simulation from baton 2 to baton M inclusive.
        for baton_number in range(2, self.m_batons + 1):
            self.line.perform_baton_pass(baton_number)

    def final_bibs(self):
        return self.line.get_bibs()


class InputParser:
    @staticmethod
    def parse_input():
        n_m = input().split()
        n = int(n_m[0])
        m = int(n_m[1])
        bibs = []
        for _ in range(n):
            bibs.append(int(input()))
        return n, m, bibs


class OutputFormatter:
    @staticmethod
    def print_bibs(bibs):
        for bib in bibs:
            print(bib)


def main():
    n, m, initial_bibs = InputParser.parse_input()
    simulation = BatonRelaySimulation(n, m, initial_bibs)
    simulation.run_simulation()
    final_bibs = simulation.final_bibs()
    OutputFormatter.print_bibs(final_bibs)


if __name__ == "__main__":
    main()