class Student:
    def __init__(self, student_id: int):
        self.id = student_id
        self.friends = set()

    def add_friend(self, other: 'Student'):
        self.friends.add(other)

    def __repr__(self):
        return f"Student({self.id})"


class GradeGroup:
    def __init__(self, grade: int, members: set):
        self.grade = grade
        self.members = members

    def contains(self, student_id: int) -> bool:
        return student_id in self.members


class SNSNetwork:
    def __init__(self, n: int):
        self.n = n
        self.students = {i: Student(i) for i in range(1, n + 1)}

    def add_friendship(self, x: int, y: int):
        self.students[x].add_friend(self.students[y])
        self.students[y].add_friend(self.students[x])

    def bfs_min_steps_to_grades(self, start_student_id: int, grade_groups: list) -> (int, set):
        """
        Perform a BFS to find the minimum communications required to spread the message
        to all grades, starting from start_student_id.

        Returns:
            (min_steps, grades_reached_set)
        """
        from collections import deque

        visited = set()
        queue = deque()
        queue.append((self.students[start_student_id], 0))  # (student, distance)
        visited.add(start_student_id)

        grades_reached = set()
        # Check if start student is in any grade
        for grade_group in grade_groups:
            if grade_group.contains(start_student_id):
                grades_reached.add(grade_group.grade)

        # Distance counts the number of friend communications so far
        min_steps = 0 if len(grades_reached) == len(grade_groups) else None

        while queue and len(grades_reached) < len(grade_groups):
            current_student, dist = queue.popleft()
            # All members of a grade get message instantly if one gets it
            # So if this student is in a grade not reached yet, add that grade
            for grade_group in grade_groups:
                if grade_group.grade not in grades_reached and grade_group.contains(current_student.id):
                    grades_reached.add(grade_group.grade)
                    # The communication cost till here is dist, no need to add
                    # Because group chat is instant
                    if len(grades_reached) == len(grade_groups):
                        # All grade groups reached, the minimal distance is dist
                        return dist, grades_reached

            # Explore friends to propagate message
            for friend in current_student.friends:
                if friend.id not in visited:
                    visited.add(friend.id)
                    queue.append((friend, dist + 1))

        # If all grade groups not reached (should not happen given problem statement)
        return min_steps if min_steps is not None else dist, grades_reached


class ModernAnnounceNetworkSolver:
    def __init__(self, n: int, A_ids: list, B_ids: list, C_ids: list, edges: list):
        self.n = n
        self.grade_groups = [
            GradeGroup(1, set(A_ids)),
            GradeGroup(2, set(B_ids)),
            GradeGroup(3, set(C_ids))
        ]
        self.network = SNSNetwork(n)
        for x, y in edges:
            self.network.add_friendship(x, y)

    def solve(self) -> (int, int):
        """
        Solve for the minimal communications and the student ID to start the broadcast.
        """
        # We need to find a student ID that yields minimal BFS distance such that
        # when message starts with this student, all grades receive the message.

        # According to problem statement, minimal distance must exist and message can be delivered to all.

        # Because the network is large, we want an efficient way.
        # We can leverage the fact that the message spreads instantly within each grade group,
        # so the BFS needs to find minimal steps to reach at least one member of each grade.

        # We try all students as start candidates and keep track of minimal communications and student id.

        # However, trying all N=10,000 students with BFS could be expensive,
        # so let's do a multi-source BFS approach from all members of each grade to precompute distances.

        # Construct a combined BFS spanning from all grade members simultaneously with 3 labels.

        import sys
        from collections import deque, defaultdict

        # For each grade, compute distance from each node to the closest member of that grade
        def bfs_from_grade(members: set):
            dist = [sys.maxsize] * (self.n + 1)
            queue = deque()
            for m in members:
                dist[m] = 0
                queue.append(m)
            while queue:
                u = queue.popleft()
                for friend in self.network.students[u].friends:
                    v = friend.id
                    if dist[v] == sys.maxsize:
                        dist[v] = dist[u] + 1
                        queue.append(v)
            return dist

        distA = bfs_from_grade(self.grade_groups[0].members)
        distB = bfs_from_grade(self.grade_groups[1].members)
        distC = bfs_from_grade(self.grade_groups[2].members)

        # We want to find a student s minimizing dist_to_start + (max distance to other grades starting from s)
        # Recall: If start student is in a grade, that grade instantly reached at cost 0.

        # The number of communications is min of distances to reach all other grades.

        # The formula for minimal communication from starting at s is:
        # max of distances_to_other_grades from s. Because starting point gets that grade instantly

        # However, since message spreads instantly within grade, total communication steps needed
        # = min distance from start to each grade member + message spreads instantly there.

        # Actually, the BFS from grades gives dist to nearest member of that grade.
        # So, starting at s means zero cost if s is member of that grade.
        # For other grades, distance computed by dist arrays.

        # The communications between friends = max dist to other grades from s, because
        # need to propagate to at least one member of each other grade.

        # So for each student s:
        # communication_cost(s) = max(dist to the other two grades except s's own grade, or these distances if s not in the grade).
        # But distances to the same grade is zero by definition if s is member.

        # We consider all three grades, minimal steps is max of the distances (for the other grades),
        # with zero for the grade s belongs to.

        min_communications = sys.maxsize
        best_student_id = None

        # Make quick lookup sets for membership
        setA = self.grade_groups[0].members
        setB = self.grade_groups[1].members
        setC = self.grade_groups[2].members

        for s in range(1, self.n + 1):
            # Determine which grades are covered instantly starting at s
            grades_covered = set()
            if s in setA:
                grades_covered.add(1)
            if s in setB:
                grades_covered.add(2)
            if s in setC:
                grades_covered.add(3)

            # The communication needed is max of distances to uncovered grades
            distances_to_cover = []
            if 1 not in grades_covered:
                distances_to_cover.append(distA[s])
            if 2 not in grades_covered:
                distances_to_cover.append(distB[s])
            if 3 not in grades_covered:
                distances_to_cover.append(distC[s])

            comm_needed = max(distances_to_cover) if distances_to_cover else 0

            if comm_needed < min_communications or (comm_needed == min_communications and (best_student_id is None or s < best_student_id)):
                min_communications = comm_needed
                best_student_id = s

        return min_communications, best_student_id


def main():
    import sys
    input = sys.stdin.readline

    N, A, B, C = map(int, input().split())
    A_ids = list(map(int, input().split()))
    B_ids = list(map(int, input().split()))
    C_ids = list(map(int, input().split()))
    M = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    solver = ModernAnnounceNetworkSolver(N, A_ids, B_ids, C_ids, edges)
    min_comm, student_id = solver.solve()
    print(min_comm, student_id)


if __name__ == "__main__":
    main()