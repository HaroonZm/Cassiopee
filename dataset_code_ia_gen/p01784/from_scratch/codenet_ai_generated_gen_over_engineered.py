class ParenthesesString:
    def __init__(self, raw_str: str):
        self.raw = raw_str
        self.min_prefix_balance = 0
        self.final_balance = 0
        self._analyze()

    def _analyze(self):
        balance = 0
        min_balance = 0
        for ch in self.raw:
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            if balance < min_balance:
                min_balance = balance
        self.min_prefix_balance = min_balance
        self.final_balance = balance

    def __repr__(self):
        return f"PS(min_prefix_balance={self.min_prefix_balance}, final_balance={self.final_balance}, raw='{self.raw}')"

class ParenthesesPermutationValidator:
    def __init__(self, strings):
        self.strings = [ParenthesesString(s) for s in strings]

    def can_form_valid_string(self) -> bool:
        # Divide strings into two groups:
        # Group A: final_balance >= 0 (they add or maintain open parens)
        # Group B: final_balance < 0 (they reduce open parens)
        group_a = [ps for ps in self.strings if ps.final_balance >= 0]
        group_b = [ps for ps in self.strings if ps.final_balance < 0]

        # Sort group_a to put the most restrictive (lowest min_prefix_balance) first
        # so that when concatenated from left to right we never get negative balance
        group_a.sort(key=lambda x: x.min_prefix_balance, reverse=True)

        # For group_b, we reverse their strings and swap '(' and ')' accordingly,
        # then analyze them similar to group_a, to ensure correctness of order when concatenating backwards.
        group_b_reversed = [self._reverse_and_swap(ps.raw) for ps in group_b]
        reversed_ps_list = [ParenthesesString(s) for s in group_b_reversed]
        reversed_ps_list.sort(key=lambda x: x.min_prefix_balance, reverse=True)

        # We'll simulate concatenation of group_a in order, then group_b in reverse order.
        balance = 0

        # Append group A
        for ps in group_a:
            if balance + ps.min_prefix_balance < 0:
                return False
            balance += ps.final_balance

        # Append group B (in reversed order of their reversed forms)
        for rps in reversed_ps_list:
            if balance + rps.min_prefix_balance < 0:
                return False
            balance += rps.final_balance

        return balance == 0

    @staticmethod
    def _reverse_and_swap(s: str) -> str:
        swapped = []
        for ch in reversed(s):
            if ch == '(':
                swapped.append(')')
            else:
                swapped.append('(')
        return ''.join(swapped)

class InputOutputHandler:
    def __init__(self):
        self.n = 0
        self.strings = []

    def read(self):
        self.n = int(input())
        self.strings = [input().strip() for _ in range(self.n)]

    def process(self):
        validator = ParenthesesPermutationValidator(self.strings)
        if validator.can_form_valid_string():
            print("Yes")
        else:
            print("No")

def main():
    ioh = InputOutputHandler()
    ioh.read()
    ioh.process()

if __name__ == "__main__":
    main()