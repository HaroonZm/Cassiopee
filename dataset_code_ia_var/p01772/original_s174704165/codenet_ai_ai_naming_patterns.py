input_string = raw_input()
is_a_found = False
az_count = 0
for char in input_string:
    is_a_found |= char == "A"
    if char == "Z" and is_a_found:
        az_count += 1
        is_a_found = False
output_string = "AZ" * az_count if az_count > 0 else -1
print output_string