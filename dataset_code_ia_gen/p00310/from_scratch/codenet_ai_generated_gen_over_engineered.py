class Department(ABC):
    def __init__(self, participants: int) -> None:
        self._validate_participants(participants)
        self._participants = participants

    @staticmethod
    def _validate_participants(participants: int) -> None:
        if not (0 <= participants <= 10000):
            raise ValueError("参加者数は0以上10000以下でなければなりません。")

    @property
    def participants(self) -> int:
        return self._participants

    @abstractmethod
    def department_name(self) -> str:
        pass

class ProgrammingDepartment(Department):
    def department_name(self) -> str:
        return "プログラミング部門"

class MobileDepartment(Department):
    def department_name(self) -> str:
        return "モバイル部門"

class IchimaiCGDepartment(Department):
    def department_name(self) -> str:
        return "いちまいの絵ＣＧ部門"

class CompetitionParticipants:
    def __init__(self, departments: List[Department]) -> None:
        self._departments = departments

    def total_participants(self) -> int:
        return sum(dept.participants for dept in self._departments)

    @classmethod
    def from_input_string(cls, input_str: str) -> 'CompetitionParticipants':
        parts = input_str.strip().split()
        if len(parts) != 3:
            raise ValueError("入力は3つの整数で構成されている必要があります。")
        p, m, c = map(int, parts)
        departments = [
            ProgrammingDepartment(p),
            MobileDepartment(m),
            IchimaiCGDepartment(c)
        ]
        return cls(departments)

def main() -> None:
    import sys
    input_line = sys.stdin.readline()
    competition = CompetitionParticipants.from_input_string(input_line)
    print(competition.total_participants())

if __name__ == "__main__":
    main()