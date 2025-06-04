class Participant:
    def __init__(self, score: int):
        self.score = score

class UniversityTeam:
    def __init__(self, name: str):
        self.name = name
        self.participants = []

    def add_participant(self, participant: Participant):
        self.participants.append(participant)

    def top_n_score_sum(self, n: int) -> int:
        sorted_scores = sorted((p.score for p in self.participants), reverse=True)
        return sum(sorted_scores[:n])

class Contest:
    def __init__(self, teams: list, top_n: int):
        self.teams = teams
        self.top_n = top_n

    def calculate_scores(self) -> dict:
        return {team.name: team.top_n_score_sum(self.top_n) for team in self.teams}

class InputParser:
    def __init__(self, lines: list):
        self.lines = lines

    def parse(self) -> Contest:
        if len(self.lines) != 20:
            raise ValueError("Expected exactly 20 lines of input")

        w_team = UniversityTeam("W")
        k_team = UniversityTeam("K")

        for i in range(10):
            score = int(self.lines[i])
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100")
            w_team.add_participant(Participant(score))

        for i in range(10, 20):
            score = int(self.lines[i])
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100")
            k_team.add_participant(Participant(score))

        return Contest([w_team, k_team], 3)

def main():
    import sys
    input_lines = [line.rstrip('\n') for line in sys.stdin]
    parser = InputParser(input_lines)
    contest = parser.parse()
    scores = contest.calculate_scores()
    print(f"{scores['W']} {scores['K']}")

if __name__ == "__main__":
    main()