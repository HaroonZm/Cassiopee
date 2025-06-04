class SubjectScore:
    def __init__(self, subject_name: str, score: int):
        self.subject_name = subject_name
        self.score = score

    def __repr__(self):
        return f"{self.subject_name}: {self.score}"

class StudentScores:
    def __init__(self, name: str, scores: list[SubjectScore]):
        self.name = name
        self.scores = scores

    @classmethod
    def from_input_line(cls, name: str, line: str, subject_order: list[str]):
        values = list(map(int, line.strip().split()))
        scores = [SubjectScore(subj, val) for subj, val in zip(subject_order, values)]
        return cls(name, scores)

    def total_score(self) -> int:
        return sum(score.score for score in self.scores)

class ScoreEvaluator:
    def __init__(self, students: list[StudentScores]):
        self.students = students

    def get_max_total_score(self) -> int:
        totals = [(student.name, student.total_score()) for student in self.students]
        max_score = max(totals, key=lambda x: x[1])[1]
        # Even if tied, return that score
        return max_score

def main():
    subject_order = ["情報", "数学", "理科", "英語"]

    student_a = StudentScores.from_input_line("A", input(), subject_order)
    student_b = StudentScores.from_input_line("B", input(), subject_order)

    evaluator = ScoreEvaluator([student_a, student_b])
    print(evaluator.get_max_total_score())

if __name__ == "__main__":
    main()