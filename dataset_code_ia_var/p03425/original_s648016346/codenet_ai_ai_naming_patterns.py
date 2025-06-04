import itertools as iterools
import collections as colls

input_lines = open(0).read().split()
num_lines, *name_list = input_lines

first_letter_counter = colls.Counter(
    name[0] for name in name_list if name[0] in "MARCH"
)

first_letter_counts = list(first_letter_counter.values())

triplet_combinations = iterools.combinations(first_letter_counts, 3)

total_triplets = sum(count1 * count2 * count3 for count1, count2, count3 in triplet_combinations)

print(total_triplets)