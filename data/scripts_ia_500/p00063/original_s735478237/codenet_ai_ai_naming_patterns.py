import sys
palindrome_count = sum(line[:-1] == line[-2::-1] for line in sys.stdin)
print(palindrome_count)