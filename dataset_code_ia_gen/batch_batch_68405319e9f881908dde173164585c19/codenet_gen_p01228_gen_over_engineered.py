from typing import List, Optional, Tuple
import sys

class HexMusicSymbol:
    """
    Représente un symbole musical sous forme hexadécimale à deux caractères,
    correspondant à une combinaison binaire des 8 sons possibles.
    """
    __slots__ = ('value',)

    VALID_HEX_CHARS = '0123456789ABCDEF'

    def __init__(self, hex_str: str):
        if len(hex_str) != 2:
            raise ValueError(f"HexMusicSymbol requires 2 chars, got '{hex_str}'")
        if any(c not in self.VALID_HEX_CHARS for c in hex_str):
            raise ValueError(f"Invalid hex chars in '{hex_str}'")
        self.value = int(hex_str, 16)

    @classmethod
    def from_int(cls, value: int) -> 'HexMusicSymbol':
        if not (0 <= value <= 0xFF):
            raise ValueError(f"Value {value} out of byte range")
        hex_str = f"{value:02X}"
        return cls(hex_str)

    def __int__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return f"{self.value:02X}"

    def is_old_product_valid(self) -> bool:
        """
        Vérifie si le symbole correspond à un son jouable par l'ancien produit,
        c’est-à-dire aucun son (00) ou exactement un seul bit à 1.
        """
        # uniquement les combinaisons possibles par un ancien produit
        old_valid_values = {
            0x00, 0x01, 0x02, 0x04, 0x08,
            0x10, 0x20, 0x40, 0x80
        }
        return self.value in old_valid_values

class RhythmPattern:
    """
    Une séquence de HexMusicSymbol représentant un pattern rythmique.
    """
    def __init__(self, symbols: List[HexMusicSymbol]):
        self.symbols = symbols

    @classmethod
    def from_string(cls, pattern_str: str) -> 'RhythmPattern':
        if len(pattern_str) % 2 != 0:
            raise ValueError("Pattern string length must be even")
        symbols = []
        for i in range(0, len(pattern_str), 2):
            sym = HexMusicSymbol(pattern_str[i:i+2].upper())
            symbols.append(sym)
        return cls(symbols)

    def length(self) -> int:
        return len(self.symbols)

    def __str__(self) -> str:
        return ''.join(str(sym) for sym in self.symbols)

    def validate_old_product(self) -> bool:
        """
        Valide si tous les symboles de ce pattern conviennent aux anciennes machines.
        """
        return all(sym.is_old_product_valid() for sym in self.symbols)

    def is_silent(self) -> bool:
        """
        Vérifie si ce pattern joue toujours '00' (silence)
        """
        return all(int(sym) == 0 for sym in self.symbols)

class RhythmPatternMerger:
    """
    Fusionne plusieurs rythmes d’anciennes machines en un seul pattern
    pour une machine nouvelle capacité (jusqu'à 8 sons simultanés).
    """

    def __init__(self, old_patterns: List[RhythmPattern]):
        self.old_patterns = old_patterns

    def lcm(self, a: int, b: int) -> int:
        import math
        return a * b // math.gcd(a, b)

    def full_lcm(self, numbers: List[int]) -> int:
        from functools import reduce
        import math
        return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)

    def expand_pattern(self, pattern: RhythmPattern, length: int) -> List[int]:
        """
        Étend ou rééchantillonne le pattern à une longueur donnée (plus grande).
        Le pattern initial est supposé être un cycle répétitif sur la mesure.
        """
        original_len = pattern.length()
        factor = length // original_len
        # Pour les vieux patterns, on peut répéter simplement chaque symbole factor fois
        expanded = []
        for sym in pattern.symbols:
            expanded.extend([int(sym)] * factor)
        return expanded

    def merge(self) -> Optional[str]:
        """
        Fusionne tous les anciens patterns selon l’énoncé.
        Retourne la chaîne hexadécimale fusionnée ou None si trop volumineux.
        """
        lengths = [p.length() for p in self.old_patterns]
        l = self.full_lcm(lengths)

        # Étendre tous les patterns à la longueur l
        expanded_patterns = [self.expand_pattern(p, l) for p in self.old_patterns]

        # Fusionner les sons par position temporelle : bitwise OR
        merged_pattern = []
        for i in range(l):
            combined = 0
            for pat_sounds in expanded_patterns:
                combined |= pat_sounds[i]
            merged_pattern.append(combined)

        # Simplifier la représentation en cherchant le motif minimal cyclique
        # pour produire la sortie la plus courte possible
        minimal_pattern = self.minimal_cyclic_pattern(merged_pattern)

        if len(minimal_pattern) * 2 > 2048:
            return None

        # Construction de la chaîne hexadécimale majuscule
        result = ''.join(f"{val:02X}" for val in minimal_pattern)
        return result

    def minimal_cyclic_pattern(self, pattern: List[int]) -> List[int]:
        """
        Trouver le motif cyclique minimal qui, répété, forme pattern.
        Recherche du plus petit k divisant len(pattern) tel que pattern est k répétitions du motif.
        """
        n = len(pattern)
        for sublen in range(1, n + 1):
            if n % sublen != 0:
                continue
            motif = pattern[:sublen]
            if motif * (n // sublen) == pattern:
                return motif
        return pattern  # fallback

class InputReader:
    """
    Flux de lecture avancé depuis stdin, pour modularité et tests potentielles.
    """

    def __init__(self):
        self.lines = sys.stdin.read().splitlines()
        self.pos = 0

    def read_int(self) -> int:
        if self.pos >= len(self.lines):
            raise EOFError("No more input lines")
        val = int(self.lines[self.pos])
        self.pos += 1
        return val

    def read_pattern(self) -> RhythmPattern:
        if self.pos >= len(self.lines):
            raise EOFError("No more input lines")
        line = self.lines[self.pos].strip()
        self.pos += 1
        return RhythmPattern.from_string(line)

def main():
    ir = InputReader()
    dataset_count = ir.read_int()
    outputs = []

    for _ in range(dataset_count):
        N = ir.read_int()
        old_patterns = []
        for _ in range(N):
            pattern = ir.read_pattern()
            if not pattern.validate_old_product():
                # Étant donné que l'énoncé garantit la validité, ceci est une sécurité
                raise ValueError("Invalid old product pattern detected")
            old_patterns.append(pattern)

        merger = RhythmPatternMerger(old_patterns)
        merged = merger.merge()
        if merged is None:
            outputs.append("Too complex.")
        else:
            outputs.append(merged)

    print('\n'.join(outputs))


if __name__ == "__main__":
    main()