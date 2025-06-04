user_input_string = input()

total_valid_partitions = 0

for partition_index in range(1, len(user_input_string)):
    
    left_substring = user_input_string[:partition_index]
    right_substring = user_input_string[partition_index:]
    
    if right_substring[0] == "0":
        continue
    
    left_number = int(left_substring)
    right_number = int(right_substring)
    
    if (left_number + right_number) % 2 == 0 \
        and right_number >= left_number \
        and (right_number - left_number) % 2 == 0:
        
        total_valid_partitions += 1

if int(user_input_string) % 2 == 0:
    total_valid_partitions += 1

print(total_valid_partitions)