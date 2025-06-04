import sys
def read_input_line(): return sys.stdin.readline().rstrip()
def read_multiple_ints(): return map(int, read_input_line().split())

input_string = read_input_line()

reversed_string = input_string[::-1]
sliced_reversed_string = reversed_string[8:]
restored_string = sliced_reversed_string[::-1]

print(restored_string)