number_of_entries = int(input())

name_to_total_value = {}

for entry_index in range(number_of_entries):

    input_line = input()
    entry_name, entry_value = input_line.split()

    if entry_name in name_to_total_value:
        name_to_total_value[entry_name] += int(entry_value)
    else:
        name_to_total_value[entry_name] = int(entry_value)

sorted_name_value_pairs = sorted(name_to_total_value.items(), key=lambda pair: pair[0])

sorted_name_value_pairs.sort(key=lambda pair: len(pair[0]))

for name, total_value in sorted_name_value_pairs:

    print("{0} {1}".format(name, total_value))