class IPAddressValidator:
    def __init__(self, segment: str):
        self.segment = segment

    def is_valid(self) -> bool:
        if not self.segment:
            return False
        # Leading zero check
        if len(self.segment) > 1 and self.segment[0] == '0':
            return False
        # Value range check
        try:
            val = int(self.segment)
        except ValueError:
            return False
        return 0 <= val <= 255


class IPAddressSplitter:
    def __init__(self, s: str):
        self.s = s
        self.length = len(s)
        self.cache = {}

    def count_valid_ips(self) -> int:
        # Start splitting into 4 parts from index 0
        return self._count_ways(0, 4)

    def _count_ways(self, start: int, parts_left: int) -> int:
        if (start, parts_left) in self.cache:
            return self.cache[(start, parts_left)]
        # If no parts left, check if consumed full string
        if parts_left == 0:
            return 1 if start == self.length else 0
        count = 0
        # IPv4 segment max length is 3
        for end in range(start + 1, min(self.length, start + 3) + 1):
            segment = self.s[start:end]
            validator = IPAddressValidator(segment)
            if validator.is_valid():
                count += self._count_ways(end, parts_left - 1)
        self.cache[(start, parts_left)] = count
        return count


class IPAddressSolutionFacade:
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.splitter = IPAddressSplitter(input_string)

    def execute(self) -> int:
        return self.splitter.count_valid_ips()


if __name__ == "__main__":
    import sys

    input_string = sys.stdin.readline().strip()
    solution = IPAddressSolutionFacade(input_string)
    print(solution.execute())