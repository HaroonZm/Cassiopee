def get_min_index(index_a, index_b):
    if index_a == -1 and index_b == -1:
        return -1
    elif index_a == -1:
        return index_b
    elif index_b == -1:
        return index_a
    else:
        return index_b if index_a >= index_b else index_a

input_length = int(input())
input_string = input()

stamp_counter = 0
current_index = 0

while True:
    ox_index = input_string[current_index:].find("OX")
    xo_index = input_string[current_index:].find("XO")
    min_index = get_min_index(ox_index, xo_index)
    if min_index == -1:
        break
    stamp_counter += 1
    current_index += min_index + 2
print(stamp_counter)