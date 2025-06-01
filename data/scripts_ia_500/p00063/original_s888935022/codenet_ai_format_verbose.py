import sys

def is_palindrome(text: str) -> bool:
    return text == text[::-1]

def count_palindromic_lines(lines: list[str]) -> int:
    stripped_lines = [line.strip() for line in lines]
    palindromic_lines = [line for line in stripped_lines if is_palindrome(line)]
    return len(palindromic_lines)

input_lines = sys.stdin.readlines()

palindromic_line_count = count_palindromic_lines(input_lines)

print(palindromic_line_count)