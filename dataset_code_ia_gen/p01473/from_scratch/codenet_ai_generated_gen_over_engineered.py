from collections import Counter
from math import factorial
from functools import lru_cache
from typing import Dict, Tuple

class PalindromicAnagramCounter:
    """
    A highly abstracted class to count the number of palindromic anagrams of a given string.
    This class anticipates future extensions such as multi-lingual support, different palindrome
    definitions, or partial palindrome matching.
    """

    def __init__(self, input_string: str):
        self.original_string = input_string
        self.char_counter = Counter(input_string)
        self.length = len(input_string)
        self.alphabet = tuple(sorted(self.char_counter.keys()))
    
    def _factorial_cache(self):
        # For memoizing factorial calls up to length
        cache = [1] * (self.length + 1)
        for i in range(2, self.length + 1):
            cache[i] = cache[i-1] * i
        return cache
    
    def _count_half_anagrams(self, half_counts: Tuple[int, ...], fact_cache) -> int:
        """
        Compute the number of distinct anagrams given counts of half the palindrome part.
        half_counts is a tuple of counts of each character for half the string.
        """
        total_half = sum(half_counts)
        numerator = fact_cache[total_half]
        denominator = 1
        for count in half_counts:
            denominator *= fact_cache[count]
        return numerator // denominator
    
    def _can_form_palindrome(self) -> Tuple[bool, int]:
        """
        Determine if palindrome formation is possible.
        Return (True, odd_char_index) if possible,
        where odd_char_index = index in alphabet of the character with odd count or -1 if none.
        """
        odd_count = 0
        odd_char_index = -1
        for idx, ch in enumerate(self.alphabet):
            if self.char_counter[ch] % 2 != 0:
                odd_count += 1
                odd_char_index = idx
                if odd_count > 1:
                    return False, -1
        return True, odd_char_index
    
    def count_palindromic_anagrams(self) -> int:
        allowed, odd_char_index = self._can_form_palindrome()
        if not allowed:
            return 0
        
        half_counts = []
        for ch in self.alphabet:
            half_counts.append(self.char_counter[ch] // 2)

        fact_cache = self._factorial_cache()
        
        return self._count_half_anagrams(tuple(half_counts), fact_cache)


def main():
    import sys
    input_string = sys.stdin.readline().strip()
    counter = PalindromicAnagramCounter(input_string)
    print(counter.count_palindromic_anagrams())

if __name__ == "__main__":
    main()