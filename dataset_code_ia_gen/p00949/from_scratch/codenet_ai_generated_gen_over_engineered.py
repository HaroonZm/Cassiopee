from typing import List, Dict, Tuple
from collections import Counter
from abc import ABC, abstractmethod


class StringSource(ABC):
    @abstractmethod
    def length(self) -> int:
        pass

    @abstractmethod
    def substring(self, start: int, length: int) -> str:
        pass

    @abstractmethod
    def char_frequency_vector(self, start: int, length: int) -> List[int]:
        pass


class ConcreteString(StringSource):
    def __init__(self, s: str):
        self._s = s
        self._prefix_freq = self._compute_prefix_frequency(s)

    def _compute_prefix_frequency(self, s: str) -> List[List[int]]:
        freq = [[0] * 26]
        for ch in s:
            curr = freq[-1].copy()
            curr[ord(ch) - ord('a')] += 1
            freq.append(curr)
        return freq

    def length(self) -> int:
        return len(self._s)

    def substring(self, start: int, length: int) -> str:
        return self._s[start:start+length]

    def char_frequency_vector(self, start: int, length: int) -> List[int]:
        end = start + length
        freq_start = self._prefix_freq[start]
        freq_end = self._prefix_freq[end]
        return [freq_end[i] - freq_start[i] for i in range(26)]


class SubstringComparator(ABC):
    @abstractmethod
    def are_anagrams(self, v1: List[int], v2: List[int]) -> bool:
        pass


class FrequencyVectorComparator(SubstringComparator):
    def are_anagrams(self, v1: List[int], v2: List[int]) -> bool:
        return v1 == v2


class HiddenAnagramSolver:
    def __init__(self, s1: StringSource, s2: StringSource, comparator: SubstringComparator):
        self.s1 = s1
        self.s2 = s2
        self.comparator = comparator

    def _can_find_hidden_anagram_of_length(self, length: int) -> bool:
        if length == 0:
            return True
        freq_map_s1 = {}
        for start1 in range(self.s1.length() - length + 1):
            freq_v = tuple(self.s1.char_frequency_vector(start1, length))
            freq_map_s1[freq_v] = True

        for start2 in range(self.s2.length() - length + 1):
            freq_v2 = self.s2.char_frequency_vector(start2, length)
            if tuple(freq_v2) in freq_map_s1:
                # Because comparison is by frequency tuples and hashing, comparator check is optional here;
                # but left for extensibility.
                if self.comparator.are_anagrams(freq_v2, list(freq_v2)):
                    return True
        return False

    def longest_hidden_anagram_length(self) -> int:
        low = 0
        high = min(self.s1.length(), self.s2.length())
        best = 0
        while low <= high:
            mid = (low + high) // 2
            if self._can_find_hidden_anagram_of_length(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        return best


def main():
    import sys

    s1_raw = sys.stdin.readline().strip()
    s2_raw = sys.stdin.readline().strip()

    s1 = ConcreteString(s1_raw)
    s2 = ConcreteString(s2_raw)

    comparator = FrequencyVectorComparator()

    solver = HiddenAnagramSolver(s1, s2, comparator)

    print(solver.longest_hidden_anagram_length())


if __name__ == "__main__":
    main()