class RoomNumberConverter:
    """Converter between old and new hospital room numbers, excluding forbidden digits."""
    def __init__(self, forbidden_digits):
        self.forbidden_digits = set(str(d) for d in forbidden_digits)
        self.allowed_digits = [str(d) for d in range(10) if str(d) not in self.forbidden_digits]
        # Precompute mapping for digit to index in allowed digits
        self.allowed_digit_to_index = {d: i for i, d in enumerate(self.allowed_digits)}
        self.base = len(self.allowed_digits)

    def old_to_new(self, old_number: int) -> int:
        """
        Converts old room number to new room number by considering the new numbering system.
        The new numbering system excludes the forbidden digits.
        This corresponds mathematically to interpreting old_number in base 10,
        then mapping it to a number in a base that excludes forbidden digits.
        """
        # Convert old_number-1 to zero-based index for new numbering system
        # Because numbering starts at 1, index is old_number-1
        zero_based_index = old_number - 1
        # Convert zero_based_index from base 10 integer to the new numbering system representation
        digits = []
        while zero_based_index >= 0:
            digits.append(zero_based_index % self.base)
            zero_based_index = (zero_based_index // self.base) - 1
        # Reverse digits to most significant first
        digits.reverse()
        # Convert digits indices to actual digit values and join
        new_room_num_str = ''.join(self.allowed_digits[d] for d in digits)
        return int(new_room_num_str)


class InputProcessor:
    """Handles input reading and output writing according to problem constraints."""
    def __init__(self, converter):
        self.converter = converter

    def process(self):
        import sys
        for line in sys.stdin:
            line = line.strip()
            if line == '0':
                break
            old_number = int(line)
            new_number = self.converter.old_to_new(old_number)
            print(new_number)


class HospitalRoomNumberSystem:
    """Facade class to orchestrate room number translation tasks"""
    def __init__(self):
        # We exclude forbidden digits '4' and '6' as per the problem statement
        self.converter = RoomNumberConverter(forbidden_digits=[4, 6])
        self.processor = InputProcessor(self.converter)

    def run(self):
        self.processor.process()


if __name__ == "__main__":
    HospitalRoomNumberSystem().run()