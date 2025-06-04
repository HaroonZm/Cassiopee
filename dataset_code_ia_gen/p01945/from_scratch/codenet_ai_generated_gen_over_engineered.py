class BalancedParentheses:
    def __init__(self, s: str):
        self.original = s
        self.star_index = self._find_star_index()
        self.cleaned = self._remove_star()
        self.length = len(self.cleaned)
        self.pair_map = self._match_parentheses()

    def _find_star_index(self):
        # Locate the star symbol index
        for i, ch in enumerate(self.original):
            if ch == '*':
                return i
        return -1  # Should never happen as problem guarantees one star

    def _remove_star(self):
        # Remove star to get a balanced parentheses string for validation/matching
        return self.original.replace('*', '')

    def _match_parentheses(self):
        # Compute matching pairs of parentheses in the cleaned string
        stack = []
        pairs = {}
        for i, ch in enumerate(self.cleaned):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    open_pos = stack.pop()
                    pairs[open_pos] = i
                    pairs[i] = open_pos
        return pairs

    def count_surrounding_pairs(self):
        # Count how many pairs of parentheses surround the star
        # star may be at position star_index; need to map this to cleaned indices after star removal
        pos = self.star_index
        # The star is not in cleaned string, so positions after star are shifted by -1
        # We create a map from original to cleaned indices for all '(' and ')' characters
        orig_to_clean = {}
        ci = 0
        for oi, ch in enumerate(self.original):
            if ch != '*':
                orig_to_clean[oi] = ci
                ci += 1

        if pos not in orig_to_clean:
            # Star position not in cleaned string, so we consider pairs around position in original string
            # We infer star's relative position between cleaned indices
            # Star is between orig_to_clean[pos-1] and orig_to_clean[pos+1] or at ends
            # We'll use the closest indices; if no neighbor parentheses, then no surrounding pairs
            left_index = None
            for i in range(pos - 1, -1, -1):
                if i in orig_to_clean:
                    left_index = orig_to_clean[i]
                    break
            right_index = None
            for i in range(pos + 1, len(self.original)):
                if i in orig_to_clean:
                    right_index = orig_to_clean[i]
                    break
            # Count how many pairs contain the segment between left_index and right_index
            # Since the star acts like a position between characters, only pairs enclosing it count
            count = 0
            for open_pos in self.pair_map:
                close_pos = self.pair_map[open_pos]
                if close_pos < open_pos:
                    open_pos, close_pos = close_pos, open_pos
                # Does the pair (open_pos, close_pos) enclose the star?
                if (left_index is None or open_pos <= left_index) and (right_index is None or close_pos >= right_index):
                    count += 1
            # Each pair counted twice in pair_map (once for open and once for close), so halving
            # To get unique pairs, we filter open_paren only
            unique_pairs = set()
            for k, v in self.pair_map.items():
                if k < v:
                    unique_pairs.add((k, v))
            total = 0
            for o, c in unique_pairs:
                if (left_index is None or o <= left_index) and (right_index is None or c >= right_index):
                    total += 1
            return total

        star_clean_idx = orig_to_clean[pos]
        # Count pairs of parentheses that enclose star_clean_idx exclusively,
        # i.e. pairs that satisfy open_pos < star_clean_idx < close_pos
        count = 0
        counted_pairs = set()
        for open_pos in self.pair_map:
            if open_pos < self.pair_map[open_pos]:
                close_pos = self.pair_map[open_pos]
                if open_pos < star_clean_idx < close_pos:
                    counted_pairs.add((open_pos, close_pos))
        return len(counted_pairs)


def main():
    s = input()
    bp = BalancedParentheses(s)
    print(bp.count_surrounding_pairs())

if __name__ == "__main__":
    main()