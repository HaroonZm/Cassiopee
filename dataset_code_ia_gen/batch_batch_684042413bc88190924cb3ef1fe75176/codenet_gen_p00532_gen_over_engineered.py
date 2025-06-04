from typing import List, Dict, Tuple

class Friend:
    def __init__(self, friend_id: int):
        self.id = friend_id
        self.total_score = 0

    def add_score(self, score: int) -> None:
        self.total_score += score

    def __repr__(self):
        return f"Friend(id={self.id}, total_score={self.total_score})"

class GameRound:
    def __init__(self, target_id: int, guesses: List[int]):
        self.target_id = target_id
        self.guesses = guesses  # index==friend_id-1 -> guess friend_id

    def compute_scores(self, friends: Dict[int, Friend]) -> None:
        correct_guesses = 0
        incorrect_count = 0
        for idx, guess in enumerate(self.guesses, start=1):
            friend = friends[idx]
            if idx == self.target_id:
                # Target guesses self - always correct
                correct_guesses += 1
            elif guess == self.target_id:
                correct_guesses += 1
            else:
                incorrect_count += 1

        # Points to non-target friends who guessed correctly (1 each)
        for idx, guess in enumerate(self.guesses, start=1):
            friend = friends[idx]
            if idx == self.target_id:
                # Target always scores 1 + bonus for incorrect others
                friend.add_score(1 + incorrect_count)
            else:
                if guess == self.target_id:
                    friend.add_score(1)

class ChristmasParty:
    def __init__(self, friend_count: int, game_count: int, targets: List[int], guess_matrix: List[List[int]]):
        self.friend_count = friend_count
        self.game_count = game_count
        self.targets = targets
        self.guess_matrix = guess_matrix
        self.friends: Dict[int, Friend] = self._init_friends()
        self.rounds: List[GameRound] = self._init_rounds()

    def _init_friends(self) -> Dict[int, Friend]:
        return {i: Friend(i) for i in range(1, self.friend_count + 1)}

    def _init_rounds(self) -> List[GameRound]:
        rounds = []
        for i in range(self.game_count):
            rounds.append(GameRound(self.targets[i], self.guess_matrix[i]))
        return rounds

    def conduct_all_rounds(self) -> None:
        for rnd in self.rounds:
            rnd.compute_scores(self.friends)

    def get_total_scores(self) -> List[int]:
        return [self.friends[i].total_score for i in range(1, self.friend_count + 1)]

class InputHandler:
    @staticmethod
    def parse_input() -> ChristmasParty:
        N = int(input())
        M = int(input())
        targets = list(map(int, input().split()))
        guess_matrix = [list(map(int, input().split())) for _ in range(M)]
        return ChristmasParty(N, M, targets, guess_matrix)

class OutputHandler:
    @staticmethod
    def print_scores(scores: List[int]) -> None:
        for score in scores:
            print(score)

def main():
    party = InputHandler.parse_input()
    party.conduct_all_rounds()
    scores = party.get_total_scores()
    OutputHandler.print_scores(scores)

if __name__ == "__main__":
    main()