from math import sqrt
from itertools import combinations

total_pairs = int(input())

number_of_groups = round((1 + sqrt(1 + 8 * total_pairs)) / 2)

if number_of_groups * (number_of_groups - 1) != 2 * total_pairs:
    print('No')
    exit()

print('Yes')
print(number_of_groups)

group_elements_lists = [list() for _ in range(number_of_groups)]

for pair_index, (first_group, second_group) in enumerate(combinations(range(number_of_groups), 2)):
    group_elements_lists[first_group].append(pair_index + 1)
    group_elements_lists[second_group].append(pair_index + 1)

for elements_list in group_elements_lists:
    number_of_elements = len(elements_list)
    elements_as_str = ' '.join(map(str, elements_list))
    print(number_of_elements, elements_as_str)