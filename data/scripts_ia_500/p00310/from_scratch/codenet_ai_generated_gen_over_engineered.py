class Division:
    def __init__(self, name: str, participants: int):
        self.name = name
        self.participants = participants

    def get_participants(self) -> int:
        return self.participants

class Competition:
    def __init__(self):
        self.divisions = []

    def add_division(self, division: Division):
        self.divisions.append(division)

    def total_participants(self) -> int:
        return sum(division.get_participants() for division in self.divisions)

class ParticipantsFactory:
    @staticmethod
    def from_input(input_line: str) -> Competition:
        parts = input_line.strip().split()
        if len(parts) != 3:
            raise ValueError("Input must have exactly three integers")
        p, m, c = map(int, parts)
        competition = Competition()
        competition.add_division(Division("プログラミング部門", p))
        competition.add_division(Division("モバイル部門", m))
        competition.add_division(Division("いちまいの絵ＣＧ部門", c))
        return competition

def main():
    import sys
    input_line = sys.stdin.readline()
    competition = ParticipantsFactory.from_input(input_line)
    print(competition.total_participants())

if __name__ == "__main__":
    main()