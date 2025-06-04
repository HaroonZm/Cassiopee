import sys

for input_line in sys.stdin:
    value_int = int(input_line)
    if value_int >= 30:
        print("Yes")
    else:
        print("No")