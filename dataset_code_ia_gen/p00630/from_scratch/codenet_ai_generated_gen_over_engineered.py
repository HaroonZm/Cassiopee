from abc import ABC, abstractmethod
import sys
import re

class CaseConverter(ABC):
    """Interface for case conversion strategies."""
    @abstractmethod
    def to_words(self, identifier: str) -> list[str]:
        """Parse an identifier into a list of words."""
        pass

    @abstractmethod
    def from_words(self, words: list[str]) -> str:
        """Combine words into an identifier following this strategy."""
        pass

    def convert(self, identifier: str) -> str:
        """Convert identifier from unknown style to this strategy."""
        words = self.to_words(identifier)
        return self.from_words(words)

class UpperCamelCaseConverter(CaseConverter):
    """Upper CamelCase: Each word starts uppercase, concatenated."""
    def to_words(self, identifier: str) -> list[str]:
        if '_' in identifier:
            # underscore separated, just split, all lower assumed
            return identifier.lower().split('_')
        else:
            # Mixed case: split before each uppercase letter, preserving acronyms
            parts = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', identifier)
            return [word.lower() for word in parts]

    def from_words(self, words: list[str]) -> str:
        # Capitalize first letter of each word
        return ''.join(word.capitalize() for word in words)

class LowerCamelCaseConverter(CaseConverter):
    """Lower CamelCase: first word lowercase, rest capitalized."""
    def to_words(self, identifier: str) -> list[str]:
        if '_' in identifier:
            # underscore separated
            return identifier.lower().split('_')
        else:
            # Mixed case split same as UpperCamelCase
            parts = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', identifier)
            return [word.lower() for word in parts]

    def from_words(self, words: list[str]) -> str:
        if not words:
            return ''
        first = words[0].lower()
        rest = [word.capitalize() for word in words[1:]]
        return first + ''.join(rest)

class UnderscoreConverter(CaseConverter):
    """Underscore: all lowercase words joined by '_'."""
    def to_words(self, identifier: str) -> list[str]:
        if '_' in identifier:
            # underscore separated: direct split
            return identifier.lower().split('_')
        else:
            # Mixed case split same as others
            parts = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', identifier)
            return [word.lower() for word in parts]

    def from_words(self, words: list[str]) -> str:
        return '_'.join(words)

class IdentifierNormalizer:
    """Facade to normalize identifier to specified naming convention."""

    _converters = {
        'U': UpperCamelCaseConverter(),
        'L': LowerCamelCaseConverter(),
        'D': UnderscoreConverter(),
    }

    def __init__(self, target_type: str):
        if target_type not in self._converters:
            raise ValueError(f"Unsupported target type: {target_type}")
        self.converter = self._converters[target_type]

    def normalize(self, identifier: str) -> str:
        """Convert given identifier to target naming convention."""
        # Input identifier is guaranteed to be one of the three styles,
        # but unknown which. We exploit converter.to_words to parse.
        return self.converter.convert(identifier)

def main():
    normalizers_cache = {
        'U': IdentifierNormalizer('U'),
        'L': IdentifierNormalizer('L'),
        'D': IdentifierNormalizer('D'),
    }
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if line.endswith(' X'):
            # EndOfInput signal: stop processing
            break
        try:
            identifier, target_type = line.rsplit(' ', 1)
        except ValueError:
            continue  # malformed line, ignore

        if target_type not in normalizers_cache:
            continue  # invalid type

        normalizer = normalizers_cache[target_type]
        result = normalizer.normalize(identifier)
        print(result)

if __name__ == '__main__':
    main()