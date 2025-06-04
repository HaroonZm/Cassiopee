class PalindromeBlockSet:
    def __init__(self, blocks: str):
        self.blocks = blocks
        self.char_frequency = self._count_char_frequency(blocks)

    @staticmethod
    def _count_char_frequency(s: str) -> dict:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        return freq

    def minimal_palindrome_cost(self) -> int:
        """
        Calcule le coût minimal pour rendre l'ensemble des blocs un palindrome après opérations.
        """
        frequency = self.char_frequency.copy()

        # Nombre de caractères dont la fréquence est impaire
        odd_count = sum(freq % 2 for freq in frequency.values())

        # Le nombre minimal d'opérations est le nombre de caractères impairs excessifs
        # dans la fréquence, car dans une palindrome au plus un caractère peut avoir une fréquence impaire.
        needed_cost = max(0, odd_count - 1)

        # Cette méthode reflète la stratégie:
        # - On peut corriger la fréquence impaire en faisant soit une suppression, soit un changement, soit une addition.
        # Comme chaque opération coûte 1, il suffit de corriger les freq impaires excédentaires.

        return needed_cost


# Abstraction pour la gestion d'opérations sur ensemble de blocs
class BlockOperations:
    def __init__(self, block_set: PalindromeBlockSet):
        self.block_set = block_set

    def compute_min_cost_to_palindrome(self) -> int:
        """
        Calcule la solution en utilisant l'ensemble des opérations offertes.
        Cette classe pourrait être étendue pour simuler explicitement des opérations, 
        mais ici nous utilisons la propriété mathématique pour la solution optimale.
        """
        return self.block_set.minimal_palindrome_cost()


# Usine pour créer des objets selon l'input (anticipation)
class PalindromeSolverFactory:
    @staticmethod
    def from_input_string(input_string: str) -> BlockOperations:
        block_set = PalindromeBlockSet(input_string.strip())
        return BlockOperations(block_set)


# Point d'entrée principal, encapsulé
def main():
    import sys
    input_string = sys.stdin.readline()
    solver = PalindromeSolverFactory.from_input_string(input_string)
    min_cost = solver.compute_min_cost_to_palindrome()
    print(min_cost)


if __name__ == "__main__":
    main()