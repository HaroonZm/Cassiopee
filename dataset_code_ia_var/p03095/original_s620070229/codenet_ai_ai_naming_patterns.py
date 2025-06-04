from collections import Counter

CONST_MODULO = 10 ** 9 + 7
_ignored_input = input()
string_input = input()
result_value = 1
character_counter = Counter(string_input)
for character_count in character_counter.values():
    result_value *= character_count + 1
    result_value %= CONST_MODULO
print(result_value - 1)