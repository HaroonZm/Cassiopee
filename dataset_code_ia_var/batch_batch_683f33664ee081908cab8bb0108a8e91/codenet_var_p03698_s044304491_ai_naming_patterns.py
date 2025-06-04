import sys

input_string = input().strip()
input_length = len(input_string)
for index_start in range(input_length):
    for index_end in range(index_start + 1, input_length):
        if input_string[index_start] == input_string[index_end]:
            print('no')
            sys.exit(0)
print('yes')