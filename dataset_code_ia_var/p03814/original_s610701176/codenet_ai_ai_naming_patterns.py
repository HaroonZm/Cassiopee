input_string = input()
input_length = len(input_string)
index_list_a = []
index_list_z = []
result_count = 0
for index in range(input_length):
    if input_string[index] == "A":
        index_list_a.append(index)
    elif input_string[index] == "Z":
        index_list_z.append(index)

result_count = (max(index_list_z) - min(index_list_a) + 1)
print(result_count)