class PalindromeChecker:
    def __init__(self, string: str):
        self.string = string

    def is_palindrome(self) -> bool:
        # Considering single-character strings as palindromes by definition
        if len(self.string) == 1:
            return True
        return self.string == self.string[::-1]

class InputHandler:
    def __init__(self):
        self.lines = []

    def read_lines(self) -> None:
        import sys
        for line in sys.stdin:
            line = line.strip()
            if line:
                self.lines.append(line)

class PalindromeProcessor:
    def __init__(self, lines):
        self.lines = lines
        self.palindrome_checkers = [PalindromeChecker(line) for line in lines]

    def count_palindromes(self) -> int:
        return sum(checker.is_palindrome() for checker in self.palindrome_checkers)

class PalindromeApplication:
    def __init__(self):
        self.input_handler = InputHandler()
        self.processor = None

    def run(self) -> None:
        self.input_handler.read_lines()
        self.processor = PalindromeProcessor(self.input_handler.lines)
        count = self.processor.count_palindromes()
        print(count)

if __name__ == "__main__":
    app = PalindromeApplication()
    app.run()