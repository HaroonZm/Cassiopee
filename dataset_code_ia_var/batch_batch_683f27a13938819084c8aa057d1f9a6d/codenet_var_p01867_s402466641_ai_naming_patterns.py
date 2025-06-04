read_input_first = input()
read_input_string = input()
split_input_terms = read_input_string.split("+")
distinct_items = []
distinct_counts = []
for term in split_input_terms:
    found_duplicate = False
    distinct_index = 0
    for distinct_item in distinct_items:
        if distinct_item == term:
            found_duplicate = True
            distinct_counts[distinct_index] += 1
            break
        distinct_index += 1
    if not found_duplicate:
        distinct_items.append(term)
        distinct_counts.append(1)
category_frequencies = [0 for category_iter in range(9)]
for count in distinct_counts:
    category_frequencies[count - 1] += 1
result_total = 0
result_total += 2 * category_frequencies[0]
for frequency_index in range(1, 9):
    if category_frequencies[frequency_index] >= 3:
        result_total += 2 * category_frequencies[frequency_index] + 4
    else:
        result_total += 4 * category_frequencies[frequency_index]
result_total -= 1
print(result_total)