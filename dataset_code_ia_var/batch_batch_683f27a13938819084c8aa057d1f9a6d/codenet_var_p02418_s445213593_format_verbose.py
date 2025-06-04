original_string = input()
pattern_string = input()

doubled_string = original_string * 2

pattern_found_index = doubled_string.find(pattern_string)

if pattern_found_index != -1:
    print('Yes')
else:
    print('No')