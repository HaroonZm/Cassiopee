import sys

input_string = input()

for character in input_string:
    if input_string.count(character) != 2:
        print("No")
        sys.exit()

print("Yes")