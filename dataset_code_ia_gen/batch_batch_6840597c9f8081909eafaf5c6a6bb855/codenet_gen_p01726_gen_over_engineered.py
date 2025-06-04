class AbstractStringMatcher:
    """
    Interface for string matchers which define a method to count substrings matching some condition relative to a pattern.
    """
    def count_matching_substrings(self, text: str, pattern: str) -> int:
        raise NotImplementedError()

class OneCharDifferenceMatcher(AbstractStringMatcher):
    """
    Counts substrings in text that differ from pattern by exactly one character.
    """

    def __init__(self):
        # Precompute function map etc. could be extended for different criteria
        self.match_criteria = self._one_char_diff

    def count_matching_substrings(self, text: str, pattern: str) -> int:
        """
        Count the substrings of text of length len(pattern) which differ from pattern by exactly one character.
        """
        text_length = len(text)
        pattern_length = len(pattern)
        count = 0

        # For extensibility, let's abstract the sliding over substrings with an iterator
        for start_index in self._substring_indices(text_length, pattern_length):
            substring = text[start_index:start_index+pattern_length]
            if self.match_criteria(substring, pattern):
                count += 1

        return count

    def _substring_indices(self, text_length: int, pattern_length: int):
        """
        Generator yielding all valid start indices for substrings in text of length pattern_length.
        """
        for i in range(text_length - pattern_length + 1):
            yield i

    def _one_char_diff(self, s1: str, s2: str) -> bool:
        """
        Check if strings s1 and s2 differ by exactly one character.
        """
        diff_count = 0

        # Potential optimization if we anticipate very long strings and early breaks
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff_count += 1
                if diff_count > 1:
                    return False

        return diff_count == 1

class Solution:
    """
    Orchestration class to encapsulate input processing and solution output.
    """

    def __init__(self, matcher: AbstractStringMatcher):
        self.matcher = matcher

    def run(self):
        S = input().strip()
        T_prime = input().strip()

        result = self.matcher.count_matching_substrings(S, T_prime)
        print(result)

if __name__ == "__main__":
    # Dependency injection of matcher for possible future extensions
    matcher = OneCharDifferenceMatcher()
    solution = Solution(matcher)
    solution.run()