input_string = raw_input()
temp_string = input_string.replace("apple", "TEMP_FRUIT")
temp_string = temp_string.replace("peach", "apple")
result_string = temp_string.replace("TEMP_FRUIT", "peach")
print result_string