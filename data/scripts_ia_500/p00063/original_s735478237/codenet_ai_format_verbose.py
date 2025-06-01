import sys

palindrome_count = 0

for input_line in sys.stdin:
    
    stripped_line = input_line[:-1]
    reversed_line_excluding_last = stripped_line[::-1]

    if stripped_line == reversed_line_excluding_last:
        palindrome_count += 1

print(palindrome_count)