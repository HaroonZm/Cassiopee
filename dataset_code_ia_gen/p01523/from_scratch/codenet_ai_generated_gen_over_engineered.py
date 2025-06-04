class RoomRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def covers(self, room: int) -> bool:
        return self.start <= room <= self.end


class Professor:
    def __init__(self, id_: int, room_range: RoomRange):
        self.id = id_
        self.range = room_range

    def covers(self, room: int) -> bool:
        return self.range.covers(room)


class PowerCoverageProblem:
    def __init__(self, total_rooms: int, professors: list):
        self.total_rooms = total_rooms
        self.professors = professors

    def is_full_coverage(self, selected_professors: set) -> bool:
        covered = [False] * (self.total_rooms + 1)
        for pid in selected_professors:
            prof = self.professors[pid]
            for room_num in range(prof.range.start, prof.range.end + 1):
                covered[room_num] = True
        return all(covered[1:])

    def solve_min_professors(self) -> str:
        # Using a backtracking with pruning because constraints are small
        best_solution_count = [float('inf')]  # mutable wrapper to share state

        # Sort professors by coverage length descending could help early pruning
        sorted_professors = sorted(
            enumerate(self.professors),
            key=lambda x: x[1].range.end - x[1].range.start,
            reverse=True
        )

        def backtrack(selected_set: set, idx: int):
            if idx == len(sorted_professors):
                if self.is_full_coverage(selected_set):
                    best_solution_count[0] = min(best_solution_count[0], len(selected_set))
                return
            # Prune if already no improvement
            if len(selected_set) >= best_solution_count[0]:
                return
            # Option 1: choose this professor
            selected_set.add(sorted_professors[idx][0])
            backtrack(selected_set, idx + 1)
            selected_set.remove(sorted_professors[idx][0])
            # Option 2: skip this professor if possible
            backtrack(selected_set, idx + 1)

        backtrack(set(), 0)
        return str(best_solution_count[0]) if best_solution_count[0] != float('inf') else "Impossible"


class InputParser:
    @staticmethod
    def parse_input() -> PowerCoverageProblem:
        import sys
        input_data = sys.stdin.read().strip().split()
        N = int(input_data[0])
        M = int(input_data[1])
        professors = []
        for i in range(M):
            a = int(input_data[2 + 2 * i])
            b = int(input_data[3 + 2 * i])
            professors.append(Professor(i, RoomRange(a, b)))
        return PowerCoverageProblem(N, professors)


def main():
    problem = InputParser.parse_input()
    result = problem.solve_min_professors()
    print(result)


if __name__ == "__main__":
    main()