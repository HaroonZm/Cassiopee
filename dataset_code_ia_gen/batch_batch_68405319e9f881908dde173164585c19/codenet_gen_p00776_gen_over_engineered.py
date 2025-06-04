from typing import List, Iterator


class EncryptionRules:
    """
    Encapsulate the encryption and decryption logic.
    The encryption: first 'b'→'a', first 'c'→'b', ..., first 'z'→'y'.
    For decryption candidates, we reverse this step.
    """

    def __init__(self):
        # Map from encrypted char back to possible original chars that could have caused it
        # encrypted char 'a' could come from original 'a' or original 'b' (because first 'b'->'a')
        # encrypted char 'b' could come from original 'b' (unchanged) or original 'c' (first 'c'->'b'), etc.
        self.char_to_originals = self._build_reverse_mapping()

    def _build_reverse_mapping(self) -> dict[str, List[str]]:
        # For each encrypted char, list all possible original chars that can be mapped to it.
        mapping = {chr(c): [chr(c)] for c in range(ord('a'), ord('z') + 1)}
        # Because encryption maps first 'b'->'a', first 'c'->'b', ..., first 'z'->'y',
        # each encrypted character (except 'z') may come from itself or from next character
        for c in range(ord('a') + 1, ord('z') + 1):
            encrypted_char = chr(c - 1)
            original_char = chr(c)
            mapping[encrypted_char].append(original_char)
        return mapping

    def candidates_for_char(self, enc_char: str) -> List[str]:
        # Return possible original chars that could have produced enc_char after encryption
        return sorted(self.char_to_originals.get(enc_char, []))


class CandidateGenerator:
    """
    Generate all candidates of the original string before encryption for a given encrypted string.
    """

    def __init__(self, rules: EncryptionRules, encrypted: str):
        self.rules = rules
        self.encrypted = encrypted
        self.length = len(encrypted)

    def generate(self) -> Iterator[str]:
        # Use DFS recursion to yield all candidates in lex order
        def dfs(pos: int, path: List[str]):
            if pos == self.length:
                yield "".join(path)
                return
            possibilities = self.rules.candidates_for_char(self.encrypted[pos])
            for c in possibilities:
                path.append(c)
                yield from dfs(pos + 1, path)
                path.pop()

        return dfs(0, [])


class ResultFormatter:
    """
    Format the results according to the problem's output specification.
    """

    MAX_PRINT = 10
    EDGE_PRINT = 5  # first 5 and last 5 when > 10

    @classmethod
    def format_and_print(cls, candidates: List[str]):
        n = len(candidates)
        print(n)
        if n == 0:
            return
        candidates.sort()
        if n <= cls.MAX_PRINT:
            for c in candidates:
                print(c)
        else:
            # print first 5 then last 5 candidates
            first_five = candidates[:cls.EDGE_PRINT]
            last_five = candidates[-cls.EDGE_PRINT:]
            for c in first_five:
                print(c)
            for c in last_five:
                print(c)


class EncryptionSystemDecoder:
    """
    Controller class to encapsulate reading inputs, decoding and printing.
    """

    def __init__(self):
        self.rules = EncryptionRules()

    def decode(self, encrypted: str) -> List[str]:
        generator = CandidateGenerator(self.rules, encrypted)
        # Collect all candidates (could be large)
        return list(generator.generate())

    def process(self):
        while True:
            line = input().strip()
            if line == "#":
                break
            candidates = self.decode(line)
            ResultFormatter.format_and_print(candidates)


if __name__ == "__main__":
    EncryptionSystemDecoder().process()