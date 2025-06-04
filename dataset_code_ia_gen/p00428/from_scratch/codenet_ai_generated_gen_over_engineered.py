class TravelPreference:
    def __init__(self, place_id: int):
        self.place_id = place_id
        self.votes = 0

    def add_vote(self, vote: int):
        self.votes += vote

    def __lt__(self, other):
        # Sort by votes descending, then by place_id ascending
        if self.votes == other.votes:
            return self.place_id < other.place_id
        return self.votes > other.votes

class TravelSurvey:
    def __init__(self, n_students: int, m_places: int):
        self.n_students = n_students
        self.m_places = m_places
        self.preferences = [TravelPreference(i + 1) for i in range(m_places)]

    def record_student_votes(self, votes: list[int]):
        for i, vote in enumerate(votes):
            self.preferences[i].add_vote(vote)

    def get_ranking(self) -> list[int]:
        sorted_preferences = sorted(self.preferences)
        return [pref.place_id for pref in sorted_preferences]

class InputParser:
    def __init__(self):
        self.datasets = []

    def parse_input(self):
        import sys
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            n_m = list(map(int, line.split()))
            if len(n_m) != 2:
                continue
            n, m = n_m
            if n == 0 and m == 0:
                break
            survey = TravelSurvey(n, m)
            for _ in range(n):
                votes_line = sys.stdin.readline().strip()
                votes = list(map(int, votes_line.split()))
                survey.record_student_votes(votes)
            self.datasets.append(survey)

class OutputHandler:
    def __init__(self, datasets: list[TravelSurvey]):
        self.datasets = datasets

    def output_results(self):
        for survey in self.datasets:
            ranking = survey.get_ranking()
            print(*ranking)

class TravelSurveyProcessor:
    def __init__(self):
        self.parser = InputParser()
        self.datasets = []

    def run(self):
        self.parser.parse_input()
        self.datasets = self.parser.datasets
        output = OutputHandler(self.datasets)
        output.output_results()

if __name__ == "__main__":
    processor = TravelSurveyProcessor()
    processor.run()