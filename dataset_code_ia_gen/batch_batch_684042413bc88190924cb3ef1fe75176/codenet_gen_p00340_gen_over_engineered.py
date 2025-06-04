class Stick:
    def __init__(self, length: int):
        self.length = length

    def __eq__(self, other):
        if not isinstance(other, Stick):
            return False
        return self.length == other.length

    def __hash__(self):
        return hash(self.length)

    def __repr__(self):
        return f"Stick(length={self.length})"


class RectangleValidator:
    def __init__(self, sticks):
        if len(sticks) != 4:
            raise ValueError("Exactly four sticks are required")
        self.sticks = sticks

    def _group_sticks_by_length(self):
        length_counts = {}
        for stick in self.sticks:
            length_counts[stick.length] = length_counts.get(stick.length, 0) + 1
        return length_counts

    def can_form_rectangle(self) -> bool:
        length_counts = self._group_sticks_by_length()
        # For a rectangle using four sticks without modification,
        # there must be either:
        # - Two pairs of equal lengths (including the case where all four are the same — square)
        counts = sorted(length_counts.values())
        if counts == [4]:
            return True  # square case
        if counts == [2, 2]:
            return True  # rectangle with pairs of equal lengths
        return False


class RectangleFactory:
    @staticmethod
    def create_sticks_from_input(input_line: str):
        lengths = list(map(int, input_line.strip().split()))
        return [Stick(length) for length in lengths]


def main():
    import sys
    input_line = sys.stdin.readline()
    sticks = RectangleFactory.create_sticks_from_input(input_line)
    validator = RectangleValidator(sticks)
    if validator.can_form_rectangle():
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()