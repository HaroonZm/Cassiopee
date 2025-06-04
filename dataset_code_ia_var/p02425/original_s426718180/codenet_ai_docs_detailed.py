class Bit:
    """
    Bitset implementation using bit manipulation on integers.
    Supports various bitwise operations and queries similar to a fixed-size bitset (64 bits).
    """

    def __init__(self):
        """
        Initializes the Bit object with 0 (all bits cleared).
        """
        self.data = 0

    def process(self, op, arg):
        """
        Dispatches the operation based on the op code.
        
        Args:
            op (str): The operation code (as string, index into funcs tuple).
            arg (str or int): The operation argument (typically bit index or dummy value).

        Operations:
            0: test  - Check if the bit at position 'arg' is set (1 or 0).
            1: set   - Set the bit at position 'arg' to 1.
            2: clear - Clear the bit at position 'arg' to 0.
            3: flip  - Flip the bit at position 'arg'.
            4: all   - Print 1 if all 64 bits are set, else 0.
            5: any   - Print 1 if any bit is set, else 0.
            6: none  - Print 1 if none of the bits are set, else 0.
            7: count - Print the number of set bits.
            8: val   - Print the integer value of the current bitset.
        """
        funcs = (
            self.test,   # 0
            self.set,    # 1
            self.clear,  # 2
            self.flip,   # 3
            self.all,    # 4
            self.any,    # 5
            self.none,   # 6
            self.count,  # 7
            self.val     # 8
        )
        # Select and execute the corresponding function
        funcs[int(op)](arg)

    def test(self, arg):
        """
        Checks if the bit at position 'arg' is set.

        Args:
            arg (str or int): Bit index to check.

        Prints:
            1 if the bit is set, 0 otherwise.
        """
        pos = int(arg)
        # (self.data & (1 << pos)) is nonzero if the bit at 'pos' is set
        print(int(bool(self.data & (1 << pos))))

    def set(self, arg):
        """
        Sets (to 1) the bit at position 'arg'.

        Args:
            arg (str or int): Bit index to set.
        """
        pos = int(arg)
        self.data |= (1 << pos)

    def clear(self, arg):
        """
        Clears (to 0) the bit at position 'arg'.

        Args:
            arg (str or int): Bit index to clear.
        """
        pos = int(arg)
        self.data &= ~(1 << pos)

    def flip(self, arg):
        """
        Flips (toggles) the bit at position 'arg'.

        Args:
            arg (str or int): Bit index to flip.
        """
        pos = int(arg)
        self.data ^= (1 << pos)

    def all(self, arg):
        """
        Checks if all 64 bits are set to 1.

        Args:
            arg: Dummy value (not used).

        Prints:
            1 if all bits are set, 0 otherwise.
        """
        # (1 << 64) - 1 is a 64-bit mask of all 1s
        print(int(self.data == (1 << 64) - 1))

    def any(self, arg):
        """
        Checks if any bit is set to 1.

        Args:
            arg: Dummy value (not used).

        Prints:
            1 if any bit is set, 0 otherwise.
        """
        print(int(self.data != 0))

    def none(self, arg):
        """
        Checks if no bits are set (all are 0).

        Args:
            arg: Dummy value (not used).

        Prints:
            1 if none of the bits are set, 0 otherwise.
        """
        print(int(self.data == 0))

    def count(self, arg):
        """
        Counts the number of bits set to 1.

        Args:
            arg: Dummy value (not used).

        Prints:
            The number of bits set to 1.
        """
        print(bin(self.data).count('1'))

    def val(self, arg):
        """
        Prints the current value of the bitset as an integer.

        Args:
            arg: Dummy value (not used).

        Prints:
            The integer value representing all bits.
        """
        print(self.data)

# Instantiate Bit object
b = Bit()

# Process all commands
for _ in range(int(input())):
    # Read operation and argument; pad with dummy if necessary
    op, arg = (input() + ' 1').split()[:2]
    b.process(op, arg)