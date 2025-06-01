class Participant:
    def __init__(self, id_):
        self.id = id_
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def total_score(self):
        return sum(self.scores)

    def __repr__(self):
        return f"Participant({self.id}, total_score={self.total_score()})"

class GameRound:
    def __init__(self, round_index, target_id, guesses):
        self.round_index = round_index
        self.target_id = target_id
        self.guesses = guesses  # dict participant_id -> guessed_id

    def compute_scores(self):
        scores = {}
        correct_count = 0
        for participant_id, guess in self.guesses.items():
            if guess == self.target_id:
                scores[participant_id] = 1
                correct_count += 1
            else:
                scores[participant_id] = 0
        # The target gets additional points equal to number of incorrect guesses
        incorrect_count = len(self.guesses) - correct_count
        scores[self.target_id] += incorrect_count
        return scores

class ChristmasParty:
    def __init__(self, num_participants, num_rounds, targets, all_guesses):
        self.num_participants = num_participants
        self.num_rounds = num_rounds
        self.participants = {i: Participant(i) for i in range(1, num_participants+1)}
        self.rounds = []
        for i in range(num_rounds):
            target_id = targets[i]
            guesses_for_round = {j+1: all_guesses[i][j] for j in range(num_participants)}
            self.rounds.append(GameRound(i+1, target_id, guesses_for_round))

    def play(self):
        for game_round in self.rounds:
            round_scores = game_round.compute_scores()
            for pid, sc in round_scores.items():
                self.participants[pid].add_score(sc)

    def print_total_scores(self):
        for pid in range(1, self.num_participants+1):
            print(self.participants[pid].total_score())

def parse_input():
    import sys
    input_stream = sys.stdin
    N = int(input_stream.readline().strip())
    M = int(input_stream.readline().strip())
    targets = list(map(int, input_stream.readline().split()))
    all_guesses = [list(map(int, input_stream.readline().split())) for _ in range(M)]
    return N, M, targets, all_guesses

def main():
    N, M, targets, all_guesses = parse_input()
    party = ChristmasParty(N, M, targets, all_guesses)
    party.play()
    party.print_total_scores()

if __name__ == "__main__":
    main()