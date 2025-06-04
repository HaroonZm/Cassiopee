class CardNumber:
    def __init__(self, value: int):
        self.value = value
        self.str_value = str(value)
        self.length = len(self.str_value)

    def __repr__(self):
        return f"CardNumber(value={self.value})"


class PermutationSumCalculator:
    MOD = 1_000_000_007

    def __init__(self, cards: list[CardNumber]):
        self.cards = cards
        self.n = len(cards)
        self.factorials = self._precompute_factorials(self.n)
        self.power_of_ten = self._precompute_powers_of_ten(max(card.length for card in cards)*self.n)
        self.dp = {}  # memoization for permutations sum calculations

    @staticmethod
    def _precompute_factorials(n: int) -> list[int]:
        fact = [1] * (n+1)
        for i in range(2, n+1):
            fact[i] = (fact[i-1] * i) % PermutationSumCalculator.MOD
        return fact

    @staticmethod
    def _precompute_powers_of_ten(max_power: int) -> list[int]:
        pw = [1]*(max_power+1)
        for i in range(1, max_power+1):
            pw[i] = (pw[i-1] * 10) % PermutationSumCalculator.MOD
        return pw

    def _count_bit_length_sum(self, subset_mask: int) -> int:
        # Sum of lengths of cards in the subset
        length_sum = 0
        for i in range(self.n):
            if (subset_mask >> i) & 1:
                length_sum += self.cards[i].length
        return length_sum

    def _compute_subset_sum(self, subset_mask: int) -> int:
        # Returns total sum of all permutations of subset cards considering duplicates
        # but digits do not start with zero card.

        if subset_mask == 0:
            return 0

        if subset_mask in self.dp:
            return self.dp[subset_mask]

        total_sum = 0
        total_card_count = bin(subset_mask).count('1')

        # Iterate over valid first cards in permutations (leading zero check)
        for i in range(self.n):
            if not (subset_mask & (1 << i)):
                continue
            card = self.cards[i]
            # Leading zero check: do not allow cards with 0 digit leading
            if card.value == 0 and total_card_count > 1:
                # You cannot start with 0 if length > 1, skip
                continue

            # Remaining subset without chosen card i
            rest_mask = subset_mask ^ (1 << i)
            length_rest = self._count_bit_length_sum(rest_mask)

            # Count of permutations of remaining cards
            rest_count = self.factorials[bin(rest_mask).count('1')]

            # Sum of permutations of the rest subset
            rest_sum = self._compute_subset_sum(rest_mask)

            # Compose sums:
            # (card * 10^{len_rest} + rest_permutation)
            # multiplied by permutations count for rest subset,
            # add rest_sum itself.

            card_contrib = (card.value * self.power_of_ten[length_rest]) % self.MOD
            subtotal = (card_contrib * rest_count) % self.MOD
            subtotal = (subtotal + rest_sum) % self.MOD

            total_sum = (total_sum + subtotal) % self.MOD

        self.dp[subset_mask] = total_sum
        return total_sum

    def compute_total_sum(self) -> int:
        # Summing over all non-empty subsets
        total = 0
        for subset_mask in range(1, 1 << self.n):
            total = (total + self._compute_subset_sum(subset_mask)) % self.MOD
        return total


class InputProcessor:
    def __init__(self):
        self.n = 0
        self.cards = []

    def read_input(self):
        import sys
        input = sys.stdin.readline
        self.n = int(input())
        temp_cards = []
        for _ in range(self.n):
            a = int(input())
            temp_cards.append(a)
        self.cards = [CardNumber(value) for value in temp_cards]


def main():
    processor = InputProcessor()
    processor.read_input()
    calculator = PermutationSumCalculator(processor.cards)
    result = calculator.compute_total_sum()
    print(result)


if __name__ == "__main__":
    main()