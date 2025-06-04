input()
sequence_a_raw = input().split()
input()
sequence_b_raw = input().split()

sequence_a_int = list(map(int, sequence_a_raw))
sequence_b_int = list(map(int, sequence_b_raw))

set_a_int = set(sequence_a_int)
set_b_int = set(sequence_b_int)

is_subset = 1 if set_b_int.issubset(set_a_int) else 0

print(is_subset)