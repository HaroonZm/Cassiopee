from typing import List, Tuple
from abc import ABC, abstractmethod


class CryslumState(ABC):
    """Abstraction for the state of a single Cryslum (level 2 or level 1 or none)."""
    
    @abstractmethod
    def satisfaction_per_unit(self, song_index: int) -> int:
        pass


class Level2State(CryslumState):
    def __init__(self, satisfaction_table: List[Tuple[int, int, int]]):
        self.satisfaction_table = satisfaction_table

    def satisfaction_per_unit(self, song_index: int) -> int:
        return self.satisfaction_table[song_index][0]


class Level1State(CryslumState):
    def __init__(self, satisfaction_table: List[Tuple[int, int, int]]):
        self.satisfaction_table = satisfaction_table

    def satisfaction_per_unit(self, song_index: int) -> int:
        return self.satisfaction_table[song_index][1]


class NoCryslumState(CryslumState):
    def __init__(self, satisfaction_table: List[Tuple[int, int, int]]):
        self.satisfaction_table = satisfaction_table

    def satisfaction_per_unit(self, song_index: int) -> int:
        # When no cryslum is used, a fixed satisfaction c_i is added once per song.
        # Multiplying by zero here since no per unit, handled specially.
        return self.satisfaction_table[song_index][2]


class CryslumUsage:
    """
    Represents an assignment of cryslum use count for a song:
    number of level 2 cryslums used, number of level 1 cryslums used, or zero cryslums used.
    """
    MAX_PER_SONG = 8  # max cryslums can be shaken at the same time
    
    def __init__(self, level2_count: int, level1_count: int):
        self.level2_count = level2_count
        self.level1_count = level1_count
        self.total = self.level2_count + self.level1_count
    
    @classmethod
    def all_possible_usages(cls):
        """
        Yield all possible usages (level2_count, level1_count) such that total <= 8.
        Also include the option (0,0) meaning no cryslum usage.
        """
        for total in range(cls.MAX_PER_SONG + 1):
            for level2 in range(total + 1):
                level1 = total - level2
                yield cls(level2, level1)

    def consume_cry_slums(self, available: int) -> bool:
        """Check if this usage can be applied given available cryslums."""
        return self.total <= available


class Setlist:
    """
    Manages the songs and satisfaction table,
    and provides satisfaction lookup for usage schemes.
    """
    def __init__(self, n: int, satisfaction_table: List[Tuple[int, int, int]]):
        self.n = n
        self.satisfaction_table = satisfaction_table

    def satisfaction_for_usage(self, song_index: int, usage: CryslumUsage) -> int:
        # If no cryslums used, satisfaction is c_i
        if usage.total == 0:
            return self.satisfaction_table[song_index][2]
        # Otherwise, sum level2 * a_i + level1 * b_i
        return usage.level2_count * self.satisfaction_table[song_index][0] + usage.level1_count * self.satisfaction_table[song_index][1]


class CryslumAllocator:
    """
    Allocates cryslums to songs to maximize total satisfaction,
    using a combinatorial DP approach.
    """
    def __init__(self, setlist: Setlist, total_cry_slums: int):
        self.setlist = setlist
        self.total_cry_slums = total_cry_slums
        self.n = setlist.n
        # DP cache: dp[song_index][cry_slums_left] = max satisfaction achievable from song_index onwards
        self.dp = [[None] * (total_cry_slums + 1) for _ in range(self.n + 1)]

    def maximize_satisfaction(self) -> int:
        return self._dfs(0, self.total_cry_slums)

    def _dfs(self, song_index: int, cry_slums_left: int) -> int:
        if song_index == self.n:
            return 0
        if self.dp[song_index][cry_slums_left] is not None:
            return self.dp[song_index][cry_slums_left]

        max_satis = -10**9  # sufficiently low number for min possible satisfaction
        # Try all possible usages for this song
        for usage in CryslumUsage.all_possible_usages():
            if usage.consume_cry_slums(cry_slums_left):
                current_satis = self.setlist.satisfaction_for_usage(song_index, usage)
                next_satis = self._dfs(song_index + 1, cry_slums_left - usage.total)
                total_satis = current_satis + next_satis
                if total_satis > max_satis:
                    max_satis = total_satis
        
        self.dp[song_index][cry_slums_left] = max_satis
        return max_satis


def read_input() -> Tuple[int, int, List[Tuple[int, int, int]]]:
    n, m = map(int, input().split())
    satisfaction_table = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        satisfaction_table.append((a, b, c))
    return n, m, satisfaction_table


def main():
    n, m, satisfaction_table = read_input()
    setlist = Setlist(n, satisfaction_table)
    allocator = CryslumAllocator(setlist, m)
    ans = allocator.maximize_satisfaction()
    print(ans)


if __name__ == "__main__":
    main()