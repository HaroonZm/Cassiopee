class Participant:
    def __init__(self, identifier: int):
        self.identifier = identifier

    def __repr__(self):
        return f"Participant({self.identifier})"

class Circle:
    def __init__(self, participants):
        self.participants = participants

    def is_empty(self):
        return len(self.participants) == 0

    def size(self):
        return len(self.participants)

    def remove_at(self, index: int):
        removed = self.participants.pop(index)
        return removed

    def get_at(self, index: int):
        return self.participants[index]

class JosephusGame:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.circle = Circle([Participant(i) for i in range(1, n+1)])

    def play(self):
        # The position from which to start counting (index-based)
        current_index = 0
        while self.circle.size() > 1:
            # Calculate the index of the participant to remove
            current_index = (current_index + self.m - 1) % self.circle.size()
            self.circle.remove_at(current_index)
        # The winner is the last remaining participant
        return self.circle.get_at(0).identifier

class JosephusSolver:
    def __init__(self):
        self.games = []

    def add_game(self, n: int, m: int):
        self.games.append(JosephusGame(n, m))

    def solve_all(self):
        results = []
        for game in self.games:
            results.append(game.play())
        return results

def main():
    import sys
    solver = JosephusSolver()
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue
        n,m = map(int, line.split())
        if n == 0 and m == 0:
            break
        solver.add_game(n,m)
    results = solver.solve_all()
    for r in results:
        print(r)

if __name__ == "__main__":
    main()