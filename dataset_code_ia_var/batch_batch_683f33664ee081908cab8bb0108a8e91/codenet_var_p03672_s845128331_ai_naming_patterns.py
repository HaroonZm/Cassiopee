import sys
read_line = sys.stdin.readline

input_chars = list(read_line().rstrip())
if len(input_chars) % 2 == 0:
    input_chars.pop()
    input_chars.pop()
else:
    input_chars.pop()
half_length = len(input_chars) // 2
if input_chars[:half_length] == input_chars[half_length:]:
    print(len(input_chars))
    sys.exit()
for trim_index in range(len(input_chars) // 2):
    input_chars.pop()
    input_chars.pop()
    half_length = len(input_chars) // 2
    if input_chars[:half_length] == input_chars[half_length:]:
        print(len(input_chars))
        sys.exit()