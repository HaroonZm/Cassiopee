class Student:
    def __init__(self, id):
        self.id = id
        self.friends = set()

    def add_friend(self, other):
        self.friends.add(other)

class FriendshipGraph:
    def __init__(self, n):
        self.students = {i: Student(i) for i in range(1, n+1)}

    def add_friendship(self, a, b):
        self.students[a].add_friend(b)
        self.students[b].add_friend(a)

    def get_invitees_count(self, origin_id=1):
        # Collect friends and friends of friends
        origin = self.students[origin_id]

        # Direct friends
        direct_friends = origin.friends

        # Friends of friends, excluding self and direct friends
        friends_of_friends = set()
        for friend_id in direct_friends:
            friends_of_friends.update(self.students[friend_id].friends)
        friends_of_friends -= direct_friends
        friends_of_friends.discard(origin_id)

        # Total invitees is the union of direct friends and their friends (excluding origin)
        invitees = direct_friends.union(friends_of_friends)
        return len(invitees)

class InputHandler:
    def __init__(self):
        self.datasets = []

    def read(self):
        while True:
            n = int(input())
            m = int(input())
            if n == 0 and m == 0:
                break
            friendships = []
            for _ in range(m):
                a,b = map(int,input().split())
                friendships.append((a,b))
            self.datasets.append((n, m, friendships))

class PartyPlanner:
    def __init__(self, datasets):
        self.datasets = datasets

    def plan(self):
        results = []
        for n, m, friendships in self.datasets:
            graph = FriendshipGraph(n)
            for a,b in friendships:
                graph.add_friendship(a,b)
            count = graph.get_invitees_count()
            results.append(count)
        return results

def main():
    handler = InputHandler()
    handler.read()
    planner = PartyPlanner(handler.datasets)
    results = planner.plan()
    for res in results:
        print(res)

if __name__ == "__main__":
    main()