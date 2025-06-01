import bisect
import sys
from typing import List, Dict, Tuple, Optional


class Student:
    def __init__(self, id_: int, score: int):
        self.id = id_
        self.score = score

    def __repr__(self):
        return f"Student(id={self.id}, score={self.score})"


class LeaderGroup:
    def __init__(self):
        self.leaders: Dict[int, Student] = {}  # id -> Student
        self.scores_sorted: List[int] = []  # sorted leader scores

    def add_leader(self, student: Student):
        if student.id in self.leaders:
            raise ValueError("Leader already added")
        self.leaders[student.id] = student
        bisect.insort(self.scores_sorted, student.score)

    def remove_leader(self, student: Student):
        if student.id not in self.leaders:
            raise ValueError("Leader does not exist")
        del self.leaders[student.id]
        idx = bisect.bisect_left(self.scores_sorted, student.score)
        self.scores_sorted.pop(idx)

    def get_min_score(self) -> Optional[int]:
        if not self.scores_sorted:
            return None
        return self.scores_sorted[0]

    def get_leader_scores(self) -> List[int]:
        return self.scores_sorted.copy()

    def count_unjoinable_students(self, students: List[Student], r: int) -> int:
        # Compute how many students cannot join any group given r
        if not self.scores_sorted:
            # no leaders means everyone cannot join any group
            return len(students)
        leaders = self.scores_sorted
        unjoinable = 0
        for st in students:
            if st.id in self.leaders:
                # leader always participates in own group
                continue
            # rule:
            # - must join a leader whose score s satisfies:
            #   s <= st.score and st.score < s + r + 1
            # same as st.score - s <= r and st.score >= s
            # find leader with s <= st.score and st.score - s <= r
            # so s in [st.score - r, st.score]
            low = st.score - r
            high = st.score
            # find leader s in leaders where low <= s <= high
            left_idx = bisect.bisect_left(leaders, low)
            right_idx = bisect.bisect_right(leaders, high)
            if left_idx >= right_idx:
                # no suitable leader found
                unjoinable += 1
        return unjoinable


class QueryProcessor:
    def __init__(self, students: List[Student]):
        self.students = students
        self.student_map = {st.id: st for st in students}
        self.groups = LeaderGroup()
        self.MAX_R = 10**9 + 1  # score max + 1

    def process(self, queries: List[Tuple[str, int]]):
        output = []
        for cmd, arg in queries:
            if cmd == "ADD":
                self._add_leader(arg)
            elif cmd == "REMOVE":
                self._remove_leader(arg)
            elif cmd == "CHECK":
                res = self._check_min_r(arg)
                output.append(res)
            else:
                raise ValueError("Unknown query command")
        return output

    def _add_leader(self, a: int):
        student = self.student_map[a]
        self.groups.add_leader(student)

    def _remove_leader(self, a: int):
        student = self.student_map[a]
        self.groups.remove_leader(student)

    def _check_min_r(self, x: int) -> str:
        if not self.groups.leaders:
            # no leaders, no participation possible except leaders none. So all non-leaders unjoinable = N
            # If x < number of non-leader students => NA else 0 if x >= non-leader students, but NO leaders means all 0
            # given condition => all students unjoinable except leaders = 0 since no leaders
            if x < len(self.students):
                return "NA"
            return "0"

        # binary search r in range [0, MAX_R]
        left, right = 0, self.MAX_R

        def condition(r):
            # how many unjoinable with r
            cnt = self.groups.count_unjoinable_students(self.students, r)
            return cnt <= x

        if not condition(self.MAX_R):
            return "NA"

        # binary search for minimal r
        while left < right:
            mid = (left + right) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return str(left)


def main():
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    students = []
    for i in range(1, N + 1):
        score = int(input())
        students.append(Student(i, score))

    queries = []
    for _ in range(Q):
        line = input().strip().split()
        if line[0] == "ADD" or line[0] == "REMOVE":
            queries.append((line[0], int(line[1])))
        else:  # CHECK
            queries.append((line[0], int(line[1])))

    processor = QueryProcessor(students)
    answers = processor.process(queries)
    for ans in answers:
        print(ans)


if __name__ == "__main__":
    main()