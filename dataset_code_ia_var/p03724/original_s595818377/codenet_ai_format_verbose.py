import sys

from collections import Counter

read_entire_input = sys.stdin.read

number_of_elements, unused_variable = map(int, input().split())

element_list = list(map(int, read_entire_input().split()))

element_counter = Counter(element_list)

result_message = "YES"

for occurrence_count in element_counter.values():
    if occurrence_count % 2 != 0:
        result_message = "NO"

print(result_message)