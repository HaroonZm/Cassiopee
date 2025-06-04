import sys
from collections import Counter

read_line_from_input = sys.stdin.readline

number_of_values, modulo_divisor = map(int, read_line_from_input().split())

unique_residues_by_modulo = [0] * modulo_divisor
duplicate_residues_by_modulo = [0] * modulo_divisor

input_numbers = map(int, read_line_from_input().split())
counts_of_each_number = Counter(input_numbers)

for value, count in counts_of_each_number.items():
    residue_class = value % modulo_divisor
    unique_residues_by_modulo[residue_class] += count % 2
    duplicate_residues_by_modulo[residue_class] += count - (count & 1)

maximum_pairs = (unique_residues_by_modulo[0] + duplicate_residues_by_modulo[0]) // 2

for offset_from_zero in range(1, (modulo_divisor + 1) // 2):
    symmetric_offset = modulo_divisor - offset_from_zero

    matching_unique_pairs = min(unique_residues_by_modulo[offset_from_zero], unique_residues_by_modulo[symmetric_offset])

    unmatched_uniques_in_offset = unique_residues_by_modulo[offset_from_zero] - matching_unique_pairs
    unmatched_uniques_in_symmetric = unique_residues_by_modulo[symmetric_offset] - matching_unique_pairs

    additional_pairs_from_uniques_and_duplicates_offset = min(unmatched_uniques_in_offset, duplicate_residues_by_modulo[symmetric_offset])
    additional_pairs_from_uniques_and_duplicates_symmetric = min(unmatched_uniques_in_symmetric, duplicate_residues_by_modulo[offset_from_zero])

    additional_pairs_from_duplicate_offset = (duplicate_residues_by_modulo[symmetric_offset] - additional_pairs_from_uniques_and_duplicates_offset) // 2
    additional_pairs_from_duplicate_symmetric = (duplicate_residues_by_modulo[offset_from_zero] - additional_pairs_from_uniques_and_duplicates_symmetric) // 2

    maximum_pairs += (
        matching_unique_pairs
        + additional_pairs_from_uniques_and_duplicates_offset
        + additional_pairs_from_uniques_and_duplicates_symmetric
        + additional_pairs_from_duplicate_offset
        + additional_pairs_from_duplicate_symmetric
    )

if modulo_divisor % 2 == 0:
    half_modulo_index = modulo_divisor // 2
    maximum_pairs += (unique_residues_by_modulo[half_modulo_index] + duplicate_residues_by_modulo[half_modulo_index]) // 2

print(maximum_pairs)