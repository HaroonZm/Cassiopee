import sys
from typing import List, Optional, Callable, Dict, Tuple


class Alphabet:
    def __init__(self, letters: str = "abcdefghijklmnopqrstuvwxyz"):
        self._letters = letters
        self._letter_to_index: Dict[str, int] = {c: i for i, c in enumerate(letters)}
        self._index_to_letter: Dict[int, str] = {i: c for i, c in enumerate(letters)}
        self._modulus = len(letters)

    def letter_to_num(self, letter: str) -> Optional[int]:
        return self._letter_to_index.get(letter)

    def num_to_letter(self, num: int) -> str:
        return self._index_to_letter[num % self._modulus]

    def modulus(self) -> int:
        return self._modulus

    def is_in_alphabet(self, c: str) -> bool:
        return c in self._letter_to_index


class ModArithmetic:
    @staticmethod
    def egcd(a: int, b: int) -> Tuple[int, int, int]:
        if b == 0:
            return a, 1, 0
        else:
            g, x, y = ModArithmetic.egcd(b, a % b)
            return g, y, x - (a // b) * y

    @staticmethod
    def modinv(a: int, m: int) -> Optional[int]:
        g, x, _ = ModArithmetic.egcd(a, m)
        if g != 1:
            return None
        else:
            return x % m


class AffineCipher:
    def __init__(self, alpha: int, beta: int, alphabet: Alphabet):
        self.alpha = alpha
        self.beta = beta
        self.alphabet = alphabet
        self.modulus = alphabet.modulus()
        self.alpha_inv = ModArithmetic.modinv(alpha, self.modulus)
        if self.alpha_inv is None:
            raise ValueError(
                f"Alpha={alpha} is not coprime with modulus={self.modulus}, no inverse exists."
            )

    def decrypt_char(self, c: str) -> str:
        if not self.alphabet.is_in_alphabet(c):
            return c
        gamma = self.alphabet.letter_to_num(c)
        # Formula: F(\gamma) = (alpha*gamma + beta) mod 26
        # Decryption: gamma = alpha_inv * (F(\gamma) - beta) mod 26
        decrypted_num = (self.alpha_inv * (gamma - self.beta)) % self.modulus
        return self.alphabet.num_to_letter(decrypted_num)

    def decrypt_text(self, text: str) -> str:
        return "".join(self.decrypt_char(c) for c in text)


class DecryptionCandidate:
    def __init__(self, alpha: int, beta: int, decrypted_text: str):
        self.alpha = alpha
        self.beta = beta
        self.decrypted_text = decrypted_text


class AffineCipherCracker:
    def __init__(self, alphabet: Alphabet, keywords: List[str]):
        self.alphabet = alphabet
        self.keywords = keywords
        self.modulus = alphabet.modulus()
        self.valid_alphas = self._compute_valid_alphas()

    def _compute_valid_alphas(self) -> List[int]:
        valid = []
        for a in range(1, self.modulus):
            if self._gcd(a, self.modulus) == 1:
                valid.append(a)
        return valid

    @staticmethod
    def _gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def try_decryptions(self, cipher_text: str) -> Optional[DecryptionCandidate]:
        for alpha in self.valid_alphas:
            for beta in range(self.modulus):
                try:
                    cipher = AffineCipher(alpha, beta, self.alphabet)
                except ValueError:
                    continue
                decrypted = cipher.decrypt_text(cipher_text)
                if self._contains_keyword(decrypted):
                    return DecryptionCandidate(alpha, beta, decrypted)
        return None

    def _contains_keyword(self, text: str) -> bool:
        # Keywords are guaranteed to be in the original text
        # We consider words separated by spaces
        lowered = text.lower()
        return any(k in lowered for k in self.keywords)


class Solution:
    def __init__(self):
        self.alphabet = Alphabet()
        self.keywords = ["that", "this"]
        self.cracker = AffineCipherCracker(self.alphabet, self.keywords)

    def process(self, input_lines: List[str]) -> List[str]:
        n = int(input_lines[0].strip())
        results: List[str] = []
        for i in range(n):
            cipher_text = input_lines[i + 1]
            candidate = self.cracker.try_decryptions(cipher_text)
            if candidate is None:
                # fallback if no candidate found; should not happen by problem statement
                results.append(cipher_text)
            else:
                results.append(candidate.decrypted_text)
        return results


def main() -> None:
    input_lines = [line.rstrip("\n") for line in sys.stdin]
    solution = Solution()
    results = solution.process(input_lines)
    for res in results:
        print(res)


if __name__ == "__main__":
    main()