from typing import List, Dict, Tuple, Optional, Iterator
import sys

class BaseConverter:
    _symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    _char_to_value: Dict[str, int] = {c: i for i, c in enumerate(_symbols)}

    @classmethod
    def to_decimal(cls, base: int, value: str) -> int:
        result = 0
        for ch in value:
            v = cls._char_to_value[ch]
            if v >= base:
                raise ValueError(f"Digit '{ch}' invalid for base {base}")
            result = result * base + v
        return result

class BinarySegmenter:
    """
    Segments binary strings obtained after removing all zeros from binary representation
    and splitting into contiguous '1' runs.
    """

    @staticmethod
    def segment(binary_str: str) -> List[int]:
        # binary_str consists only of '0' or '1'
        segments = []
        run_len = 0
        for ch in binary_str:
            if ch == '1':
                run_len += 1
            else:
                if run_len > 0:
                    segments.append(run_len)
                    run_len = 0
        if run_len > 0:
            segments.append(run_len)
        return segments

class NimGame:
    """
    Models the game described, with abstractions for steps and piles.
    """

    def __init__(self, piles: List[int]):
        self.piles = piles

    def step1_transform(self) -> None:
        """
        Remove all piles, convert each to binary, remove zeros, segment runs of ones,
        and set piles to concatenation of those segments.
        """
        new_piles = []
        for pile in self.piles:
            binary_repr = bin(pile)[2:]
            segments = BinarySegmenter.segment(binary_repr)
            new_piles.extend(segments)
        self.piles = new_piles

    def is_lost(self) -> bool:
        return len(self.piles) == 0

    def nim_sum(self) -> int:
        from functools import reduce
        from operator import ixor
        return reduce(ixor, self.piles, 0)

    def optimal_move(self) -> Tuple[int, int]:
        """
        Returns (pile index, amount to remove) that is optimal, or (-1, -1) if no move.
        """
        xor_sum = self.nim_sum()
        if xor_sum == 0:
            return (-1, -1)
        for i, pile in enumerate(self.piles):
            target = pile ^ xor_sum
            if target < pile:
                return (i, pile - target)
        return (-1, -1)

    def play_turn(self) -> Optional[bool]:
        """
        Conducts one full turn:
        Step1: transform piles
        Step2: if empty piles, current player loses => return False
        Step3: reduce one pile by x (optimal move)
        Returns True if current player has not lost; False if lost.
        """
        self.step1_transform()
        if self.is_lost():
            return False
        # choose optimal move (pile, remove amount)
        idx, rem = self.optimal_move()
        if idx == -1:
            # no move possible => lose
            return False
        self.piles[idx] -= rem
        if self.piles[idx] == 0:
            self.piles.pop(idx)
        return True

class GameRunner:
    """
    Runs the two-player alternating game using NimGame abstraction.
    """

    def __init__(self, piles: List[int]):
        self.game = NimGame(piles)
        self.current_player = 0  # 0 you, 1 friend A

    def run(self) -> str:
        """
        Runs until one player loses by empty set after Step1.
        Return "win" if player 0 wins, else "lose".
        """
        while True:
            alive = self.game.play_turn()
            if not alive:
                # current player lost
                return "lose" if self.current_player == 0 else "win"
            self.current_player = 1 - self.current_player

def parse_input() -> List[int]:
    input = sys.stdin.read().strip().split('\n')
    n = int(input[0])
    piles = []
    index = 1
    for _ in range(n):
        p_s, m_s = input[index].split()
        index += 1
        base = int(p_s)
        value = m_s.strip()
        decimal = BaseConverter.to_decimal(base, value)
        piles.append(decimal)
    return piles

def main():
    piles = parse_input()
    runner = GameRunner(piles)
    print(runner.run())

if __name__ == "__main__":
    main()