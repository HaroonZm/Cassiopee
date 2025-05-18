import sys

for input_line in sys.stdin:
    input_line = input_line.split()
    input_line = [int(char) for char in input_line]
    input_line.sort(reverse=True)
    input_line = [str(num) for num in input_line]
    print ' '.join(input_line)