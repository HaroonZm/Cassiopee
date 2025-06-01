class PalindromeChecker:
    def __init__(self):
        self._lines = []
    def add_line(self, line: str):
        self._lines.append(line)
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
    def count_palindromes(self) -> int:
        return sum(1 for line in self._lines if self.is_palindrome(line))
class InputReader:
    def __init__(self, source):
        self._source = source
    def read_all(self):
        for line in self._source:
            yield line.rstrip('\n')
class PalindromeApp:
    def __init__(self, input_source):
        self._reader = InputReader(input_source)
        self._checker = PalindromeChecker()
    def run(self):
        for line in self._reader.read_all():
            if line:
                self._checker.add_line(line)
        print(self._checker.count_palindromes())
if __name__ == "__main__":
    import sys
    app = PalindromeApp(sys.stdin)
    app.run()