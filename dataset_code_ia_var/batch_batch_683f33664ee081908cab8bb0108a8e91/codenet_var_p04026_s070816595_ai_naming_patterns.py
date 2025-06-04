input_string = input()
input_length = len(input_string)
found_pair = False

for index_adjacent in range(input_length - 1):
    if input_string[index_adjacent] == input_string[index_adjacent + 1]:
        print(index_adjacent + 1, index_adjacent + 2)
        found_pair = True
        break

if not found_pair:
    for index_separated in range(input_length - 2):
        if input_string[index_separated] == input_string[index_separated + 2]:
            print(index_separated + 1, index_separated + 3)
            found_pair = True
            break

if not found_pair:
    print(-1, -1)