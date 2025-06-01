class Fish:
    def __init__(self, name: str, base_points: int, bonus_threshold: int, bonus_points: int):
        self.name = name
        self.base_points = base_points
        self.bonus_threshold = bonus_threshold
        self.bonus_points = bonus_points

    def calculate_score(self, count: int) -> int:
        bonus_count = count // self.bonus_threshold if self.bonus_threshold > 0 else 0
        total_score = count * self.base_points + bonus_count * self.bonus_points
        return total_score

class Fisherman:
    def __init__(self, name: str, iwana_count: int, yamame_count: int):
        self.name = name
        self.iwana_count = iwana_count
        self.yamame_count = yamame_count

    def total_score(self, iwana: Fish, yamame: Fish) -> int:
        iwana_score = iwana.calculate_score(self.iwana_count)
        yamame_score = yamame.calculate_score(self.yamame_count)
        return iwana_score + yamame_score

class FishingCompetition:
    def __init__(self, fisher1: Fisherman, fisher2: Fisherman, iwana: Fish, yamame: Fish):
        self.fisher1 = fisher1
        self.fisher2 = fisher2
        self.iwana = iwana
        self.yamame = yamame

    def judge_winner(self) -> str:
        score1 = self.fisher1.total_score(self.iwana, self.yamame)
        score2 = self.fisher2.total_score(self.iwana, self.yamame)
        if score1 > score2:
            return self.fisher1.name
        elif score2 > score1:
            return self.fisher2.name
        else:
            return "even"

class InputReader:
    @staticmethod
    def read_ints() -> list[int]:
        return list(map(int, input().split()))

class Solution:
    def __init__(self):
        self.h1 = 0
        self.h2 = 0
        self.k1 = 0
        self.k2 = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

    def parse_input(self):
        self.h1, self.h2 = InputReader.read_ints()
        self.k1, self.k2 = InputReader.read_ints()
        self.a, self.b, self.c, self.d = InputReader.read_ints()

    def run(self):
        self.parse_input()
        iwana = Fish("iwana", self.a, 10, self.c)
        yamame = Fish("yamame", self.b, 20, self.d)
        hiroshi = Fisherman("hiroshi", self.h1, self.h2)
        kenjiro = Fisherman("kenjiro", self.k1, self.k2)
        competition = FishingCompetition(hiroshi, kenjiro, iwana, yamame)
        print(competition.judge_winner())

if __name__ == "__main__":
    Solution().run()