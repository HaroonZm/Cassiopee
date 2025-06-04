import re

input_text = input()
pattern_with_underscores = input()

pattern_with_wildcards = pattern_with_underscores.replace('_', '.')

pattern_found_in_text = re.search(pattern_with_wildcards, input_text)

if pattern_found_in_text:
    print('Yes')
else:
    print('No')