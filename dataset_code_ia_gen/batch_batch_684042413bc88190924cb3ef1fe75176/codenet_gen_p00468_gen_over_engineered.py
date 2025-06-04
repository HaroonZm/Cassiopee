class StudentNetwork:
    class FriendshipGraph:
        def __init__(self, num_students):
            self.num_students = num_students
            # Adjacency list: key=student_id, value=set of friend student_ids
            self.adjacency = {i: set() for i in range(1, num_students + 1)}

        def add_friendship(self, a, b):
            self.adjacency[a].add(b)
            self.adjacency[b].add(a)

        def find_friends_and_friends_of_friends(self, start_student):
            # We want students at distance 1 or 2 excluding the start_student
            # Breadth-first search limited to distance 2
            from collections import deque

            visited = {start_student: 0}
            queue = deque([start_student])
            invited = set()

            while queue:
                current = queue.popleft()
                current_distance = visited[current]

                # If distance is 2, do not go deeper
                if current_distance == 2:
                    continue

                for neighbor in self.adjacency[current]:
                    if neighbor not in visited:
                        visited[neighbor] = current_distance + 1
                        if visited[neighbor] <= 2 and neighbor != start_student:
                            invited.add(neighbor)
                        queue.append(neighbor)
            return invited

    def __init__(self):
        self.datasets = []

    def add_dataset(self, n, m, friendships):
        graph = self.FriendshipGraph(n)
        for a, b in friendships:
            graph.add_friendship(a, b)
        self.datasets.append(graph)

    def compute_invites(self):
        # For each dataset, compute friends and friends-of-friends of student 1
        results = []
        for graph in self.datasets:
            invited_students = graph.find_friends_and_friends_of_friends(1)
            results.append(len(invited_students))
        return results

class InputOutputHandler:
    def __init__(self):
        self.student_network = StudentNetwork()

    def parse_input(self):
        import sys
        lines_iter = iter(sys.stdin.read().splitlines())
        while True:
            try:
                n = int(next(lines_iter))
                m = int(next(lines_iter))
                if n == 0 and m == 0:
                    break
                friendships = []
                for _ in range(m):
                    a, b = map(int, next(lines_iter).split())
                    friendships.append((a,b))
                self.student_network.add_dataset(n, m, friendships)
            except StopIteration:
                break

    def output_results(self):
        results = self.student_network.compute_invites()
        for res in results:
            print(res)

def main():
    ioh = InputOutputHandler()
    ioh.parse_input()
    ioh.output_results()

if __name__ == "__main__":
    main()