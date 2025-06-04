from string import ascii_letters as nm_ascii_letters
from collections import defaultdict as nm_defaultdict

def nm_read_int_list():
    return list(map(int, input().split()))

nm_letter_group_map = {nm_letter: nm_index // 13 for nm_index, nm_letter in enumerate(nm_ascii_letters)}
nm_group_count = nm_defaultdict(int)
nm_result_string = ""

input()
for nm_char in input():
    nm_group_count[nm_letter_group_map[nm_char]] += 1

if nm_group_count[0] > nm_group_count[1]:
    nm_result_string = "a" * (nm_group_count[0] - nm_group_count[1])
else:
    nm_result_string = "z" * (nm_group_count[1] - nm_group_count[0])

if nm_group_count[2] > nm_group_count[3]:
    nm_result_string += "A" * (nm_group_count[2] - nm_group_count[3])
else:
    nm_result_string += "Z" * (nm_group_count[3] - nm_group_count[2])

print(len(nm_result_string))
print(nm_result_string)