import sys

palindrome_count = 0
for input_line in sys.stdin:
    stripped_word = input_line.rstrip('\n')
    if stripped_word == stripped_word[::-1]:
        palindrome_count += 1
print(palindrome_count)