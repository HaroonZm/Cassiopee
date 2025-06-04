import sys
import math
from collections import Counter

input_string_length = int(input())
input_string = input()

modulo_value = 1000000007

substring_count = 1
character_counter = Counter()
character_counter[input_string[0]] += 1

for current_char in input_string[1:]:
    if current_char in character_counter:
        current_product = 1
        for counted_char, counted_count in character_counter.items():
            if counted_char == current_char:
                continue
            current_product = (current_product * (1 + counted_count)) % modulo_value
        substring_count = (substring_count + current_product) % modulo_value
        character_counter[current_char] += 1
    else:
        substring_count = (2 * substring_count) % modulo_value
        substring_count = (substring_count + 1) % modulo_value
        character_counter[current_char] += 1

print(substring_count)